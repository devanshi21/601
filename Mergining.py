import pandas as pd
df_Airbnb = pd.read_csv('Air Bnb_NYC_2019.csv')
df_crime = pd.read_csv('NYC_crime.csv')

df1 = pd.DataFrame(df_Airbnb,columns=['latitude','longitude'])
df2 = pd.DataFrame(df_crime,columns=['latitude','longitude'])


intersected_df = pd.merge(df2, df1, how='inner')
#intersected_df = pd.merge(df1, df2.drop_duplicates(), how='inner')

#intersected_df = pd.concat([df1, df2],axis=0,sort=True)
#intersected_df.dropna(inplace=True)

#for lati common 
lati_air= []
lati_air= df_Airbnb['latitude'].round(5)
lati_crime= []
lati_crime= df_crime['latitude'].round(5)

final_lati = []
final_lati = list(set(lati_air) & set(lati_crime))
len(final_lati) #17470

#for longi common
long_air= []
long_air= df_Airbnb['longitude'].round(5)
long_crime= []
long_crime= df_crime['longitude'].round(5)

final_long = []
final_long = list(set(long_air) & set(long_crime))
len(final_long) #13751

print(final_long)

## Working


>>> df_Airbnb['latitude']= df_Airbnb['latitude'].round(5)
>>> df_Airbnb['longitude']= df_Airbnb['longitude'].round(5)
>>> df_crime['latitude']= df_crime['latitude'].round(5)
>>> df_crime['longitude']= df_crime['longitude'].round(5)
>>> intersected_df = pd.merge(df_Airbnb, df_crime, how='inner')
>>> intersected_df