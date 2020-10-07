import pandas as pd
import numpy as np


def min_max_scale(X_train, X_validate, X_test):
    # import scaler
    from sklearn.preprocessing import MinMaxScaler
    # Create scaler object
    scaler = MinMaxScaler(copy=True).fit(X_train)
    
    # tranform into scaled data (arrays)
    X_train_scaled = scaler.transform(X_train)
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)
    
    # Create dataframes out of the scaled arrays that were generated by the scaler tranform.
    X_train_scaled = pd.DataFrame(X_train_scaled, 
                              columns=X_train.columns.values).\
                            set_index([X_train.index.values])

    X_validate_scaled = pd.DataFrame(X_validate_scaled, 
                                columns=X_validate.columns.values).\
                            set_index([X_validate.index.values])

    X_test_scaled = pd.DataFrame(X_test_scaled, 
                                columns=X_test.columns.values).\
                            set_index([X_test.index.values])
    return X_train_scaled, X_validate_scaled, X_test_scaled

def select_kbest(X, y, n):
    '''Uses correlation to select the best k number of features 
    to use in a model'''
    # import the selector
    from sklearn.feature_selection import SelectKBest, f_regression
    # create the selector and fit it to the scaled data
    f_selector = SelectKBest(f_regression, k=n).fit(X, y)
    # get the 'selected/best' features with boolean mask
    f_support = f_selector.get_support()
    # return the actual column names of selected features into a list
    f_feature = X.iloc[:,f_support].columns.tolist()
    return f_feature

def rfe(X, y, n):
    '''Uses a linear regression model to predict the best features'''
    # import the selector
    from sklearn.feature_selection import RFE
    # import the linear regression model
    from sklearn.linear_model import LinearRegression
    # create the model object
    lm = LinearRegression()
    # create the rfe selector
    rfe = RFE(lm, n)
    # fit and transform the selector to the scaled data
    X_rfe = rfe.fit_transform(X, y)
    # get the 'best' features in a boolean mask
    mask = rfe.support_
    # map the features to the mask
    X_reduced_scaled_rfe = X.iloc[:,mask]
    # get the columns of the best features and add to a list
    f_feature = X_reduced_scaled_rfe.columns.tolist()
    return f_feature

