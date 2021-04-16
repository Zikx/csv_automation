import os
import os.path
import csv
import pandas as pd

# input root_dir
root_dir = input('root_dir : ')

# csv_system_manu_id
csv_system_manu_id = pd.read_csv(f'{root_dir}_id.csv',
    names = ['systemId', 'manuId', 'systemName']
)

# create csv and row
f = open('write.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(["_manufacturerId", "occlusalDiameter", "apicalDiameter", "length", "stlFilePath", "_defaultAbutmentId", "_fixturesystemId", "fixtureName", "gingivaHeight"])

def search_id(val):
    row_idx = int(csv_system_manu_id.index[csv_system_manu_id["systemName"] == val].tolist()[0])

    system_id = csv_system_manu_id.iloc[row_idx][0]
    manufact_id = csv_system_manu_id.iloc[row_idx][1]    

    return system_id, manufact_id


# export dir  
for dir_path, dirs, files in os.walk(root_dir):
    print(f'path : {dir_path}')
    system_name = dir_path[len(root_dir) + 1:]
    for file_name in files:
        file_code = file_name[:-3]
        file_path = dir_path + '\\' + file_code
        
        system_id, manufact_id = search_id(system_name)

        wr.writerow([manufact_id, '','','',file_path, '',system_id, file_code, 0.0])

        print(f'## file : {file_path} ')

f.close()


