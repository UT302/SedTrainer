import shlex, subprocess
import random
import io
import math
import sys


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




print(f"""Welcome to the sed program trainer.
Change the word in this text to the correct one:
Given text:
{strEnd}""")
print("-" * 25)
print(f"""Correct version:
{strStart}""")
print("-" * 25)
print("Your sed script:")
userSedScript = input("> ")

answer = subprocess.getoutput(f"echo {strEnd} | {userSedScript}")

if str(answer) == str(strStart):

    print("good job!")

    





