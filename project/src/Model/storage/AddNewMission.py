from pathlib import Path
from FindNextMissionNumber import findNextMissionNumber
import sys
import json

# resolving the project Path that we can then use as reference
projectPath = Path('project').resolve()

def addNewTask(taskName, dataPath, taskID):
    with open(dataPath / 'tasks', 'a') as file:
        file.write(
            taskID + ',' +
            taskName + '\n')

def addNewHabit(habitName, dataPath, habitID):
    with open(dataPath / 'habits', 'a') as file:
        file.write(
                habitID + ',' +
                habitName + '\n')


def addNewQuest(questName, dataPath, questID):
    with open(dataPath / 'quests', 'a') as file:
        file.write(
                questID + ',' +
                questName + '\n')

def addNewMission(missionName, missionType):
    dataPath = projectPath / 'data'

    missionID = findNextMissionNumber(missionType)

    if (missionType == 't' or missionType.lower() == 'task'):
        addNewTask(missionName, dataPath, missionID)

    elif (missionType == 'h' or missionType.lower() == 'habit'):
        addNewHabit(missionName, dataPath, missionID)

    elif (missionType == 'q' or missionType.lower() == 'quest'):
        addNewQuest(missionName, dataPath, missionID)

# take the new task, append to existing json
# replace the existing json with new json