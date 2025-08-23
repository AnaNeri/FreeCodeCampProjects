import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date']).set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = df.plot(legend=False, figsize=[12,3.5], color='red', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views').figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()
    df_bar = df_bar.groupby(['Years', 'Months']).mean()    
    df_bar = df_bar.unstack(level='Months')
    df_bar.columns = df_bar.columns.droplevel(0)
    
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[month_order]
    
    # Draw bar plot
    fig = df_bar.plot(figsize = [7,6], kind='bar', ylabel='Average Page Views').figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True).sort_values()
    
    fig, axes= plt.subplots(1,2, figsize = (10,4))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], palette='husl', legend=False, hue='year')
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], palette='husl', legend=False, hue='month')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_ylabel('Page Views')
    axes[0].set_xlabel('Year')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

