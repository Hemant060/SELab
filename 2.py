print("Welcome to my game! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play! ")
score = 0

answer = input("What is the capital city of Nepal? ")
if answer.lower() == "kathmandu":
    print("Correct! ")
    score +=1
else:
    print("Incorrect! ")    

answer = input("What is the capital city of India? ")
if answer.lower() == "new delhi":
    print("Correct! ")
    score +=1
else:
    print("Incorrect! ")  

answer = input("Which is the highest peak in the world? ")
if answer.lower() == "mt.everest":
    print("Correct! ")
    score +=1
else:
    print("Incorrect! ") 

answer = input("Which city is the hottest city of Nepal? ")
if answer.lower() == "nepalgunj":
    print("Correct! ")
    score +=1
else:
    print("Incorrect! ")     

print("You got " + str(score) + " questions correct!")  
print("You got " + str(score/4 * 100) + "%")  