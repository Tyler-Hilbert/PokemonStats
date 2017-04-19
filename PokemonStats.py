import pandas as pd

pokemon_df = pd.read_csv("pokemon.csv")

# Break pokemon of 2 types into 2 entries
stat_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def','Speed', 'Catch_Rate', 'Body_Style']
type_cols = ['Type_1', 'Type_2']
melted = pd.melt(pokemon_df, stat_cols, type_cols, value_name='Type')

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



# Find highest HP
#types = set(melted["Type"])
#for type_ in types:
#	print(melted["HP"][melted["Type"]==type])
#	print(melted["HP"][melted["Type"]==type].mean())
