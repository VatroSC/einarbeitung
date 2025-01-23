import json
import yaml

with open("/root/einarbeitung/base.json", "r") as file:
    source_data = json.load(file)

with open("/root/einarbeitung/03_Dateiformate/data.yaml", "w") as yaml_file:
    yaml.dump(source_data, yaml_file)

'''
with open("/root/einarbeitung/03_Dateiformate/data.yaml", "r") as yaml_file:
    print(yaml_file.read)
'''
