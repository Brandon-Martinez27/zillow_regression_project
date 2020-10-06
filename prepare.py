import pandas as pd
import acquire

def acquire_and_prep_data():
    df = acquire .get_zillow_data()

    df = df.drop

    df = df[['calculatedfinishedsquarefeet','bathroomcnt', 'bedroomcnt', 'regionidzip', 'fips', 'taxamount', 'taxvaluedollarcnt', 'yearbuilt']]

    df['bedroomcnt'] = df['bedroomcnt'].astype(int)
    df['calculatedfinishedsquarefeet'] = df['calculatedfinishedsquarefeet'].astype(int)
    df['regionidzip']=df['regionidzip'].astype(int)
    df['fips'] = df['fips'].astype(int)
    df['yearbuilt']=df['yearbuilt'].astype(int)

    df = df.rename(columns={'calculatedfinishedsquarefeet': 'sqft', 'regionidzip': 'zipcode'})