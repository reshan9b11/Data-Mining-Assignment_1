# This is a sample Python script.
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

#Opening Json Data
#filterStatusConfirmed=0
#filterStatusRecovered=0
#filterStatusDeceased=0
confirmed_count = 0
recovered_count = 0
deceased_count = 0
def dataPre(json_file_path,start_date,end_date):
    with open(json_file_path) as f:
        states_daily = json.load(f)

    # Preparing Data Frame
    
    print(states_daily['states_daily'][0].keys())
    # Getting Columns
    columnNames = list(states_daily['states_daily'][0].keys())
    print(columnNames)
    len(states_daily['states_daily'])
    # Getting Each Instanes
    rows = [list(states_daily['states_daily'][i].values()) for i in range(len(states_daily['states_daily']))]
    rowsArray = np.array(rows)
    dataframe = pd.DataFrame(data=rowsArray, columns=columnNames)
    dataframe.head(5)


    # Preprocessing of Data
    arr = columnNames[0:]
    arr.remove('date')
    arr.remove('status')
    for item in arr:
        dataframe[item] = dataframe[item].astype(int)

    dataframe['date'] = pd.to_datetime(dataframe['date'])
    filterStatusConfirmed = dataframe.loc[dataframe['status'] == 'Confirmed']
    filterStatusRecovered = dataframe.loc[dataframe['status'] == 'Recovered']
    filterStatusDeceased = dataframe.loc[dataframe['status'] == 'Deceased']
    union_terr = ['dl', 'an', 'jk', 'la', 'dn', 'py', 'cg', 'ld', ]
    state = []
    for item in arr:
        if item in union_terr or item == 'un' or item == 'dd' or item == 'tt':
            continue
        state.append(item)
    print(state)
    print(arr)
    #print(dataframe.head())
    return dataframe,filterStatusConfirmed,filterStatusRecovered,filterStatusDeceased
    # filterStatusDeceased.head(5)

def Q1_1(json_file_path, start_date, end_date):
        dataframe ,filterStatusConfirmed,filterStatusRecovered,filterStatusDeceased = dataPre(json_file_path,start_date,end_date)
        #print(dataframe.head())
        print(filterStatusConfirmed.head())
      # Answer1_1  (If we get date from user and pass that date while comparing it is genralized)
        marchToSept1_Confirmed = filterStatusConfirmed[(filterStatusConfirmed['date'] >= '2020-03-14') & (filterStatusConfirmed['date'] <= '2020-09-05')]
        marchToSept1_Recovered = filterStatusRecovered[(filterStatusRecovered['date'] >= '2020-03-14') & (filterStatusRecovered['date'] <= '2020-09-05')]
        marchToSept1_Deceased = filterStatusDeceased[(filterStatusDeceased['date'] >= '2020-03-14') & (filterStatusDeceased['date'] <= '2020-09-05')]
        print("Confirmed:{0} \nRecovered : {1}\nDeceased : {2}".format(marchToSept1_Confirmed['tt'].sum(),
                                                                       marchToSept1_Recovered['tt'].sum(),
                                                                       marchToSept1_Deceased['tt'].sum()))
        print("Confirmed:{0} \nRecovered : {1}\nDeceased : {2}".format(marchToSept1_Confirmed['tt'].sum() , marchToSept1_Recovered['tt'].sum() , marchToSept1_Deceased['tt'].sum() ))
        return confirmed_count, recovered_count, deceased_count

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    if(len(sys.argv)==4):
        start_date=""
        end_date=""
        json_file_path=""
        json_file_path = sys.argv[1]
        if os.path.exists(json_file_path):
            start_date = sys.argv[2]
            end_date = sys.argv[3]
            
        else:
            print("File path not exit")
    else:
        print("YOu forgot the Argument")
    
  #  dataPre(json_file_path,start_date ,end_date)
    Q1_1(json_file_path, start_date, end_date)
#print(json_file_path)
#print(start_date)
#print(end_date)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
