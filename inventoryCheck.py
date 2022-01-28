import pandas as pd
import csv
import codecs
import math
from module import zzModules

#difine import or export filename and path
importFilePath = r'inventoryCheck/import/'
importFileName = r'MB51_ALL.csv'
exportFilePath = r'inventoryCheck/export/'
exportFileName = r'MB51_ALL_result.csv'

def readFile():

    global df_inventory_in

    read_inventory = zzModules.readFileClass()
    read_inventory.setPara(importFilePath, importFileName)
    df_inventory_in = read_inventory.readFile()

    print("file read completed")

def editData():
    
    global df_inventory_exp
    df_inventory_exp = df_inventory_in[0:0]

# 品目を取得する。その際に重複削除も行う。
    df_material = df_inventory_in["品目"]
    df_material = df_material.drop_duplicates()
    df_material = df_material.reset_index()

# 以下、上記の品目の数だけloop処理を行う。
    for idx, ser in df_material.iterrows():
        
## 上記で取得した品目で改めてフィルターを行う。
        df_inventory_material =  df_inventory_in[df_inventory_in['品目'] == ser['品目']]
#移動タイプ101.261,543,687が発生していないものは        
#        if [101,261,543,687] in df_inventory_material['移動タイプ'] .values:
        if ['101'] in df_inventory_material['移動タイプ'] .values:
            if ['261'] in df_inventory_material['移動タイプ'] .values:
                pass
            elif ['687'] in df_inventory_material['移動タイプ'] .values:
                pass
            elif ['543'] in df_inventory_material['移動タイプ'] .values:
                pass
            else:
                df_inventory_exp = df_inventory_exp.append(ser)
                continue

    print("edit data completed")

def writeFile():
    write_inventory = zzModules.writeFileClass()
    write_inventory.setPara(exportFilePath, exportFileName, df_inventory_exp)
    write_inventory.writeFile()

    print("writeFile completed")

if __name__ == "__main__":

    readFile()

    editData()

    writeFile()

    print("process completed")