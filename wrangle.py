import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from env import host, user, password
import os
import warnings
warnings.filterwarnings("ignore")
import acquire_g
from sklearn.preprocessing import MinMaxScaler


########################## Establishing connection ###########################
# establish mysql connection
def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

########################## Creating function to get data ######################
def new_zillow_data():
    '''
    This function reads the zillow data from the Codeup db into a df,
    write it to a csv file, and returns the df. 
    '''
    # Selecting all data in the properties_2017 table
    sql_query = '''SELECT * FROM properties_2017 as prop
                LEFT JOIN predictions_2017 as pred on prop.id = pred.id
                LEFT JOIN propertylandusetype as pluy on prop.propertylandusetypeid = pluy.propertylandusetypeid
                WHERE transactiondate between '2017-05-01' and '2017-06-30'
                AND prop.propertylandusetypeid IN (261, 263, 264, 266, 270, 273, 274, 275, 279)'''

    # The pandas read_sql function allows us to create a df with the afformentioned sql querry    
    df = pd.read_sql(sql_query, get_connection('zillow'))

    # Converts the df into a csv
    df.to_csv('zillow_df.csv')

    # This prevents any duplicated columns. The ~ allows to return the unique columns. A boolean array is created
    # and only falses are returned
    df = df.loc[:,~df.columns.duplicated()]

    return df

def get_zillow_data(cached=False):
    '''
    This function reads in zillow data from Codeup database if cached == False, a csv is created
    returning the df. If cached == True, the function reads in the zillow df from a csv file & returns df
    '''
    # This runs if there is no csv containing the zillow data
    if cached or os.path.isfile('zillow_df.csv') == False:

        # Converts the df into a csv
        df = new_zillow_data()

    else:

        # If the csv was stored locally, the csv will return the df
        df = pd.read_csv('zillow_df.csv', index_col=0)

    return df

    ####################### Function to prep ############################
    # Creating an acquire prep data function to clean and prep the paramaters that we will be using
def acquire_and_prep_data():
    # Using the get_zillow_data function to acquire
    df = acquire_g.get_zillow_data()

    # Selecting the parameters for exploring
    df = df[['calculatedfinishedsquarefeet','bathroomcnt', 'bedroomcnt', 'regionidzip', 'fips', 'taxamount', 'taxvaluedollarcnt', 'yearbuilt']]

    # Dropping missing data
    df = df.dropna()

    # Changing some data types as integers instead of floats
    df['bedroomcnt'] = df['bedroomcnt'].astype(int)
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].astype(int)
    df['regionidzip']=df['regionidzip'].astype(int)
    df['fips'] = df['fips'].astype(int)
    df['yearbuilt']=df['yearbuilt'].astype(int)

    # Renaming columns to read easier
    df = df.rename(columns={'calculatedfinishedsquarefeet': 'sqft', 'regionidzip': 'zipcode'})

    # Adding tax rate
    df['tax_rate'] = round((df['taxamount'] / df['taxvaluedollarcnt']) * 100 , 2)

    # Adding county from the function created above
    df['county'] = df.apply(lambda x: fips_labels(x), axis=1)

    # dropping fips now since I have the county
    df = df.drop(columns = ['fips'])

    return df

    ########################### Function to split #############################
    # Function to split data into train, validate, test datasets
def zillow_split(df):
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test

########################## Function to scale ###########################
# Function will scale the train, validate and test
def add_scaled_columns(train, validate, test, scaler, columns_to_scale):
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    scaler.fit(train[columns_to_scale])
    
    train = pd.concat([
        train, pd.DataFrame(scaler.transform(train[columns_to_scale]), 
                            columns=new_column_names, 
                            index=train.index),], axis=1)
    validate = pd.concat([
        validate, pd.DataFrame(scaler.transform(validate[columns_to_scale]), 
                            columns=new_column_names, 
                            index=validate.index),], axis=1)
    test = pd.concat([
        test, pd.DataFrame(scaler.transform(test[columns_to_scale]), 
                            columns=new_column_names, 
                            index=test.index),], axis=1)
    return train, validate, test

