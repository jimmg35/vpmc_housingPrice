
# 用於將實價登陸原始資料按照縣市與種類
# 解析成獨立csv檔

import pandas as pd
import os 
from os import listdir

total = 0
BASE_PATH = "data"
OUTPUT_PATH = "myadata"
for county in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 't', 'u', 'v', 'w', 'x', 'z']:
    for i in listdir("data"):
        countyMark = i[i.index("_")+1: i.index("_")+2]
        if county == countyMark:

            filePath = os.path.join(BASE_PATH, i)
            shtte_names = pd.ExcelFile(filePath).sheet_names

            for sheet in shtte_names:
                output_path = os.path.join(OUTPUT_PATH, county, '{}.csv'.format(sheet))
                data_xls = pd.read_excel(filePath, sheet, index_col=None)
                if os.path.exists(output_path):
                    total += 1
                    data_xls.to_csv(os.path.join(OUTPUT_PATH, county, '{}_{}.csv'.format(sheet,total)), encoding='utf-8-sig')
                    print('{}.csv'.format(total))
                else:
                    data_xls.to_csv(output_path, encoding='utf-8-sig')
                    print(output_path)




