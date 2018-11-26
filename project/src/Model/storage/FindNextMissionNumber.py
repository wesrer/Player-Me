from pathlib import Path
from project.src.storage.makeChangesToStoredFiles import incrementNextMission, deleteEmpty
import json

# resolving the project Path that we can then use as reference
projectPath = Path('project').resolve()

def findNextMissionNumber(missionType):
    data = fileToData()

    # tasks
    if (missionType == 't' or missionType.lower() == 'task'):
        if (data['emptytasks'] == 'None'): 
            incrementNextMission('t') #TODO:
            return data['tasks']
        else:
            empty = findFirstEmpty(data, 'emptytasks')
            deleteEmpty(empty, 't') # TODO:
            return empty
   
    # habits
    elif (missionType == 'h' or missionType.lower() == 'habit'):
        if (data['emptyhabits'] == 'None'):
            incrementNextMission('h')
            return data['habits']
        else:
            empty = findFirstEmpty(data, 'emptyhabits')
            deleteEmpty(empty, 'h')
            return empty

    # quests
    elif (missionType == 'q' or missionType.lower() == 'quest'):
        if (data['emptyquests'] == 'None'):
            incrementNextMission('q')
            return data['quests']
        else:
            empty = findFirstEmpty(data, 'emptyquests')
            deleteEmpty(empty, 'q')
            return empty

# reads the mission_info file and converts the data into a dictionary
def fileToData():
    dataDict = {}
    with open(projectPath / 'local' / 'mission_info', 'r') as file:
        
        # read the file one line at a time
        for line in file.readlines():
            # the keys and the values are separated by ':'
            line = line.split(':')
            dataDict[line[0]] = line[1]

    return dataDict
                

def findFirstEmpty(someDictionary, key):
    return someDictionary[key].split(',')[0]
    

            

