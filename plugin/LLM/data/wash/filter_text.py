import json

input_path="./bianmu.json"
out_path="../train_data.txt"


with open(input_path,"r",encoding="utf-8") as fopen:
    data=json.load(fopen)

with open(out_path, 'w', encoding='utf-8') as f:
    for entry in data:
        for entity in entry.get('Entities', []):
            if 'Text' in entity:
                if str(entity['Text'])!="None" and str(entity['Text'])!=" ":
                    f.write(str(entity['Text']) + '\n')