'''
Created on Nov 27, 2017
predict the stock price using linear regression

$ sudo pip install requests --ignore-installed
$ sudo pip install numpy --upgrade --ignore-installed
$ sudo pip install scipy --upgrade --ignore-installed
$ sudo pip install scikit-learn --upgrade --ignore-installed
$ sudo pip install pandas --ignore-installed

@author: Kuei-Lin Yang (Hubert)
'''

import sys
import time
import requests
import re
import datetime

import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, linear_model
import matplotlib.pyplot as plt

def find_crumb_store(lines):
    for l in lines:
        if re.findall(r'CrumbStore', l):
            #print type(l), l
            return l.split(':')[2].strip('"')
    print 'Cannot find CrumbStore'
    sys.exit(1)
    
def get_page_data(symbol):
    url = 'https://finance.yahoo.com/quote/%s/?p=%s' % (symbol, symbol)
    try:
        r = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
    
    cookie = {'B': r.cookies['B']}
    lines = r.content.decode('unicode-escape').strip().replace('}', '\n').split('\n')
    return cookie, lines
    
def get_cookie_crumb(symbol):
    (cookie, lines) = get_page_data(symbol)
    #print type(lines), lines
    crumb = find_crumb_store(lines)
    return cookie, crumb

def get_data(symbol, start_date, end_date, cookie, crumb):
    url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&crumb=%s" % (symbol, start_date, end_date, crumb)
    try:
        r = requests.get(url, cookies=cookie)
        with open(symbol, 'wb') as wf:
            for block in r.iter_content(1024):
                wf.write(block)
        print 'Download successfully!'
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)
        
def download_quotes(symbol):
    start_date = 0
    end_date = int( time.time() )
    (cookie, crumb) = get_cookie_crumb(symbol)
    get_data(symbol, start_date, end_date, cookie, crumb)
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        symbol = sys.argv[1]
        print 'Download %s ...' % (symbol)
        download_quotes(symbol)
    else:
        print 'Usage: python StockLinearRegression.py SYMBOL'
        sys.exit(1)

    df = pd.read_csv(symbol)
    # Add a new feature: high low percentage
    df['HL_PCT'] = (df['High'] - df['Low']) / (df['Low']*100)
    # Add a new feature: close open percentage change
    df['PCT_CHNG'] = (df['Close'] - df['Open']) / (df['Open']*100)
    
    forecast_col = 'Close'
    forecast_out = int(30)
    #print 'length = {}, and forecast_out = {}'.format(len(df), forecast_out)
    df['Label'] = df[forecast_col].shift(-forecast_out)    
    df_label = df[['Close', 'HL_PCT', 'PCT_CHNG', 'Volume', 'Label']]
    
    X = np.array(df_label.drop(['Label'], 1))
    X = preprocessing.scale(X)
    #print 'Length of X: {}'.format(len(X))
    
    X_forecast_out = X[-forecast_out:]
    print 'Length of X_forecast_out: {}'.format(len(X_forecast_out))
    X = X[:-forecast_out]
    print 'Length of X: {}'.format(len(X))
    
    y = np.array(df['Label'])
    y = y[:-forecast_out]
    print 'Length of y: {}'.format(len(y))
    
    # Create training and test sets
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
    print 'Length of X_train: {}, X_test:{}'.format(len(X_train), len(X_test))
    print 'Length of y_train: {}, y_test:{}'.format(len(y_train), len(y_test))
    
    # Train by linear regression
    clf = linear_model.LinearRegression()
    clf.fit(X_train, y_train)
    
    # Test
    accuracy = clf.score(X_test, y_test)
    print 'Accuracy of Linear Regression:{}'.format(accuracy)
    
    # Predict
    forecast_prediction = clf.predict(X_forecast_out)
    print forecast_prediction
    
    # Plot
    df_label.dropna(inplace=True)
    df_label['Forecast'] = np.nan
    last_date = df.iloc[-1][0]
    last_unix = int(time.mktime(time.strptime(last_date, "%Y-%m-%d")))
    #print last_unix
    one_day = 86400
    next_unix = last_unix + one_day
    
    for i in forecast_prediction:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += 86400
        df_label.loc[next_date] = [np.nan for _ in range(len(df_label.columns)-1)]+[i]
    
    df_label['Close'].plot(figsize=(15,6), color="green")
    df_label['Forecast'].plot(figsize=(15,6), color="orange")
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    