import os
import os.path
import csv

# ["_manufacturerId", "occlusalDiameter", "apicalDiameter", "length", "stlFilePath", "_defaultAbutmentId", "_fixturesystemId", "fixtureName", "gingivaHeight"]
# 9 개 행
root_dir = input('root_dir : ')

from_mongo_id = root_dir + '_id'

for dir_path, dirs, files in os.walk(root_dir):
    print(f'path : {path}')
    for file_name in files:
        file_code = file_name[:-3]
        file_path = path + '\\' + file_code
        print(f'## file : {file_path} ')

# for fdr in file_list :
    # file_sa = []
    # file_sa.append(fdr)
    # print(type(fdr))
 
    # file_save.append(file_sa)
 
# with open('export.csv','w+',encoding='euc-kr',newline='') as f :
#     writer = csv.writer(f)
#     writer.writerows(file_save)  