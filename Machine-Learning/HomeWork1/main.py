import os

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def SetupData():
    global train_df, test_df, combine

    basePath = os.getcwd().__str__()

    if basePath.__contains__(r'\Machine-Learning\HomeWork1'):
        pass
    else:
        basePath = basePath + r'\Machine-Learning\HomeWork1'

    baseDataPath = basePath + r'\input'
    trainPath = baseDataPath + r'\train.csv'
    testPath = baseDataPath + r'\test.csv'

    train_df = pd.read_csv(trainPath)
    test_df = pd.read_csv(testPath)
    combine = [train_df, test_df]

def ShowDataStats():
    print()
    print(train_df.info())
    print()

def DescribeData():
    print()
    print(train_df.describe())
    print()

def FindSurvivors(data, columnName, sortValue):
    totalCount = len(data["Survived"])
    survivorCount = len(data.loc[data["Survived"] == 1])

    print("------------ " + str(columnName) + " " + str(sortValue) + " ------------")
    print("Survival Rate - {:.2f}%".format((survivorCount / totalCount) * 100))
    print()

def GroupData(columnName, sortValue):
    initialGroup = train_df.loc[train_df[columnName] == sortValue]

    FindSurvivors(initialGroup, columnName, sortValue)

def DisplayValueCounts():
    for column in train_df:
        print()
        print("------------ " + column + " Count ------------")
        print(train_df[column].count())
        print()

def DisplayUniqueValues():
    for column in train_df:
        print()
        print("------------ " + column + " Unique Count ------------")
        print(train_df[column].unique())
        print()

def DisplayFrequentValues():
    for column in train_df:
        print()
        print("------------ " + column + " Freq Count ------------")
        print(train_df[column].value_counts())
        print()

def Main():
    SetupData()

    #shows count and datatype
    #ShowDataStats()

    #shows high level calculations mean, std, etc
    #DescribeData()

    #Group data for further analysis
    #Used for comparing the survival rate based on Pclass
    # print()
    # GroupData('Pclass', 1)
    # GroupData('Pclass', 2)
    # GroupData('Pclass', 3)
    #Used for comparing the survival rate based on sex
    # print()
    # GroupData('Sex', "female")
    # GroupData('Sex', "male")

    #This is to handle those points of freq, count, unique values
    #DisplayValueCounts()
    #DisplayUniqueValues()
    #DisplayFrequentValues()

    x = [1,2,3]
    y = [2,4,6]

    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    Main()
