import pandas as pd
import os 
from os import listdir
import json
from src.util.util import initCountyFolder


removeColConst = 'Unnamed: 0'

def checkSchema(dataSchema, standard):

    dataSchema.remove(removeColConst)

    if set(standard).issubset(set(dataSchema)) == False:
        print(list(set(standard) - set(dataSchema)))

    return set(standard).issubset(set(dataSchema))


with open("./config/schema.json", 'r', encoding="utf-8") as f:
    schema = json.load(f)

    BASE_PATH = "data/splitData"
    OUTPUT_PATH = "data/mergeData"
    initCountyFolder(OUTPUT_PATH, useCountyName=False)

    

    for county in listdir(BASE_PATH):
        for classes in ["land", "park", "build", "deal"]:
            class_folder_path = os.path.join(BASE_PATH, county, classes)
            
            total = []
            for i in listdir(class_folder_path):
                filePath = os.path.join(BASE_PATH, county, classes, i)
                data = pd.read_csv(filePath)
                if checkSchema(list(data.columns), schema[classes]):
                    total.append(data)

            if len(total) == 0:
                continue
            
            totalDf = pd.concat(total)
            totalDf.to_csv(os.path.join(OUTPUT_PATH, county, "{}.csv".format(classes)), encoding="utf-8-sig")