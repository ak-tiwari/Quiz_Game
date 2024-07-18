print("WELCOME TO MY COMPUTER QUIZ !")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


answer = input("What does GPU STANDS FOR? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")
    
answer = input("What does RAM stands for? ")
if answer.lower() == " random access memory":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


print ("you got "+ str(score) + " questions correct!")

print("you got" + str((score/4)*100) + "%") 
