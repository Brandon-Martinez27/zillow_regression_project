import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from acquire_b import get_zillow_data

# Alias for fips
def fips_labels(x):
    if x['fips'] == 6037:
        return 'Los Angeles County'
    elif x['fips'] == 6059:
        return 'Orange County'
    elif x['fips'] == 6111:
        return 'Ventura County'

def prep_zillow(cached=True):
    '''
    This function acquires and prepares the zillow data from a local csv, default.
    Passing cached=False acquires fresh data from Codeup db and writes to csv.
    '''
    # use my acquire function to read data into a df from a csv file
    df = get_zillow_data(cached)

    # choose columns that we want to use (features and target)
    df = df[['bathroomcnt', 'bedroomcnt', 'regionidzip', 'fips', 'taxamount', 'taxvaluedollarcnt', 'yearbuilt', 'calculatedfinishedsquarefeet']]

    # drop null columns
    df = df.dropna()

    # change categorical columns to integer
    df[['bedroomcnt', 'regionidzip', 'fips', 'yearbuilt', 'calculatedfinishedsquarefeet']] = \
    df[['bedroomcnt', 'regionidzip', 'fips', 'yearbuilt', 'calculatedfinishedsquarefeet']].astype('int')

    # rename columns for easy reading
    df = df.rename(columns={
    'regionidzip': 'zipcode',
    'calculatedfinishedsquarefeet': 'sqft',
    'taxvaluedollarcnt': 'home_value'})

    # Adding county from the function created above
    df['county'] = df.apply(lambda x: fips_labels(x), axis=1)

    # Adding tax rate
    df['tax_rate'] = round((df['taxamount'] / df['home_value']) * 100 , 2)

    # dropping fips now since I have the county
    df = df.drop(columns = ['fips'])

    # Going to only look at homes with 5 or less bedrooms
    df = df[df.bedroomcnt < 6]

    # Going to only look at homes with 4 or less bathrooms
    df = df[df.bathroomcnt < 5]
    
    return df

# Function to split data into train, validate, test datasets
def zillow_split(df):
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test

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

