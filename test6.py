import json

malformed_list = []

with open('C:/Users/vasan/Desktop/test_2.json', 'w') as f:
    for line in f:
        try:
                data = json.loads(line)
                json.dump(data,f)
        except ValueError:
                malformed_list.append(line)
                #print('Could not parse line:', line)
    