# @@==================================================================================================@@
#
#  Program ArrayProcFile:
#
#  ArraysAndFilesExercise - Advanced Problem SOlving Week 6 : Day 1: Arrays & Dictionaries / 
#      Day 1: Learning Activity: Arrays & Files
#
# Program: Read in specified file 
#          Create an array (or list) in your program to store each line of the file as a separate element.
#          Open the file, read in each line into your array/list, and close the file.
#          Print out the first & last two elements of your array/list, and the number
#           of lines in the file
#                 
# REQUIREMENT: Your program should not take any user input.
#
# Specifications:  When coding, consider the following guidelines:
#
#   Correctness: Your code should perform as specified. Correctness will count for the
#                 largest portion of your grade.
#
#   Comments: For each function/method that you design from scratch, write a summary
#              comment. Within functions, the more complicated parts of your code should be
#              described using "internal" comments.
#
#   DRYness: If you find yourself repeating a task, you can add a helper function and call
#               that function instead of duplicating the code, or place the code inside a loop. 
#               A good rule of thumb is if a function/method is more than about 20 lines 
#               long, consider introducing helper functions to do some of the work, even if
#               they are only called once.
#
#   Programming style: Your variable names should be meaningful and your code as simple
#                 and clear as possible. Each line must be less than 80 characters long including spaces &
#                 comments. You can break up long lines using \ in python, or newlines in Java.
#
#   Manually download the file turing.txt:
#      http://emhill.github.io/150/morea/10.dict//data/turing.txt & save to your computer 
#       or  upload to repl.it.
#
#  NOTE: If we wanted to find out the file type if not a regular file we would use
#        python-magic or 
# #      filetype library:       https://github.com/h2non/filetype.py
#
#  Certain functions associated with os.path are used in this code. 
#  Guidance for importing os vs os.path can be found in this StackOverflow article:
#  Should I use `import os.path` or `import os`?
#    https://stackoverflow.com/questions/2724348/should-i-use-import-os-path-or-import-os
#    https://docs.python.org/3/library/os.path.html#os.path.isfile
#
#  I found os library to be sufficient for this program. 
#
#  An intersting code line is as follows:
#   filePathTest=Path(filePath)   -- but requires pathlib library and python 3.4
#                                       'from pathlib import Path'
#  >>> I dispensed with this in favor of os 
#
#  Author: Daniel Wroblewski
#    Date: 11/14/2024
#   Status: COMPLETE
# @@==================================================================================================@@

import os   

#
# -------------------------------------------------------------------------------
#
#  Function is_readable:  function to tell if the file can be read by the current user
#
# -------------------------------------------------------------------------------
def is_readable(filepath):
    return os.access(filepath, os.R_OK)


# -------------------------------------------------------------------------------
#
#  Function is_readable:  function to tell if the file can be read by the current user
#
# -------------------------------------------------------------------------------
def isExistNotDir(wDir):

	if not os.path.exists(wDir):
		print("User selected work directory path ",wDir," does not exist. Closing")	
		return True
	if not os.path.isdir(wDir):
		print("Location ",wDir," is not a directory. Closing")	
		return True

	return False


# -------------------------------------------------------------------------------
#
#  Function pathSet:  set up the paths for the program
#
# -------------------------------------------------------------------------------
def pathSet(wkd):

	os.chdir(wkd)         # anchor working dir to requested dir
	currwd=os.getcwd()
	print("Current directory where input and output files exist / created is ",currwd)
	return


# -------------------------------------------------------------------------------
#
#  Function existAsNotFileNotReadable:  set up the paths for the program
#                                       Any failure condition returns True 
#
# -------------------------------------------------------------------------------

def existAsNotFileNotReadable(fPath,f_in,wkd):
#
#  TEST: 'does path exist' :
#
	if not os.path.exists(fPath):
		print("File ",f_in," cannot be found or path ",wkd," is wrong file path. Closing")
		return True	
#
#  TEST: Is filePath a file or directory?
#
	if not os.path.isfile(fPath):    # not a file, test if dir then give up
		if os.path.isdir(fPath):
			print("filePath ",fPath," is a directory, not a file.")	 
			return True
		print("File ",f_in," is not a regular text readable file. Closing")
		return True			
#
#   TEST: is file readable:
#
	if not is_readable(fPath):
		print("Current user does not have permissons to read file: ",fPath," ,Closing")
		return True

	return False	


# -------------------------------------------------------------------------------
#
#  Function minLine:  determine if the input file has enough lines to fulfill
#                     the requirements. Must have 2 or more lines
#
#
#  If lineCount < 2 then cannot fulfill the request. 
#  If linecount 2 then index 0 is first and last two are index 0 and 1
#  Else first is index 0 and last two are linecount-1 and linecount-2
#	(will figure this out later) 
#
# -------------------------------------------------------------------------------
def minLine(fp):

	linesCount=sum(1 for _ in open(fp, 'r'))
	if linesCount > 1:
		return True

	return False


# -----------------------------------------------------------------------------------
#
#  Function file_content:  function to return number of lines and the array of 
#                          file lines
#
#  - open file multiple times, once for each operation/calculation/data struct build
#
# -----------------------------------------------------------------------------------
def file_content(filePath):
	lineCount=0
	fileStr=[]
#
#  choose one method:  
#
	with open(filePath, 'r') as fn:
		lineCount=sum(1 for _ in fn)
#
#	lineCount=sum(1 for _ in open(filePath, 'r'))
#
	with open(filePath,'r') as fn2:
		for lines in fn2:
			fileStr.append(lines.strip())   # cleanup the line before array insert

	fn.close()
	fn2.close()	
	return lineCount,fileStr	


# -------------------------------------------------------------------------------
#
#  Function fileStatsResult:  function to return the result requested in the
#                              assigned requirements in program header
#
# -------------------------------------------------------------------------------
def fileStatsResult(count,lineArray):

	fl=0
	sl=count-2
	ll=count-1
	print("First line is ",lineArray[fl])
	print("Second to last line is ",lineArray[sl])
	print("Last line is ",lineArray[ll])
	print("<=====================================>")
	print("TOTAL LINE COUNT IS: ",count)

	return

# -------------------------------------------------------------------------------
#  main program
# -------------------------------------------------------------------------------
#
#  The working directory is hardcoded and input file is homed at program start.
#
#  Conditions checked:
#  -------------------------------
#   Directory path exists
#   File exists
#   File is a regular text file and not a special file, e.g. directory, socket, executable program,
#    etc
#   User has permissons to read the file
#   and other conditions
#
def main():
	#
	#   Hardcoded working directory - no user input allowed
	#
	wkdir = "C:\\MyPythonProjects\\JOC-AdvProbSolvg\\ArraysAndFiles-JOC-APS\\"
	#
	wkdir=wkdir.strip()       # removes any trailing spaces or leading ~
	fileIn="turing.txt"       # input file

	if isExistNotDir(wkdir):  # directory checks
		exit(1)

	pathSet(wkdir)
	filePath=os.path.join(wkdir, fileIn)    # add in filename to path as 'filePath'

	if ( existAsNotFileNotReadable(filePath,fileIn,wkdir)  ):  # multiple checks
		exit(1)

	if not minLine(filePath):            # input file must have 2 or more lines
		exit(1)
#
#  File and path exist and input file useable by program. Now get the lines:
#	
	lineCount=0
	fileLines=[]
	lineCount,fileLines=file_content(filePath)   # calculate and parse input file

	fileStatsResult(lineCount,fileLines)       # return required result

main()
