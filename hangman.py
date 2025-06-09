import random
print("Welcome to the HangMan game")
words=["apple","banana","cat","dog","egg","fish"]
randomword=random.choice(words).lower()
display=[]
for i in range(len(randomword)):
    display.append('_')
print(display)    #loops ends here
j=0
while j<6 and '_' in display:
  guess=input("enter your guess").strip().lower()
  #strip is used to avoid unwanted spaces at the beginning and ending
  found=False
  for letter in range(len(randomword)):
     if randomword[letter]==guess:
         display[letter]=guess
         found=True
  if not found: #if our guess is false
     j+=1 #we have to give another chance for user to guess   
     print("😢wrong choice")
  else:
     print("HUHU! correct guess")
  print('Current word:', ' '.join(display))   
  #after loop ends
if '_' not in display:
     print("\n you Won! The Word Was: ",randomword )  
else:
     print("\n Game Over.The word was: ",randomword)   