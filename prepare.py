import pandas as pd
import acquire_g

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

    # Renaming columns to read easier
    df = df.rename(columns={'calculatedfinishedsquarefeet': 'sqft', 'regionidzip': 'zipcode'})

    # Adding tax rate
    df['tax_rate'] = round((df['taxamount'] / df['taxvaluedollarcnt']) * 100 , 2)

    # Adding county from the function created above
    df['county'] = df.apply(lambda x: fips_labels(x), axis=1)

    # dropping fips now since I have the county
    df = df.drop(columns = ['fips'])

    return df