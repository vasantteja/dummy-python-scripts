import json
import csv
import pandas as pd
from pandas import DataFrame
import collections

FIELD_ORDER = ['event_type', 'userId', 'time','killer','dmg_table','item_sku', 'gold_spent','gold_earned', 'item_id','meta']


malformed_list = []
clean_dicts = []
#clean_dicts = collections.defaultdict(list)
with open('C:/Users/vasan/Desktop/test_2.json', 'r') as f:
    for line in f:
        try:
            d = json.loads(line)
            if isinstance(d, dict):
                clean_dicts.append(d)
            else:
                malformed_list.append(d)
        except ValueError:
            malformed_list.append(line)
            #print('Could not parse line:', line)

"""
for item in clean_dicts:
    if type(item) == int:
        print(type(item))
"""

#df = pd.DataFrame(clean_dicts)
#df['event_type'] = df['event_type'].str.lower()
#print(df.shape)
#print (df)
"""
clean_dicts2 = []
malformed_list2 = []
for element in clean_dicts:
    if len(element) > 10:
        try:
            clean_dicts2.append(element)
        except TypeError:
            malformed_list2.append(element)

"""

   

#df = pd.DataFrame(clean_dicts2)
        

"""
new_dict = {}
for item in clean_dicts:
   event_type = item['event_type']
   new_dict[event_type] = item


print(new_dict)
"""

"""
swap = []
print(clean_dicts)
result = filter(lambda x: x.startswith('{'), clean_dicts)
for i in result:
    swap.append(i)

print(swap)
#print(clean_dicts[1])
#df  = json.dumps(clean_dicts)
"""

#data_transposed = zip(clean_dicts)

#clean_list2 = []
#error_list_2 = []
"""
for word in clean_dicts:
    if word[0] == "{":
        clean_list2.append(word)
    elif word[0] != "{":
        error_list_2.append(word)

df = pd.DataFrame(clean_list2)

print(df)
#df = pd.io.json.json_normalize(clean_dicts, record_path='dmg_table')
"""

#path = 'C:/Users/vasan/Desktop/data.json'

#data = pd.read_json('C:/Users/vasan/Desktop/data.json', lines=True)

#df = pd.read_json(path, orient='columns')

#df = pd.read_json(clean_dicts)

# View the first ten rows
#df.head(10)

#DataFrame.from_records(clean_dicts)

#df = pd.DataFrame(clean_dicts)
#print(df)



#bool_series_meta = pd.notnull(df["meta"])
#df = df[bool_series_meta]
#player_death_df = df[df.event_type == "player_death"]
#print(player_death_df)
#game_econ_df = df[df.event_type == "game_econ"]
#print(game_econ_df)
#login_df = df[df.event_type == "login"]
#print(login_df)
#pickup_items_df = df[df.event_type == "pickup_items"]
#print(pickup_items_df)

#print(player_death_df)
#print(game_econ_df)
#print(login_df)
#print(pickup_items_df)


#bool_series = pd.notnull(player_death_df["dmg_table"])
#temp_df = player_death_df[bool_series] 




"""
s = temp_df.apply(lambda x: pd.Series(x['dmg_table']), axis=1).stack().reset_index(level=1, drop=True)
s.name = 'dmg_table'
df2 = temp_df.drop('dmg_table', axis=1).join(temp_df)
df2['dmg_table'] = pd.Series(df2['dmg_table'], dtype=object)
df2
"""

#print(new_temp_df)
#print(df2)
"""
#new_df = new_temp_df.dropna(subset = ['dmg_table'])
#print(new_df)
#bool_series_new = pd.notnull(new_temp_df["dmg_table"])
#temp_df = new_temp_df[bool_series_new]
new_temp_df = temp_df.dmg_table.apply(pd.Series) \
    .merge(temp_df, right_index = True, left_index = True) \
    .drop(["dmg_table"], axis = 1) \
    .melt(id_vars = ['event_type','userId', 'time','killer','meta'], value_name = "dmg_table") \
    .drop("variable", axis = 1) \
    .dropna()
new_temp_df = new_temp_df[pd.notnull(new_temp_df['dmg_table'])]
flattened_df = pd.concat([new_temp_df.drop(['dmg_table'], axis=1), new_temp_df['dmg_table'].apply(pd.Series)], axis=1)
#flattened_df = pd.concat([new_temp_df.drop('dmg_table', axis=1), pd.DataFrame(new_temp_df['dmg_table'].tolist())], axis=1)
print(flattened_df)
"""




#final_json_list = []
#for i in clean_dicts:
#    final_json_list.append(i.strip())

#print(clean_dicts)
#print(final_json_list)


#with open('myfile.csv', 'w') as o:
#    w = csv.DictWriter(o, fieldnames=FIELD_ORDER)
#    w.writeheader()
#    for d in clean_dicts:
#        w.writerow(d)


#print(malformed_list)

#with open('data.json', 'w') as outfile:
#    json.dump(clean_dicts, outfile)


malformed_list2 = []
error_list = []

for word in malformed_list:
    if isinstance(word,int) or isinstance(word,float):
        error_list.append(word)
    else:
        malformed_list2.append(word)

malformed_list_final = []
error_list_final = []

for word in malformed_list2:
            if word[0] == '{':
                malformed_list_final.append(word)
            else:
                error_list_final.append(word)
    

#m = []

#m = map(lambda clean_dicts: malformed_list2.strip(), m)

#n = []

#n = list(map(lambda clean_dicts: error_list.strip(), n))

#list(map(str.strip,error_list))

"""
final_malformed_list = []
for i in malformed_list2:
    final_malformed_list.append(i.strip())

final_error_list = []
for i in error_list:
    final_error_list.append(i.strip())
"""


#print(n)
#print(malformed_list2)
#print(final_malformed_list)
print(error_list_final)
#print(final_error_list)