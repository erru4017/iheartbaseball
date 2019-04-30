#! /usr/bin/python

from pybaseball import statcast
from pybaseball import playerid_reverse_lookup
from pybaseball.lahman import *
from pybaseball.retrosheet import *
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
# %matplotlib inline


def readData_Erin():
    april2015 = pd.read_csv("../data/2015/dataApril2015.csv")
    may2015 = pd.read_csv("../data/2015/dataMay2015.csv")
    june2015 = pd.read_csv("../data/2015/dataJune2015.csv")
    july2015 = pd.read_csv("../data/2015/dataJuly2015.csv")
    aug2015 = pd.read_csv("../data/2015/dataAug2015.csv")
    sep2015 = pd.read_csv("../data/2015/dataSept2015.csv")
    oct2015 = pd.read_csv("../data/2015/dataOct2015.csv")
    df2015 = pd.concat([april2015,may2015,june2015,july2015,aug2015,sep2015,oct2015])
    
    df2016 = pd.read_csv("../data/2016/data2016.csv")
    
    april2017 = pd.read_csv("../data/2017/dataApril2017.csv")
    may2017 = pd.read_csv("../data/2017/dataMay2017.csv")
    june2017 = pd.read_csv("../data/2017/dataJune2017.csv")
    july2017 = pd.read_csv("../data/2017/dataJuly2017.csv")
    aug2017 = pd.read_csv("../data/2017/dataAug2017.csv")
    sep2017 = pd.read_csv("../data/2017/dataSept2017.csv")
    oct2017 = pd.read_csv("../data/2017/dataOct2017.csv")
    df2017 = pd.concat([april2017,may2017,june2017,july2017,aug2017,sep2017,oct2017])
    
    april2018 = pd.read_csv("../data/2018/dataApril2018.csv")
    may2018 = pd.read_csv("../data/2018/dataMay2018.csv")
    june2018 = pd.read_csv("../data/2018/dataJune2018.csv")
    july2018 = pd.read_csv("../data/2018/dataJuly2018.csv")
    aug2018 = pd.read_csv("../data/2018/dataAug2018.csv")
    sep2018 = pd.read_csv("../data/2018/dataSept2018.csv")
    oct2018 = pd.read_csv("../data/2018/dataOct2018.csv")
    df2018 = pd.concat([april2018,may2018,june2018,july2018,aug2018,sep2018,oct2018])
    
    df1518 = pd.concat([df2015, df2016, df2017, df2018])
    
    return df1518
    
def validStates(inning1, inning2, outs1, out2, topbot1, topbot2):
    if(inning1 < inning2): #cant go back an inning
        return False
    if ((topbot1 == topbot2) and (inning1 == inning2) ): #cant go down in outs, if in the same inning
        if(outs1 < outs2):
            return False
    if(topbot1 == 'Bot' and topbot2 =='Top'): #cant go from bot to top in the same inning
        if(inning1 >= inning2):
            return False
    else:
        return True
        
def readData_Court():
    df2015 = pd.read_csv("../data/2015/data2015.csv")
    df2016 = pd.read_csv("../data/2016/data2016.csv")
    df2017 = pd.read_csv("../data/2017/data2017.csv")
    df2018 = pd.read_csv("../data/2018/data2018.csv")
    
    df1518 = pd.concat([df2015, df2016, df2017, df2018])
    
    return df1518
    
    
def getState(df, inning, inning_topbot, on_1b, on_2b, on_3b, outs_when_up):
    if (df == 0):
        print("HELLO? you made it")
    if on_1b == 1:
        df_criteria = df.loc[df['on_1b'].notnull()]
    else:
        df_criteria = df.loc[df['on_1b'].isnull()]
    if on_2b == 1:
        df_criteria = df_criteria.loc[df['on_2b'].notnull()]
    else:
        df_criteria = df_criteria.loc[df['on_2b'].isnull()]
    if on_3b == 1:
        df_criteria = df_criteria.loc[df['on_3b'].notnull()]
    else:
        df_criteria = df_criteria.loc[df['on_3b'].isnull()]
        
    df_criteria = df_criteria.loc[(df['inning']==inning) & (df['inning_topbot']==inning_topbot)
                         & ((df['home_score'])-(df['away_score'])==-1)
                         & (df['outs_when_up']==outs_when_up)]
    return len(df_criteria.loc[df_criteria['W'] == True])/len(df_criteria)
    
    
def getRank(ranking, team):
    r = ranking.loc[ranking['Tm']==team]['Rk']
    return 0.1/r

def getWeight(probPrev, probCurrent, r):
    weight = (probCurrent/probPrev)
    if (weight>1):
        weight = (probCurrent/probPrev)/100
    else:
        weight = -1*(probCurrent/probPrev)/100

    return probCurrent + weight + r
    
    
def main():
    df1518 = readData_Erin()
    gameData = df1518.copy().groupby(['game_date', 'away_team', 'home_team']).max()[['away_score', 'home_score']].reset_index()
    gameData['W'] = gameData['home_score']>gameData['away_score']
    gameData.head()
    states = df1518.copy()
    df = states.merge(gameData[['game_date','home_team','W']], how='inner',on=['game_date', 'home_team'])
    ranking = pd.read_csv('../data/rankings.csv') #https://www.baseball-reference.com/leagues/MLB/2018-standings.shtml
    ###ASK USER###
    
    # team = 'BOS'
    team = raw_input("Enter a home team: ")
    probPrev = getState(df, 7, 'Bot', 0, 0, 0, 0 )
    probCurrent = getState(df, 7, 'Bot', 0, 0, 0, 1)
    r = getRank(ranking, team)
    newProb = getWeight(probPrev, probCurrent, r)
    print (newProb)

if __name__ == '__main__':
    main()
