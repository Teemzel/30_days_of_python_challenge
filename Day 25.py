"""display the purpose of this program
display the instruction
ask the user a question
if the question is correct,display:"correct" and add 1 to the score
else display:"wrong"
go back to step 3 until all the question have been answered
print the score of the user"""

print("little history about myself")
print("select the letters with the correct option")
score=0

question1=input("what are my real name? \n(a)Dazzling gleam: \n(b)tolu gbemi: \n(c)sliver gold: \n")
if (question1.lower()=="a"):
   print("correct")
   score+=5
else:
   print("wrong")
   score-=2

question2=input("in what year was i born? \n(a)2000: \n(b)1990: \n(c)1998: \n")
if (question2.lower()=="c"):
   print("correct")
   score+=5
else:
   print("wrong")
   score-=2

question3=input("what is my complexion? \n(a)yellow: \n(b)chocolate: \n(c)white: \n")
if (question3.lower()=="b"):
   print("correct")
   score+=5
else:
   print("wrong")
   score-=2

question4=input("how many siblings do i have? \n(a)4: \n(b)1: \n(c)5: \n")
if (question4.lower()=="c"):
   print("correct")
   score+=5
else:
   print("wrong")
   score-=2

question5=input("what is the name of my school? \n(a)future map: \n(b)tablagos: \n(c)wetlagos: \n")
if (question5.lower()=="a"):
   print("correct")
   score+=5
else:
   print("wrong")
   score-=2

print("your score is",score)