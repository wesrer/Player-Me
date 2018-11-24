import sys
from project.src.Model.missions.AddNewMission import addNewMission

def main ():

    # the action identifier 
    if (sys.argv[1].lower() == 'add'):
        # TODO: add some more preprocessing. This is very simple.
        missionName = ' '.join(sys.argv[3:])
        addNewMission(missionName, sys.argv[2])

if __name__ == "__main__":
    main()

