import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#Loading the data
df = pd.read_csv('WorldCupMatches.csv')
print(df.head())

#Generating total number of goals colums
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())

#Bar Chart
f, ax = plt.subplots(figsize=(12,7))
sns.set_style('whitegrid')
sns.set_context('poster', font_scale=.8)
ax = sns.barplot(data=df, x='Year',y='Total Goals')
ax.set_title('Total Goals per Year')
plt.show()

#Visualizing distribution of the goals data
df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Goal Distribution')
plt.show()