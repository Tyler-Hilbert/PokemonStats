import pandas as pd
import pylab

pokemon_df = pd.read_csv("pokemon.csv")

print(pokemon_df['Type_1'].value_counts() + pokemon_df['Type_2'].value_counts())

stats = pokemon_df.groupby('Type_1').mean() + pokemon_df.groupby('Type_2').mean()

print(stats)

# Todo - get these plots to work ##
#print (stats.hist(bins=15))
#pylab.show()
