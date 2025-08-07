def load_data(file):
    if not os.path.exists(file):
        with open(file , "w") as f1:
            json.dump([],f1)
    with open(file,"r") as f2:
        return json.load(f2)

def save_data(file,data):
    with open(file ,"w") as f:
        json.dump(data,f,indent=4)
        
def checkuserid(id,file):
    data = load_data(file)
    for account in data:
        if account["id"] == id:
            return True
    return False