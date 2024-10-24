import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.stats import linregress # type: ignore

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.subplots(figsize = (10, 6))
    plt. scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Get the slope and the y-intercept for the first line of best fit
    slope, intercept, r_value, p_value, std_err  = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Predicting the sea level rise to 2050
    extended_years = list(range(min(df['Year']), 2051))

    # Create first line of best fit
    line_of_best_fit = [slope * years + intercept for years in extended_years]

    # Plot the first line of best fit
    plt.plot(extended_years, line_of_best_fit, color='red')

    # Create dataframe for second line of best fit
    df_recent = df[df['Year'] >= 2000]

    # Get the slope and the y-intercept for the second line of best fit
    slope_recent, intercept_recent,r_value_recent, p_value_recent, std_err_recent  = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Predicting the sea level rise from 2000 to 2050
    extended_years_recent = list(range(min(df_recent['Year']), 2051))

    # Create second line of best fit
    best_line_fit_recent = [slope_recent * year + intercept_recent for year in extended_years_recent]

    # Plot the second line of best fit
    plt.plot(extended_years_recent, best_line_fit_recent, color='green')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()