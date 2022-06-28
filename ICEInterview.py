# Please provide a sample python program that:
#  takes text file as input and produces output  
# showing the most used words in 
# that text in descending order.
# (* make all words lowercase *)
#-----------------XC-----------------------------------------------------
# For extra credit show the total number of words, total 
# number of lines, and the total number of paragraphs.
#=====================================================================================

from collections import Counter
from tabulate import tabulate
import os


 
#===================VARIABLES======================================================================

textFileImp = ['file1.txt']
FOLDER_PATH = r"C:\Users\Sir Ronnie\Documents\1CODING\Python\interviewQ"
fileSource = [open(f).read() for f in textFileImp] #==========|'r' is reading mode in py|========================== open('file1.txt','r')||||
words = fileSource.lower()
wordUses = 0
lineCount = 0


#Extra Credit Function, Count # of lines, #of words=================================================
Lines = words.readlines()         #readlines does exactly that, from the text file referenced.
for line in Lines:
        lineCount += 1
        print("Line{}: , Words:{}, # of Words:{}".format(lineCount, line.strip(),line.count()));


# Count number of words in file function=============================================================
def wordNum (words):                                  # This function will iterate through the spaces
    wordsX = words.strip()                            # in the lines, each space = +1 word. The count
    count = 1 +" : number of words in provided file"  # begins at 1 to account for first words lack of
    for i in wordsX:                                  # space due to the .strip() method
        if i == " ":
            count += 1
    return count;



# #Determine frequency of individual word use

#=======================================================================================================
# wordCounter = line.lower().replace(',','').replace('.','').split(" ") # this makes everything lowercase, swaps " , " with " " to create spaces, uses split to remove said spaces.
# for charCount in wordCounter:
#     words.append(charCount);                      <=====================Previous code, new code is cleaner works the same see below
#========================================================================================================
def wordCounter(words):
    wordUses = Counter(words.split())



#Table to display information
data = [{lineCount}]
