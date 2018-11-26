import json
import changeMissionFiles from makeChangesToMissionFiles

validChangeTypes = 

# TODO:

# def incrementNextMission(missionType):

# def deleteEmpty(emptyValue, missionType):

# missionType -> either task, habit, queue or reward
# changeType -> add, modify, delete, completed or done, start, stop
def writeNewMissionFile(missionType, changeType, writeObject):
    jsonObject = json.dumps(writeObject, indent=4, separators=(',', ':'))

    if (missionType == 'r' or 
        missionType.lower() == 'reward' or 
        missionType.lower() == 'rewards'):

        checkForValidChangeTypes(missionType, changeType)
        commitChangesToRewards(writeObject)

def checkForValidChangeTypes(missionType, changeType):
    missionType = missionType.lower()
    
    switch
 

# def commitChangesToRewards():

# def commitChangestToMetaData():