import sys
import pickle
from datetime import date, timedelta
from os import path

def main(aList):

    try:
        #checks if a dictionary is available to be uploaded 
        if path.exists("pickledDict.p"):
            myDict = pickle.load(open("pickledDict.p","rb"))

        #if no dictionary available, creates new one
        if not path.exists("pickledDict.p"):
            myDict = {}

        # if you want to add a task to spaced repeat
        if aList[1] == "add":

            # if you want add a bunch of tasks from text file
            if aList[2][-4:] == ".txt":
                if not path.exists(aList[2]):
                    print("File not in directory")
                    return 
                with open(aList[2], "r") as txtInput:
                    #makes list of strings of each line in txt file
                    listOfLines = txtInput.readlines() 
                    #pops the "\n" out of each string
                    for i in range(len(listOfLines) - 1):
                        listOfLines[i] = listOfLines[i][0:-1]
                    print(listOfLines)
                    for i in range(len(listOfLines)):
                        for j in [1, 2, 4, 8, 16, 32, 64, 128]:
                            dateofTask = date.today()+timedelta(days=i+j-1)
                            try:
                                myDict[dateofTask] += f" {listOfLines[i]}"
                            except:
                                myDict[dateofTask] = listOfLines[i]

            # if you want a singular task that does not end in ".txt"
            else:
                for i in [1, 2, 4, 8, 16, 32, 64, 128]:
                    laterDay = date.today()+timedelta(days=i-1)
                    try:
                        myDict[laterDay] += " {}".format(aList[2])
                    except:
                        myDict[laterDay] = aList[2]

        # if you want to see the tasks for today
        if aList[1] == "view":
            if aList[2] == "tommorrow":
                for word in myDict[date.today() + timedelta(days=1)].split():
                    print(word)
            else:
                try:
                    for word in myDict[date.today()].split():
                        print(word)
                except:
                    print("No tasks!")

        # to see schedule for later days
        if aList[1] == "check":
            for day in sorted(myDict.keys()):
                print(f"\nOn {day} you have to do:\n")
                for word in myDict[day].split():
                    print(word)

    finally:
        pickle.dump(myDict, open("pickledDict.p","wb"))

if __name__ == "__main__":
    main(sys.argv)        