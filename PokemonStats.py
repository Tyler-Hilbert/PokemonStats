import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


pokemon_df = pd.read_csv("pokemon.csv")

# Break pokemon of 2 types into 2 entries
stat_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def','Speed', 'Catch_Rate', 'Body_Style']
type_cols = ['Type_1', 'Type_2']
melted = pd.melt(pokemon_df, stat_cols, type_cols, value_name='Type').dropna()

# Describe types
described_stats = melted.groupby('Type')[stat_cols].describe()
described_stats.to_csv('described_stats.csv')


# Number of pokemon by type
print("Number of pokemon by type")
print(melted['Type'].value_counts())
print("\n")

# Number of pokemon by body style
print("Number of pokemon by body style")
print(pokemon_df['Body_Style'].value_counts())






# Print
print("\nGraphing\n")

types = set(melted["Type"])
for type in types:
	specific_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def','Speed']
	stats = melted[specific_cols][melted['Type']==type].mean()

	objects = ('HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def','Speed') # TODO find a way to convert this without retyping
	y_pos = np.arange(len(objects))

	plt.bar(y_pos, stats, align='center', alpha=0.5)
	plt.xticks(y_pos, stat_cols)
	plt.ylabel('Base')
	title = type + ' stats'
	plt.title(title)
	 
	plt.show()