import json

def load_json(path):
    try:
        with open(path,"r") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return []

def update_json(path,data):
    try:
        with open(path,"w") as file:
            json.dump(data,file,indent=2)
            return True
    except Exception as e:
        return False