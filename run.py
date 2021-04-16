import os
import os.path
import csv

# input root_dir
root_dir = input('root_dir : ')
from_mongo_id = root_dir + '_id'

# create csv and row
f = open('write.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(["_manufacturerId", "occlusalDiameter", "apicalDiameter", "length", "stlFilePath", "_defaultAbutmentId", "_fixturesystemId", "fixtureName", "gingivaHeight"])

# export dir  
for dir_path, dirs, files in os.walk(root_dir):
    print(f'path : {dir_path}')
    system_name = dir_path[len(root_dir) + 1:]
    for file_name in files:
        file_code = file_name[:-3]
        file_path = dir_path + '\\' + file_code
        wr.writerow([root_dir, '','','',file_path, '',system_name, file_code, 0.0])

        print(f'## file : {file_path} ')



f.close()