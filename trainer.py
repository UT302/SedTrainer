import shlex, subprocess
import random 
import io
import math
import sys
import string 

adjective = ["big","small","enormous","ephereal"]

noun = ["dolphin","cat","tiger","john"]

verb = ["ran after", "ate", "bit", "kicked"]

#infinitive = ["","","",""]

def makeSentence():

    genSentence = [random.choice(adjective),(random.choice(noun)),(random.choice(verb)),random.choice(noun)]
  
    return (genSentence)

startSentence = makeSentence()

def sentenceShift():
      
    randWord = random.choice(startSentence)
         
    wordInd = startSentence.index(randWord)

    revWord = randWord[::-1]
      
    revSentence = startSentence.copy()
     
    revSentence[wordInd] = revWord

    return (revSentence)

endSentence = sentenceShift()

strStart = (" ".join(startSentence))
strEnd = (" ".join(endSentence))


def randChars(chrAmount):

    charList = (list(string.ascii_letters))

    randStr = (random.sample(charList, k = chrAmount))

    cleanStr = ("".join(randStr))

    return (cleanStr)

def lowerCase(strStart):

    if strStart == strStart.lower():
        print("Right answer.")
    else:
        print("Wrong answer.") 


randChr = (random.randrange(5, 7))

fRange = [randChars(randChr)]

qRange = [lowerCase]

def quizChooser():

    problem = [random.choice(fRange), random.choice(qRange)] 

    return (problem)



print(f"""Welcome to the sed program trainer.
Given text:
{strEnd}""")
print("-" * 25)
print(f"""Correct version:
#{strStart}""")
print("-" * 25)
print("Your sed script:")
print(strStart)

userSedScript = input("> ")

answer = subprocess.getoutput(f"echo {strEnd} | {userSedScript}")

if str(answer) == str(strStart):

    print("good job!")
