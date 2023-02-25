import pandas as pd
import json

def load_and_read_json(file_path_json):
    with open(file_path_json, 'r') as f:
        data = json.load(f)
    return data

def Ransomware_Detection_Based_File_Family(file_path,file_hash):
    df = pd.read_csv(r"C:\Users\cherif\Documents\data_sets.csv")
    result = df[df["MD5"] == file_hash ]
    if len(result) == 0 :
        return False
    else:
        return True

if __name__ == '__main__':
    dic=load_and_read_json(r"C:\Users\cherif\Documents\data_file_2023-02-19.json")
    for i in dic:
        print(Ransomware_Detection_Based_File_Family(r"C:\Users\cherif\Documents\pestudio.exe",dic[i]['md5Hash']))
