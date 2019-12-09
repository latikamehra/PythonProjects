'''
Created on Aug 7, 2019

@author: latikamehra
'''

import pandas as pd
from dbOps import Postgres
import logging
from ops import LoadCSVtoPostgres
from sqls import PlayCountByMonth as pcm
from sqls import PlayCountBySong as pcs
from sqls import PlayCountBySongAndMonth as pcsm
from sqls import Top_N_SongsOfTheMonth as topNsongs
from visualization import MultipleLineGraphs, MultipleLineSubplots, BarGraph, BarSubplots
import pprint

csvFile = "/Users/latikamehra/Documents/AppleMusicPlayActivity.csv"
tableName = "data_analysis.apple_music_activity"

pg = Postgres.postgres(tableName=tableName)
pg.connect()

def loadData():
    lvl = lvl=logging.INFO
    loadData = LoadCSVtoPostgres.Load(csvFile, tableName, lvl)
    loadData.createTable(True)
    loadData.insertData()
    loadData.pg.closeConns()

    
def analysePCSM():
    pcsm_res = pg.executeReadStatement(pcsm.sql.format(tableName))
    
    pcsmDict = {}
    
    
    for row in pcsm_res :
        song = row[0]
        yrmnth = str((row[1]))+"-"+str((row[2]))
        cnt = row[3]
        
        if song!=' ' and song!='':
            pcsmDict.setdefault(song, {}) # Set the default value for this song's key as an empty dictionary - won't effect if the key already exists
            pcsmDict[song][yrmnth]=cnt # Update the play-count value
        
    mlg = MultipleLineSubplots.LineSubPlots("PlayCountBySongAndMonth", "Radiohead Song Play Counts By Year & Month", "Year-Month", "Play Count")   
        
    mlg.plotMultipleLineGraphs(5, pcsmDict)
    
    
def analysePCM():
    pcm_res = pg.executeReadStatement(pcm.sql.format(tableName))
    
    pcmXaxis = []
    pcmYaxis = []
    
    
    for row in pcm_res :
        yrmnth = str((row[0]))+"-"+str((row[1]))
        cnt = row[2]
        
        pcmXaxis.append(yrmnth) 
        pcmYaxis.append(cnt)
      
    bg = BarGraph("PlayCountByMonth", "Radiohead Play Count By Year-Month", "Year-Month","Play Count") 
    bg.plotGraph( pcmXaxis, pcmYaxis)
    
    
def analysePCS():
    pcs_res = pg.executeReadStatement(pcs.sql.format(tableName))
    
    pcsXaxis = []
    pcsYaxis = []
    
    
    for row in pcs_res :
        song = row[0]
        if len(song)>33 : song = song[0:29]+"..." 
        cnt = row[1]
        
        pcsXaxis.append(song)
        pcsYaxis.append(cnt)
      
    bg = BarSubplots.BarSubplots(30, "PlayCountBySong", "Radiohead Play Count By Songs", "Songs","Play Count") 
    bg.plotGraph( pcsXaxis, pcsYaxis)


def fetchTopNSongs(num):
    sql = topNsongs.sql.format(tableName, str(num))
    topSong_res = pg.executeReadStatement(sql)
    
    #pprint.pprint (topSong_res)
    
    df = pd.DataFrame(topSong_res, columns=('Date', 'Song', 'PlayCount'))
    
    grpsByDate = df.groupby('Date')
    
    pcsXaxis = []
    pcsYaxis = []
    
    for dt, dtGrp in grpsByDate :
        pcsXaxis = dtGrp['Song']
        pcsYaxis = dtGrp['PlayCount']
        bg = BarGraph.BarGraph("TopSongsPerMonth", "Radiohead Play Count", dt, "Counts")
        bg.plotGraph(pcsXaxis, pcsYaxis)


fetchTopNSongs(5)
#analysePCS()
#analysePCM()    
#analysePCSM()
    
