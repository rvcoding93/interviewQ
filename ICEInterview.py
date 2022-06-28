# Please provide a sample python program that:
#  takes text file as input and produces output 
# showing the most used words in 
# that text in descending order.
# (* make all words lowercase *)
#-----------------XC-----------------------------------------------------
# For extra credit show the total number of words, total 
# number of lines, and the total number of paragraphs.
#=====================================================================================

from importlib.metadata import files
from tabulate import tabulate

fileSource = open("interviewText.txt","r") #==========|'r' is reading mode in py|==========
words = fileSource.lower()
wordUses = 0
lineCount = 0


#Extra Credit Function, Count # of lines, #of words
Lines = words.readlines()         #readlines does exactly that, from the text file referenced.
for line in Lines:
        lineCount += 1
        print("Line{}: , Words:{}, # of Words:{}".format(lineCount, line.strip(),line.count()))


# Count number of words function
def wordNum (words):                                  # This function will iterate through the spaces
    wordsX = words.strip()                            # in the lines, each space = +1 word. The count
    count = 1 +" : number of words in provided file"  # begins at 1 to account for first words lack of
    for i in wordsX:                                  # space due to the .strip() method
        if i == " ":
            count += 1
    return count


