# Zillow Project Summary

# Goal
- Predict values of single unit properties using the property data form those whos last transaction was during the hot months of May & June 2017
- Need property location State & County
- Tax rates of each county using tax amounts & tax values. Distribution of tax rates - seperate from the model. We don't know tax amounts until we know tax value

# Audience
- Zillow data science team

# Deliverables 
- Presentation - summarize single unit property values.
- Explore phase with visualizations
- Github with 1 notebook for explore and 1 notebook with modeling
- Explore: at least 1 statistical test with visualization documenting the hypothesis test
    - At least 1 T-test and 1 correlation test
- Modeling: Establish baseline to beat with algorithims & hyperparameters.
- .py files to reproduce
- README.md with planning, instructions to clone, goals of project, data dictionary, key finding/ takeaways

# Project Guidance
- 1st itteration use sq.ft of home, # of bedrooms, # of baths, to establish property value
- Scale after establishing a baseline

# Acquire
- Acquire from the SQL db 
 
# Prepare
- Split data into train, validate, and test
- Plot distributions of individual variables to see how to handle outliers
- Address nulls, missing data, & data integrity issues
- units measures to decide how to scale

# Exploration
- Address questions from planning and brainstorming, visuals and statistical analysis
- At least 1 T-test and 1 correlation test
- Visualize all combos of variables ie. heatmat
- What independent variables correlate with dependent variable. What independent variables correlate with other independent variables. 
- Summarize take aways and conclusions

# Modeling
- Show visual of model performing better than the baseline
- Document algorithims used with results before settling for the best model
- Compute SSE, RMSE, & MSE plotting y by yhat
- Create model.py that has functions to fit, predict, evaluate, the final model of the test settling

# Terms
- Parcelid - unique id assigned to the property by the tax assesor
- A single-unit property is a rental property that is rented as a single entity. A condo, a townhouse, or a vacation rental would typically be single-unit properties. If you’re adding a single-unit property to Renting Well you don’t need to add individual units – the tenant and lease are associated to the property itself.
- FIPS codes are numbers which uniquely identify geographic areas. The number of digits in FIPS codes vary depending on the level of geography. State-level FIPS codes have two digits, county-level FIPS codes have five digits of which the first two are the FIPS code of the state to which the county belongs.