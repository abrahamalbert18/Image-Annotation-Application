# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:25:07 2018

@author: Albert
"""
import pandas as pd
import numpy as np

df = pd.read_csv("./PreprocessedDataFiles/MergedPreprocessedDataFiles/MergedPreprocessedDrinkingDataLabels v2.csv")
# originalDF = df
df['index'] = range(0, len(df))

splitRatio = [0.6,0.2,0.2]

def indicesSplit(splitRatio):
    train = df.sample(frac = splitRatio[0], random_state = 42)
    val = df.drop(train.index).sample(frac = 0.5, random_state = 42)
    test = df.drop(train.index.append(val.index))#.sample(frac = splitRatio[2])
    
    return train, val, test

if __name__=="__main__":
    train, val, test = indicesSplit(splitRatio)
    np.savez("./Splits/indicesSplits.npz", train = train, val = val, test = test)    
