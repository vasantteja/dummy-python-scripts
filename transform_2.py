import pandas as pd
from extract import Extract
from pandas.io.json import json_normalize

class Player_Death_Transform:

      

    def classify(self, df):
        new_temp_df = df.dmg_table.apply(pd.Series) \
        .merge(df, right_index = True, left_index = True) \
        .drop(["dmg_table"], axis = 1) \
        .melt(id_vars = ['event_type','userId', 'time','killer'], value_name = "dmg_table") \
        .drop("variable", axis = 1) \
        .dropna()

        return new_temp_df
    
    def flattened_df_method(self, temp_df):
        #flattened_df = pd.concat([temp_df.drop(['dmg_table'], axis=1), temp_df['dmg_table'].apply(pd.Series)], axis=1)
        flattened_df = temp_df.join(pd.DataFrame(temp_df.pop('dmg_table').tolist()))
        #flattened_df = pd.concat([temp_df.drop('dmg_table', axis=1), pd.DataFrame(temp_df['dmg_table'].tolist())], axis=1)
        return flattened_df

c1 = Extract()

# Call getData() function
# Output: 2+3j
df1, malinformed_events, error_events = c1.Load('C:/Users/vasan/Desktop/test_3.json')
#df1.drop('meta', axis=1, inplace=True)

# Create another ComplexNumber object
# and create a new attribute 'attr'
#c2 = ComplexNumber(5)
#c2.attr = 10

# Output: (5, 0, 10)
#print(df1)
#c2 = Player_Death_Transform()

#player_death_df = df1[df1.event_type == "player_death"]
#print(player_death_df)
#game_econ_df1 = df1[df1.event_type == "game_econ"]
#game_econ_df2 = game_econ_df1.drop(['dmg_table', 'gold_earned','item_id','killer','meta'], axis = 1)
#print(game_econ_df2)
#login_df1 = df1[df1.event_type == "login"]
#login_df2 = login_df1.drop(['dmg_table', 'gold_earned','gold_spent','item_id','item_sku','killer','meta'], axis = 1)
#print(login_df2)
#pickup_items_df1 = df1[df1.event_type == "pickup_items"]
#pickup_items_df2 = pickup_items_df1.drop(['dmg_table','gold_spent','killer','meta'], axis = 1)
#print(pickup_items_df2)

#bool_series = pd.notnull(player_death_df["dmg_table"])
#temp_df = player_death_df[bool_series] 

#broken_df = c2.classify(temp_df)
#flatter_df = c2.flattened_df_method(broken_df)
#flatter_df = flatter_df.dropna(subset=['dmg','npc']) 
#flatter_df = flatter_df.dropna()


#print(flatter_df)
#lyca = list(df1.columns.values)
#print(flatter_df)

#login_not_ot_df = df1.query('event_type == "login" & event_type != "player_death" & event_type != "game_econ" & event_type != "pickup_items"')
#print(login_not_ot_df)
#export_csv_df = df1.to_csv (r'source_of_truth_1.csv', index = None, header=True)
#export_csv_player_deaths = flatter_df.to_csv (r'player_deaths_3.csv', index = None, header=True)
#export_csv_login = login_df2.to_csv (r'login_3.csv', index = None, header=True)
#export_csv_game_econ = game_econ_df2.to_csv (r'game_econ_3.csv', index = None, header=True)
#export_csv_pickup_items = pickup_items_df2.to_csv (r'pickup_items_3.csv', index = None, header=True)

#cnt_mal = len(malinformed_events)
#cnt_error = len(error_events)

with open('malformed_3.txt', 'w') as f:
    for item in malinformed_events:
        f.write("%s\n" % item)

with open('error_3.txt', 'w') as f:
    for item in error_events:
        f.write("%s\n" % item)

#print(cnt_mal)
#print(cnt_error)


