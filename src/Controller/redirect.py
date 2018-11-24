import sys
from project.src.Model.missions.AddNewMission import addNewMission

def main ():
    if (sys.argv[1].lower() == 'add'):
        addNewMission(str(sys.argv[3:]), sys.argv[2])


if __name__ == "__main__":
    main()
