import csv 
import pandas as pd

csv_df = pd.read_csv('test_id.csv',
    names = ['systemId', 'manuId', 'systemName']
)

sysName = '5.0 External HA'

# systemName 을 참조하여 해당 열의 번호를 찾음
row_idx_for_systemId = int(csv_df.index[csv_df['systemName'] == sysName].tolist()[0])
# system_id = csv_df.iloc[systemId_row_idx][0]

print(csv_df.iloc[row_idx_for_systemId][0])