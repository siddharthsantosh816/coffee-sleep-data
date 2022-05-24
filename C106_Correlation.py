import csv
import pandas as pd
import plotly.express as px
import numpy as np

def getDataSource(path):
    coffee=[]
    sleep=[]
    with open(path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for data in csv_reader:
            print(data)
            coffee.append(float(data['Coffee in ml']))
            print(coffee)
            sleep.append(float(data['sleep in hours']))
            print(sleep)
        return{'x':coffee,'y':sleep}

def findcorrelation(dataSource):
    correlation=np.corrcoef(x=dataSource['x'],y=dataSource['y'])
    print(correlation[0][1])

def plotFigure(path):
    df =pd.read_csv(path)
    scatterG=px.scatter(df,x='Coffee in ml',y='sleep in hours')
    scatterG.show()

def setup():
    data_path='C:/Users/w/Desktop/Python/csv/P106_Coffee_vs_SleepHrs.csv'
    data=getDataSource(data_path)
    findcorrelation(data)
    plotFigure(data_path)

setup()

    

