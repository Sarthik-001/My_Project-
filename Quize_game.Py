print("\t\t\t-------------------------------------------------------------------")
print("\t\t\t\t\tWelcome to my Computet Quize")
print("\t\t\t\t\t----------------------------")

playing = input("Do you Want to Play (yes/no): ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play.")
score = 0

answer = input("\tWhat dose CPU Fullform : ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("\tWhat dose PSU Fullform : ")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose GPU Fullform : ")
if answer.lower() == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose RAM Fullform : ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose OTP Fullform : ")
if answer.lower() == "one time password":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose LED Fullform : ")
if answer.lower() == "light emitting diode":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose NTFS Fullform : ")
if answer.lower() == "new technology file system":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose FAT Fullform : ")
if answer.lower() == "file allocation table":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose LCD Fullform : ")
if answer.lower() == "liquid crystal display":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("\tWhat dose ROM Fullform : ")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " question correct!")
print("You got " + str((score / 10) * 100) + "%.")

print("\t\t\t-------------------------------------------------------------------")