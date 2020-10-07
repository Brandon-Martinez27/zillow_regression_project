import pandas as pd
import acquire_g
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Alias for fips
def fips_labels(x):
    if x['fips'] == 6037:
        return 'Los Angeles County'
    elif x['fips'] == 6059:
        return 'Orange County'
    elif x['fips'] == 6111:
        return 'Ventura County'

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

    # Adding tax rate
    df['tax_rate'] = round((df['taxamount'] / df['taxvaluedollarcnt']) * 100 , 2)

    # Renaming columns to read easier
    df = df.rename(columns={'calculatedfinishedsquarefeet': 'sqft', 'regionidzip': 'zip_code', 'taxvaluedollarcnt': 'home_value'})

    # Adding county from the function created above
    df['county'] = df.apply(lambda x: fips_labels(x), axis=1)

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
