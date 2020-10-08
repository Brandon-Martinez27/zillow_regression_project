# Zillow Regression Project

### Author George Arredondo and Brandon Martinez

## Description:
We have been tasked by the Zillow Data Science team to predict single unit property tax assessment value.

## [Presentation](https://www.canva.com/design/DAEKBO5FrUg/share/preview?token=dlLZoS3lS9x_ruYsoCnYQQ&role=EDITOR&utm_content=DAEKBO5FrUg&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

## Goals
- Predict values of single unit properties using property data from the Zillow database on the Codeup SQL server. The focus will be specifically on the property values on the hot months of May & June 2017.
- Need property locations (state and county)
- Plot distribution of tax rates by county
- Create a presentation of findings

## Background
> We want to be able to predict the values of single unit properties that the tax district assesses using the property data from those whose last transaction was during the "hot months" (in terms of real estate demand) of May and June in 2017. We also need some additional information outside of the model.

> Zach lost the email that told us where these properties were located. Ugh, Zach :-/. Because property taxes are assessed at the county level, we would like to know what states and counties these are located in.

> We'd also like to know the distribution of tax rates for each county.
The data should have the tax amounts and tax value of the home, so it shouldn't be too hard to calculate. Please include in your report to us the distribution of tax rates for each county so that we can see how much they vary within the properties in the county and the rates the bulk of the properties sit around.

> Note that this is separate from the model you will build, because if you use tax amount in your model, you would be using a future data point to predict a future data point, and that is cheating! In other words, for prediction purposes, we won't know tax amount until we know tax value.

## Key Terms
- [Parcelid](https://en.wikipedia.org/wiki/Assessor%27s_parcel_number) is a number assigned to parcels of real property by the tax assessor of a particular jurisdiction for purposes of identification and record-keeping.
- A [single-unit property](https://help.rentingwell.com/article/multi-unit-vs-single-unit/) is a rental property that is rented as a single entity. A condo, a townhouse, or a vacation rental would typically be single-unit properties. If you’re adding a single-unit property to Renting Well you don’t need to add individual units – the tenant and lease are associated to the property itself.
- [FIPS](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt#:~:text=FIPS%20codes%20are%20numbers%20which,to%20which%20the%20county%20belongs.) codes are numbers which uniquely identify geographic areas. The number of digits in FIPS codes vary depending on the level of geography. State-level FIPS codes have two digits, county-level FIPS codes have five digits of which the first two are the FIPS code of the state to which the county belongs.

## Data Dictionary
| Feature | Definition |
| --- | --- |
| fullbathcnt | Number of full bathrooms |
| sqft | Property structure square footage |
| bathroomcnt | Number of bathrooms (includes half baths) |
| bedroomcnt | Number of bedrooms |
| county | County associated with property |
| taxamount | Taxes for property |
| yearbuilt | Year property was built |
| tax_rate | Calculation of (taxamount/ home_value) * 100 | 

| Target | Definition |
| --- | --- |
| home_value | Value of the property |

## Inital Hypothesis & Thoughts
> H<sub>0</sub>: There is no relationship between home values and the number of bedrooms, bathrooms and square feet.

> H<sub>a</sub>: There is a relationship between home values and the number of bedrooms, bathrooms and square feet.

## Project Planning

### Acquire
- Create an acquire.py file that contains functions to establish a connection and get the data from the Codeup SQL database.
- ENV file is needed for credentials to access the database

### Prepare
- Create a prepare.py file that contains functions to prepare, explore, and split the data. 
- Null values are dropped
- Data types are adjusted to get ready for modeling
- Features are selected and renamed
- Filters are selected to remove outliers

### Explore
- Variables are visualized
- Statistical tests performed to confirm inital hypothesis

### Model
- Establish a baseline model
- Show visual of model performing better than the baseline
- Document algorithims and hyperameters
- Compute SSE, RMSE, & MSE (plotting y by yhat)
- Create model.py that has functions to fit, predict, evaluate, the final model of the test settling

### Conclusions
- We found that square footage, bedroom count and bathroom count are drivers for market value of single unit properties
- Polynomial model performed 24% better than the baseline with the drivers described above
- The properties are located in southern California in Los Angeles County, Orange County and Ventura County
- Los Angeles County has the highest tax rate of all three counties 
- Los Angeles County has a large variation in tax rate compared to the other counties and has the most properties

## How to Reproduce 
- Use functions in acquire.py file to acquire data
    * Must have env file for Codeup SQL credentials 
- Use functions in prepare.py for data prepartion
- Use functions model.py to model