'''
Created on Aug 20, 2019

@author: latikamehra
'''

from formatters import AppLogger, PrettyPrinter
import os
from imageanalysis import ImageFileList, BasicImageDetails, PixelData
from ops import ImageDetailsDataFrame, PotentialDuplicates, PrimarySecondaryDuplicates, ProbableDuplicates
from manageDuplicates import CleanupDuplicates, ManageDuplicates, DuplicatesForReview

imgDir = "/Users/latikamehra/Pictures/Jonny1/"

toKeepDir = imgDir+"/DuplicatesToReview/ToKeep"
secDupesDir = imgDir+"/DuplicatesToReview/ToRemove"

curDir = os.path.dirname(os.path.abspath(__file__))
debugDir = curDir+"/debug/"
logDir = curDir+"/logs/"
opDir = curDir+"/output/"

AppLogger.initiate(logDir, "FindAndHandleDuplicates", consoleFlag=False)
log = AppLogger.logger.getChild(__name__)


    
basicDetsLog = AppLogger.prntr("BasicDetails", debugDir, "BasicImageDetails", consoleFlag=False)
dupleListOP = AppLogger.prntr("DupeList", opDir, "ListOfPotentialDuplicates", consoleFlag=True)

pp = PrettyPrinter.PrettyPrint()


imgFileList = ImageFileList.fetch(imgDir)

detDictDict = BasicImageDetails.fetch(imgFileList)

basicDetsLog.debug(pp.collectionPrnt(detDictDict))

df = ImageDetailsDataFrame.construct(detDictDict)

potentialDupeListList = PotentialDuplicates.fetch(df)

probableDupeListList = ProbableDuplicates.fetch(potentialDupeListList)

dupeDict = PrimarySecondaryDuplicates.fetchDict(probableDupeListList)

dupleListOP.debug(pp.collectionPrnt(dupeDict))








