
from ops import FindDuplicates, MoveAndReviewDuplicates
from pprint import pprint as pp
from formatters import AppLogger
import os 


imgDir = "/Users/latikamehra/Pictures/Jonny1/"

logDir = os.path.dirname(os.path.abspath(__file__))+"/logs/"


AppLogger.initiate(logDir, "FindAndHandleDuplicates", consoleFlag=False)



toKeepDir = imgDir+"/DuplicatesToReview/ToKeep"
secDupesDir = imgDir+"/DuplicatesToReview/ToRemove"

fnd = FindDuplicates.FindDuplicates(imgDir)
dupeDict = fnd.fetchAllDuplicates()

mv = MoveAndReviewDuplicates.MoveAndReview(imgDir,toKeepDir,secDupesDir)

#mv.moveAndReviewDuplicates(dupeDict)

#mv.moveDupesToKeepToOriginalDir()

#mv.removeDuplicates()
