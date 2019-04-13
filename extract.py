import json
import pandas as pd

class Extract:
    
       

    def Load(self, path):
        url = path
        malformed_list = []
        clean_dicts = []
        #clean_dicts = collections.defaultdict(list)
        with open(url, 'r') as f:
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

        df = pd.DataFrame(clean_dicts)
        df['event_type'] = df['event_type'].str.lower()

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

        error_list_bokka = error_list_final + error_list

        error_df = df[(df.event_type != "login") & (df.event_type != "pickup_items") & (df.event_type != "game_econ" ) & (df.event_type != "dmg_table")]
        error_df_final = error_df.values.tolist()
        malformed_list_final_mat = malformed_list_final + error_df_final

        return df,malformed_list_final_mat,error_list_bokka


#c1 = Extract()


#df1, malkonda, errorkonda = c1.Load('C:/Users/vasan/Desktop/test_2.json')



# Output: (5, 0, 10)
#print(puspam.shape)

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
#c1.attr