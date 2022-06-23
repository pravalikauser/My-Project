#The project is about finding dates in inputed text
import re
import time
data=input('enter your text here:')
pattern_to_find=re.finditer("\d{1,2}-\w{1,3}-\d{2,4}",data)
print("The dates in given text are:")
for i in pattern_to_find:
  time.sleep(1)
  print(i.group())

