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

def GraphingDataSetupForAge(x1, y1, x2, y2, x3, y3, x4, y4, groupOne, groupTwo, columnName):
    for i in range(90):
        x1.append(i)
        y1.append(len(groupOne.loc[groupOne[columnName] == i]))
        x2.append(i)
        y2.append(len(groupTwo.loc[groupTwo[columnName] == i]))
        x3.append(i)
        y3.append(len(groupOne.loc[groupOne[columnName] == i]))
        x4.append(i)
        y4.append(len(groupTwo.loc[groupTwo[columnName] == i]))

def AddGraph(graphData, col, row, width, x, y, label, title):
    if len(graphData) <= 1:
        graphData[col].bar(x, y, width=width)
        graphData[col].set_xlabel(label)
        graphData[col].set_title(title)
    else:
        graphData[col,row].bar(x, y, width=width)
        graphData[col,row].set_xlabel(label)
        graphData[col,row].set_title(title)

def CreateGraph(rows, cols, w, h, mainLabel, columnName, compareVals):
    nonSurvivors = train_df.loc[train_df[columnName] == compareVals[0]]
    survivors = train_df.loc[train_df[columnName] == compareVals[1]]

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    x4 = []
    y4 = []

    GraphingDataSetupForAge(x1, y1, x2, y2, x3, y3, x4, y4, nonSurvivors, survivors, mainLabel)

    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(w, h))

    # for y in range(rows):
    #     for x in range(cols):
    #         if rows == 2:
    #             if y % 2 == 0:
    #                 AddGraph(axes, y, x, 1.0, x1, y1, mainLabel, str(columnName) + ' = ' + str(compareVals[0]))
    #             else:
    #                 AddGraph(axes, y, x, 1.0, x1, y1, mainLabel, str(columnName) + ' = ' + str(compareVals[1]))

    AddGraph(axes, 0, 0, 1.0, x1, y1, mainLabel, str(columnName) + ' = ' + str(compareVals[0]))
    AddGraph(axes, 0, 1, 1.0, x2, y2, mainLabel, str(columnName) + ' = ' + str(compareVals[1]))
    AddGraph(axes, 1, 0, 1.0, x3, y3, mainLabel, str(columnName) + ' = ' + str(compareVals[0]))
    AddGraph(axes, 1, 1, 1.0, x4, y4, mainLabel, str(columnName) + ' = ' + str(compareVals[1]))

    fig.tight_layout()

def ShowCurrentGraph():
    plt.show()

def ChangeData(columnName, oldValue, newValue):
    train_df.loc[train_df[columnName] == oldValue, columnName] = newValue

def ChangeColumnName(oldColName, newColName):
    train_df.rename(columns = {oldColName : newColName}, inplace = True)

def FillInNullOrMissingData(columnName):
    if columnName == 'Fare':
        train_df[columnName].fillna(train_df[columnName].mode(), inplace=True)
    elif columnName == 'Embarked':
        train_df[columnName].fillna(train_df[columnName].mode(), inplace=True)
    else:
        train_df[columnName].fillna(train_df[columnName].mean(), inplace=True)

def Main():
    SetupData()

    ######## shows count and datatype
    # ShowDataStats()

    ######## shows high level calculations mean, std, etc
    # DescribeData()

    ######## Group data for further analysis
    ######## Used for comparing the survival rate based on Pclass
    # print()
    # GroupData('Pclass', 1)
    # GroupData('Pclass', 2)
    # GroupData('Pclass', 3)
    ######## Used for comparing the survival rate based on sex
    # print()
    # GroupData('Sex', "female")
    # GroupData('Sex', "male")

    ######## This is to handle those points of freq, count, unique values
    # DisplayValueCounts()
    # DisplayUniqueValues()
    # DisplayFrequentValues()

    ######## creating and displaying bar graphs
    # CreateGraph(2, 2, 6, 4, 'Age', 'Survived', [0, 1])
    # ShowCurrentGraph()

    ######## Changing data
    # ChangeData('Sex', 'female', 1)
    # ChangeData('Sex', 'male', 0)
    # ChangeColumnName('Sex', 'Gender')

    # print()
    # print(train_df.head(5))
    # print()

    ######## Filling in null values
    # FillInNullOrMissingData('Age')

    # print()
    # print(train_df['Age'])
    # print()

    # FillInNullOrMissingData('Embarked')

    # print()
    # print(train_df.loc[train_df['PassengerId'] == 62])
    # print()

    # FillInNullOrMissingData('Fare')

    # print()
    # print(train_df.info())
    # print()

if __name__ == "__main__":
    Main()