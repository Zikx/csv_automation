import os
import os.path
import subprocess


# input root_dir
root_dir = input('root_dir : ')
adr_list = root_dir.split('\\')
company_name = adr_list[4]

for dir_path, dirs, files in os.walk(root_dir):
    print(f'path : {dirs}')
    system_name = dir_path[len(root_dir) + 1:]
    # system_name = adr_list[5]
    
    for file_name in files:
        if not file_name.endswith('.stl'):
            continue

        file_path = dir_path + '\\' + file_name        
        # transform stl to om
        subprocess.run(['C:\OSSTEM\One3D\Bin-x64\clMeshDecimator.exe', f'C:\\Develop\\stl\\fixture\\{company_name}\\{system_name}\\{file_name}', f'C:\\Develop\\om\\fixture\\{company_name}\\{system_name}\\{file_name[:-3]}om', '0.0', '0'], shell=True, text=True )