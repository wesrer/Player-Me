from pathlib import Path
import sys

projectPath = Path('project').resolve()
print(projectPath)

dataPath = projectPath / 'data'

def addNewMission (missionName, missionIdentifier):
    if (missionIdentifier == 't' or missionIdentifier.lower() == 'task'):
        addNewTask(missionName)
    elif (missionIdentifier == 'h' or missionIdentifier.lower() == 'habit'):
        addNewHabit(missionName)
    elif (missionIdentifier == 'q' or missionIdentifier.lower() == 'quest'):
        addNewQuest(missionName)

def addNewTask(taskName):
    # TODO: this needs to have more metadata and data
    # present version just for testing purposes
    with open(dataPath / 'tasks', 'a') as file:
        file.write(taskName + '\n')
    
def addNewHabit(habitName):
    print('no luck here baby')
def addNewQuest(habitName):
    print('no luck here baby')



