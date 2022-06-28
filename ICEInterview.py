# Please provide a sample python program that takes text file 
# as input and produces output showing the most used words in 
# that text in descending order.
#-----------------XC-----------------------------------------------------
# For extra credit show the total number of words, total 
# number of lines, and the total number of paragraphs.
#=====================================================================================

from tabulate import tabulate

fileSource = open("interviewText.txt","r") #==========|'r' is reading mode in py|==========
wordCount = []
wordUses = 0
lineCount = 0


#Extra Credit Function, Count # of lines, #of words
Lines = fileSource.readlines()         #readlines does exactly that, from the text file referenced.
for line in Lines:
        lineCount += 1
        print("Line{}: , Words:{}".format(lineCount, line.strip()))