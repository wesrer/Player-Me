from pathlib import Path
import sys

# resolving the project Path that we can then use as reference
projectPath = Path('project').resolve()


def addNewTask(taskName, dataPath):
    with open(dataPath / 'tasks', 'a') as file:
        file.write(taskName + '\n')

def addNewHabit(habitName, dataPath):
    with open(dataPath / 'habits', 'a') as file:
        file.write(habitName + '\n')

def addNewQuest(questName, dataPath):
    with open(dataPath / 'quests', 'a') as file:
        file.write(questName + '\n')

def addNewMission(missionName, missionIdentifier):
    dataPath = projectPath / 'data'

    if (missionIdentifier == 't' or missionIdentifier.lower() == 'task'):
        addNewTask(missionName, dataPath)

    elif (missionIdentifier == 'h' or missionIdentifier.lower() == 'habit'):
        addNewHabit(missionName, dataPath)
    
    elif (missionIdentifier == 'q' or missionIdentifier.lower() == 'quest'):
        addNewQuest(missionName, dataPath)


