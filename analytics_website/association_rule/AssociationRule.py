# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:16:32 2018

@author: aripiralas
"""

import pandas as pd
import glob
import os
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# set wd

FILE_PATH = 'S:/B&M/Analytics & Store Segmentation/Ad Hoc Analyses/Association Rule - 2017 Halloween/'

class AssociationRulesAlgo:
    
    def getARData(self):
        os.chdir(self.FILE_PATH)
# get all the .csv from wd
        allfiles = glob.glob("*.csv")
    # prepare empty data frame
        raw_data = pd.DataFrame()
    # read and merge all csv in a for loop
        raw_data = pd.concat((pd.read_csv(f, header=None) for f in allfiles))
# changing column names
        raw_data.columns = ['TransID', 'Quantity', 'ItemClass']
        raw_data = raw_data[~raw_data['ItemClass'].str.startswith("4-")]
        return raw_data

    def oneHotCoding(self, data):    
        df = data.groupby(['TransID', 'ItemClass'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('TransID')
        return df 
    
    def __init__(self,FILE_PATH,ROW_COUNT=100000,lift=1.1,support=0.01,confidence=0.25):
        self.FILE_PATH = FILE_PATH
        raw_data = self.getARData()
## Do one Hot coding 
        basket = self.oneHotCoding(raw_data.iloc[:ROW_COUNT,:])
## convert quantity to hot codes 1 or 0
        basket_set = basket.applymap(lambda x: 0 if x <= 0 else 1)
# generate frequent item sets
        frequent_itemset = apriori(basket_set, min_support=support, use_colnames=True)
        self.rules = association_rules(frequent_itemset, metric="lift")
        self.rules = self.rules[(self.rules.lift >= lift) & (self.rules.confidence >= confidence)]
    
    def getRules(self):
        return self.rules

