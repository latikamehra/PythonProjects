
from ops import FindDuplicates, MoveAndReviewDuplicates
from pprint import pprint as pp
from formatters import AppLogger
import os 


imgDir = "/Users/latikamehra/Pictures/Jonny1/"

toKeepDir = imgDir+"/DuplicatesToReview/ToKeep"
secDupesDir = imgDir+"/DuplicatesToReview/ToRemove"

logDir = os.path.dirname(os.path.abspath(__file__))+"/logs/"
AppLogger.initiate(logDir, "FindAndHandleDuplicates", consoleFlag=False)


fnd = FindDuplicates.FindDuplicates(imgDir)
dupeDict = fnd.fetchAllDuplicates()

mv = MoveAndReviewDuplicates.MoveAndReview(imgDir,toKeepDir,secDupesDir)

#mv.moveAndReviewDuplicates(dupeDict)

#mv.moveDupesToKeepToOriginalDir()

#mv.removeDuplicates()
