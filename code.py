# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    weather_df_monthly=df.resample(period).sum()
    plt.plot(weather_df_monthly.index.values,weather_df_monthly[col])
    plt.show()






# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    sns.countplot(x='Weather', data=df)
    plt.xticks(rotation=90)
    plt.show()








# Function to plot continous plots
def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    if(plt_typ=='distplot'):
        sns.distplot(df['Temp (C)'])
        sns.distplot(df['Dew Point Temp (C)'])
        sns.distplot(df['Rel Hum (%)'])
        sns.distplot(df['Wind Spd (km/h)'])
        sns.distplot(df['Visibility (km)'])

        sns.distplot(df['Stn Press (kPa)'])
    elif(plt_typ=='boxplot'):
        sns.boxplot(df['Temp (C)'])    
    plt.show()








# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    grouping=df.groupby([col1])[col2].agg(agg1)
    grouping.plot(kind='bar')
    plt.show()
    return grouping
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df=pd.read_csv(path,parse_dates=['Date/Time'],index_col=['Date/Time'])


categorical_var=weather_df.select_dtypes(include='object')
print(categorical_var)
numerical_var=weather_df.select_dtypes(include='number')
print(numerical_var)
# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
line_chart(weather_df,'M','Temp (C)')

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(weather_df)
# Let's p
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
plot_cont(weather_df,'distplot')
# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(weather_df,'boxplot')

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
group_values(weather_df,'Weather','mean','Visibility (km)')



