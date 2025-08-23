import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x =df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Create scatter plot
    plt.scatter(x=x, y=y)

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x, y)
    years_extended = [i for i in range(1880, 2051, 1)]
    
    line= [intercept + slope*xi for xi in years_extended ]
    plt.plot(years_extended, line)

    # Create second line of best fit
    x_extend_s = [i for i in range(2000, 2051, 1)]
    x_s = df[(df['Year']>= 2000)]['Year']
    y_s = df[(df['Year']>= 2000)]['CSIRO Adjusted Sea Level']
    
    slope, intercept, r, p, se = linregress(x_s, y_s)
    
    line_s = [intercept + slope*xi for xi in x_extend_s ]
    plt.plot(x_extend_s, line_s)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

