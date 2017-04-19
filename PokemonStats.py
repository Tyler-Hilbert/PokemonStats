import pandas as pd

pokemon_df = pd.read_csv("pokemon.csv")

stat_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def','Speed', 'Catch_Rate']
type_cols = ['Type_1', 'Type_2']
melted = pd.melt(pokemon_df, stat_cols, type_cols, value_name='Type')


described_stats = melted.groupby('Type')[stat_cols].describe()
described_stats.to_csv('described_stats.csv')