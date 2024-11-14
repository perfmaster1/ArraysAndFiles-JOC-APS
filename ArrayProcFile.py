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
#
#
#  Author: Daniel Wroblewski
#    Date: 11/10/2024
#   Status: Authoring
# @@==================================================================================================@@

import os
from pathlib import Path

# -------------------------------------------------------------------------------
#
#  Function is_readable:  function to tell if the file can be read by the current user
#
# -------------------------------------------------------------------------------
def is_readable(filepath):
    return os.access(filepath, os.R_OK)

# -------------------------------------------------------------------------------
#
#  Function file_content:  function to return number of lines and the array of 
#                          file lines
# -------------------------------------------------------------------------------
def file_content(filePath):
	lineCount=0
	fileStr=[]

	with open(filePath, 'r') as fn:
		lineCount=sum(i for lines in fn)

	with open(filePath,'r') as fn2:
		for lines in fn2:
			fileStr.append(lines.strip())

	fn.close()
	fn2.close()	
	return lineCount,fileStr	
	
# -------------------------------------------------------------------------------
#
#  Function fileStatsResult:  function to return requested information
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
#
# 
def main():

	wkdir = "C:\\MyPythonProjects\\JOC-AdvProbSolvg\\ArraysAndFiles-JOC-APS\\"

	wkdir=wkdir.strip()                               # removes any trailing spaces or leading ~
	fileIn="turing.txt" 
	print("Current directory where input and output files exist / created is ",cwd)
	if not os.path.exists(wkdir):
		print("Directory path ",wkdir," does not exist. Closing")	
		exit(1)	

	filePath=os.path.join(wkdir, fileIn)
	filePathTest=Path(filePath)
	if not os.path.exists(filePath):
		print("File ",fileIn," cannot be found or path ",wkdir," is wrong file path. Closing")
		exit(1)	
	if not filePathTest.Path.is_file():
		print("File ",fileIn," is not a regular text readable file. Closing")
		exit(1)			
	if not filePathTest.Path.is_readable():
		print("Current user does not have permissons to read file: ",filePath," ,Closing")
		exit(1)	

#
#  File and path exist and file useable by program. Now get the lines
#	
	lineCount=0
	fileLines=[]
	lineCount,fileLines=file_content(filePath)
#
#  If lineCount < 2 then cannot fulfill the request. 
#  If linecount 2 then index 0 is first and last two are index 0 and 1
#  Else first is index 0 and last two are linecount-1 and linecount-2
#

main()