import sys
import pickle
from datetime import date, timedelta
from os import path

def main(aList):

	try:
		#checks if a dictionary is available to be uploaded 
		if path.exists("pickledDict.p"):
			myDict = pickle.load(open("pickledDict.p","rb"))
			print(myDict)

		#if no dictionary available, creates new one
		if not path.exists("pickledDict.p"):
			myDict = {}

		# if you want to add a task to spaced repeat
		if aList[1] == "add":

			# if you want add a bunch of tasks from text file
			if aList[2][-4:-1]+aList[2][-1] == ".txt":
				if not path.exists(aList[2]):
					print("File does not exist xor not in directory xor both, rerun program")
					return 0
				with open(aList[2], "r") as txtInput:
					listOfLines = txtInput.readlines()
					for index, task in enumerate(listOfLines):
						task = task.join(" ")
						for i in [1, 2, 4, 8, 16, 32, 64, 128]:
							dateofTask = date.today()+timedelta(days=i+index)
						try:
							myDict[dateofTask] += " {}".format(task)
						except:
							myDict[dateofTask] = task

			# if you want a singular task that does not end in ".txt"
			else:
				for i in [1, 2, 4, 8, 16, 32, 64, 128]:
					laterDay = date.today()+timedelta(days=i)
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
			for day in myDict.keys():
				print("\nOn {} you have to do:\n".format(day))
				for word in myDict[day].split():
					print(word)

	finally:
		pickle.dump(myDict, open("pickledDict.p","wb"))

if __name__ == "__main__":
	main(sys.argv)        