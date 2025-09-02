import json


def save_json_file(save_location, data):
    
    with open(save_location, "w", encoding="utf-8") as file:
        json.dump(data,file, indent=2)
        
        
def load_json_file(save_location):
    
    with open(save_location, "r") as file:
        return json.load(file)
    
    
    
    