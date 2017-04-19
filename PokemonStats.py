import pandas as pd
import pylab as plt

pokemon_df = pd.read_csv("pokemon.csv")




stat_cols = ['HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed', 'Catch_Rate']
type_cols = ['Type_1', 'Type_2']
melted = pd.melt(pokemon_df, stat_cols, type_cols, value_name='Type');
print(melted.groupby('Type')[stat_cols].mean())

# TODO ---- figure out how to loop through the different stats here---------------------------------------
#for key, grp in melted.groupby('Type')[stat_cols].mean():
#    plt.plot(grp['B'], label=key)
#    grp['D'] = pd.rolling_mean(grp['B'], window=5)    
#    plt.plot(grp['D'], label='rolling ({k})'.format(k=key))
#plt.legend(loc='best')    
#plt.show()

#print(melted.groupby('Type')[stat_cols].describe())
#melted.groupby('Type')[stat_cols].describe().to_csv('described_stats.csv')

#plt.imshow(melted,aspect="auto")
#plt.show()







# TOdo - there is a problem when only one of the types exists... I get NAN if I don't have a type1 or type 2 of any of the values
#print(pokemon_df['Type_1'].value_counts() + pokemon_df['Type_2'].value_counts())


#stats = pokemon_df.groupby('Type_1').mean() + pokemon_df.groupby('Type_2').mean()

#stats.to_csv('Type_Stats.csv')

#type1 = pokemon_df.groupby('Type_1');
#type1.apply().to_csv('type1.csv');


# Todo - figure out how to get just specific stats
#print(stats['Total', 'HP'])
#importantStats = stats.DataFrame(index='number', columns=['Total', 'HP'])

# Todo - get these plots to work ##
#print (stats.hist(bins=15))
#pylab.show()
