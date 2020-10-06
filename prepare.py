import pandas as pd
import acquire

# Creating an acquire prep data function to clean and prep the paramaters that we will be using
def acquire_and_prep_data():
    # Using the get_zillow_data function to acquire
    df = acquire .get_zillow_data()

    # Dropping missing data
    df = df.dropna()

    # Selecting the parameters for exploring
    df = df[['calculatedfinishedsquarefeet','bathroomcnt', 'bedroomcnt', 'regionidzip', 'fips', 'taxamount', 'taxvaluedollarcnt', 'yearbuilt']]

    # Changing some data types as integers instead of floats
    df['bedroomcnt'] = df['bedroomcnt'].astype(int)
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].astype(int)
    df['regionidzip']=df['regionidzip'].astype(int)
    df['fips'] = df['fips'].astype(int)
    df['yearbuilt']=df['yearbuilt'].astype(int)

    # Renaming columns to read easier
    df = df.rename(columns={'calculatedfinishedsquarefeet': 'sqft', 'regionidzip': 'zipcode'})

    return df