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
  
  randWord = random.choice(genSentence)
      
  wordInd = genSentence.index(randWord)

  revWord = randWord[::-1]
  
  revSentence = genSentence.copy()
  
  revSentence[wordInd] = revWord

  return (" ".join(revSentence))


print("""Welcome to the sed program trainer.
Change the word in this sentence to the correct one:""")
print("-" * 25)
startSentence = makeSentence()
print(startSentence)
print("-" * 25)


userScript = input("> ")

#subprocess.call(userScript, shell = True)
#subprocess.run(userScript, text = True, shell = True)
answer = subprocess.getoutput(userScript)

if answer == "trainer.py":
    print("good job!")

    





