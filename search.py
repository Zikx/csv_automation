import csv 
import pandas as pd
import sys

csv_df_id = pd.read_csv('test_id.csv',
    names = ['systemId', 'manuId', 'systemName']
)

def search_val(col, val):
    row_idx = int(csv_df_id.index[csv_df_id[col] == val].tolist()[0])

    system_id = csv_df_id.iloc[row_idx][0]
    manufact_id = csv_df_id.iloc[row_idx][1]    

    return system_id, manufact_id

print(search_val("systemName", "3.0 OnePiece HA"))


# sysName = input()



# systemName 을 참조하여 해당 열의 번호를 찾음
# row_idx_for_systemId = int(csv_df_id.index[csv_df_id['systemName'] == sysName].tolist()[0])

# system_id = csv_df_id.iloc[row_idx_for_systemId][0]
# manufact_id = csv_df_id.iloc[row_idx_for_systemId][1]