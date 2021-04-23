import os
import os.path
import csv
import pandas as pd


# define Function 

def search_id(val):
    row_idx = int(csv_system_manu_id.index[csv_system_manu_id["systemName"] == val].tolist()[0])

    system_id = csv_system_manu_id.iloc[row_idx][0]
    manufact_id = csv_system_manu_id.iloc[row_idx][1]    

    return system_id, manufact_id

def search_OAL(file_code, system_name):
    row_idx = int(csv_OAL.index[(csv_OAL["Code"] == file_code) & (csv_OAL["System"] == system_name)].tolist()[0])
    print(f'row_idx : {row_idx}')

    occlusal = csv_OAL.iloc[row_idx][3]
    apical = csv_OAL.iloc[row_idx][4]    
    length = csv_OAL.iloc[row_idx][5]    

    return occlusal, apical, length

def import_fixture_system(root_dir):
    f = open(f'toMongoDB_{root_dir}.csv','w', newline='')
    wr = csv.writer(f)
    wr.writerow(["_manufacturerId", "systemName"])
    
    manufact_id = input('manufacturer Id : ')
    system_name = os.listdir(root_dir)
    
    for systemName in system_name:
        wr.writerow([manufact_id, systemName])
    f.close()



# input root_dir
root_dir = input('root_dir : ')

import_fixture_system(root_dir)

input('await system_id.csv')

# csv_system_manu_id
csv_system_manu_id = pd.read_csv(f'{root_dir}_id.csv',
    names = ['systemId', 'manuId', 'systemName']
)

# csv_OAL
csv_OAL = pd.read_csv(f'{root_dir}_cp.csv',
    names = ['Manufacturer', 'System', 'Code', 'Occlusal', 'Apical', 'Length', 'Orientation','FMF path']
)


# create csv and row for export 
f = open(f'importData_{root_dir}.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(["_manufacturerId", "occlusalDiameter", "apicalDiameter", "length", "stlFilePath", "_defaultAbutmentId", "_fixturesystemId", "fixtureName", "gingivaHeight"])

# export dir  

for dir_path, dirs, files in os.walk(root_dir):
    print(f'path : {dir_path}')
    system_name = dir_path[len(root_dir) + 1:]
    for file_name in files:
        if not file_name.endswith('.om'):
            continue

        file_code = file_name[:-3]
        file_path = dir_path + '\\' + file_code

        system_id, manufact_id = search_id(system_name)
        occlusal, apical, length = search_OAL(file_code, system_name)
        print(f'system name : {system_name}')
        wr.writerow([manufact_id, occlusal, apical, length, file_path, '',system_id, file_code, 0.0])

        print(f'## file : {file_path} ')

f.close()
