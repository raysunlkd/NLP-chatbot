# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:59:17 2020

@author: 51722
"""
import pandas as pd
data=pd.read_csv('F:\\Courses\\HKUST_Semester_Spring\\MAFS6010U\\NLP_chatbot\\chatbot2\\dataset_preprocessed.csv')
data.columns=["patterns","responses","tag"]
def intents_aquire(data):
    tags=list(pd.DataFrame(data['tag']).drop_duplicates()['tag'])
    intents=[]
    for tag in tags:
        patterns=list(data.loc[data.tag==tag,"patterns"].drop_duplicates())
        print(len(patterns))
        for pattern in patterns:
            responses=list(data.loc[data.patterns==pattern,"responses"])
            temp={"tag":pattern,"patterns":pattern,"responses":responses}
            intents.append(temp)
    output={"intents":intents}
    return output
intents=intents_aquire(data)
import json
 
filename='intents.json'
with open(filename,'w') as file_obj:
    json.dump(intents,file_obj)