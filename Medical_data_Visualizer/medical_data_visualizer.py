import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 - get data
df = pd.read_csv('medical_examination.csv')

# 2 - calculate overweight
df['overweight'] = ((df['weight'] / (df['height']/100)**2) > 25).astype(int)

# 3 - normalize
df['cholesterol'] = df['cholesterol'].replace({0:1, 1:0, 2:1, 3:1})
df['gluc'] = df['gluc'].replace({0:1, 1:0, 2:1, 3:1})

# 4 - Draw the Categorical Plot
def draw_cat_plot():
    # 5 - DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = pd.melt(df, ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6 - Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature.
    df_cat = df_cat[df_cat['variable'] == 'cardio'].groupby('value').agg({
        'cholesterol': lambda x: x.value_counts().to_dict(),
        'gluc': lambda x: x.value_counts().to_dict(),
        'smoke': lambda x: x.value_counts().to_dict(),
        'alco': lambda x: x.value_counts().to_dict(),
        'active': lambda x: x.value_counts().to_dict(),
        'overweight': lambda x: x.value_counts().to_dict()
    }).reset_index().rename({'value':'cardio'}, axis='columns')
    
    # 7 - Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library.
    # Create a list to store DataFrames for each row
    df2 = []

    for _, row in df_cat.iterrows():
        cardio = row['cardio']
        for variable in df_cat.columns[1:]:
            value_counts = row[variable]
            # Convert the dictionary to a DataFrame
            temp_df = pd.DataFrame.from_dict(value_counts, orient='index', columns=['total'])
            temp_df['value'] = temp_df.index
            temp_df['variable'] = variable
            temp_df['cardio'] = cardio
            df2.append(temp_df)

    df_cat = pd.concat(df2, ignore_index=True)
    
    df_cat = df_cat.sort_values('variable')
    # 8 - Get the figure for the output and store it in the fig variable.
    g = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig = g.fig
    
    # 9 - DON'T CHANGE
    fig.savefig('catplot.png')
    return fig

# 10 - Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # 11 - Clean the data 
    df_heat = df[  (df['ap_lo'] <= df['ap_hi']) 
                 & (df['height'] >= df['height'].quantile(0.025)) 
                 & (df['height'] <= df['height'].quantile(0.975))
                 & (df['weight'] >= df['weight'].quantile(0.025))
                 & (df['weight'] <= df['weight'].quantile(0.975))] 

    # 12 - Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr().round(1)
    
    # 13 - Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14 - Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15 - Plot the correlation matrix using the method provided by the seaborn library
    sns.heatmap(corr, mask=mask, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, 
                annot=True, fmt='.1f')

    # 16 - DON'T CHANGE
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()