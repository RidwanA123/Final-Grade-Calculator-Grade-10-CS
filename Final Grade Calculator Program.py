
testmark = []
quizmark = []                                 #Varibles
assignmentmark = []
quiztotal = 0
testtotal = 0
assignmenttotal = 0

print(75 * "*")    #Discription
print("This calculator helps you determine your final course grade without needing your current grade.")
print("You enter your number of quizes and the marks recived on them, number of tests and the marks recived on them, number of assignments and the marks recived on them, and finally your summative or exam mark which is worth 30% of your final grade.")
print("If you don't have tests, assignments, or quizes, just type 0 when prompted. But you need to have at least two of these three components or it would be harder (and impossible for this program)to determine your final grade.")
print("Keep in mind that all these weights are based on the actual course marking weights and that the teacher could have thier own mark weighting system.")

print(75 * "*")

quizes = int(input("How many quizes did you have?> "))
if (quizes > 0):
    
    for a in range(quizes):
            print("What was your mark for quiz",a+1,"?")
            q = int(input(">"))
            quizmark.append(q)                                     #Gets Input from user for each componet calculates the average for each
    for b in range(quizes):
            quiztotal = quiztotal + quizmark[b]

    quizmarks = len(quizmark)
    quizaverage = quiztotal/quizmarks
tests = int(input("How many unit tests did you have?> "))
if (tests > 0):
    
    for c in range(tests):
        print("What was your mark for unit test",c+1,"?")
        t = int(input(">"))
        testmark.append(t)
    for d in range(tests):
        testtotal = testtotal + testmark[d]
    testmarks = len(testmark)
    testaverage = testtotal/testmarks
assignments = int(input("How many assignments did you have?> "))
if (assignments > 0):
    
    for e in range(assignments):
        print("What was your mark for assignment",e+1,"?")
        a = int(input(">"))
        assignmentmark.append(a)
    for f in range(assignments):
       assignmenttotal = assignmenttotal + assignmentmark[f]
    assignmentmarks = len(assignmentmark)
    assignmentaverage = assignmenttotal/assignmentmarks



final = int(input("What was your mark for the summative or exam (30%)?> "))
if (quizes == 0):
    finalgrade = (0.30*assignmentaverage + 0.40*testaverage + 0.30*final)/1
    finalgrade = float(finalgrade)                                                          #Calculates the final grade accoding to the wieghts and what user inputted, then outputs the grade
    finalgrade = round(finalgrade,1)
    testaverage = round(testaverage,1)
    assignmentaverage = round(assignmentaverage,1)

    print(75*"*")
    print("Your test average is "+str(testaverage)+"%")
    print("Your assignment average is "+str(assignmentaverage)+"%")     
    print("Your Final Course Grade is " + str(finalgrade) +"%")
    
    print(75*"*")
elif (assignments == 0):
    finalgrade = (0.20*quizaverage + 0.50*testaverage + 0.30*final)/1
    finalgrade = float(finalgrade)
    finalgrade = round(finalgrade,1)

    testaverage = round(testaverage,1)
    quizaverage = round(quizaverage,1)

    print(75*"*")
    print("Your test average is "+str(testaverage)+"%")
    print("Your quiz average is "+str(quizaverage)+"%")     
    print("Your Final Course Grade is " + str(finalgrade) +"%")
    print(75*"*")
elif (tests == 0):
    finalgrade = (0.50*assignmentaverage + 0.20*quizaverage + 0.30*final)/1
    finalgrade = float(finalgrade)
    finalgrade = round(finalgrade,1)
    assignmenttaverage = round(assignmentaverage,1)
    quizaverage = round(quizaverage,1)

    print(75*"*")
    print("Your assignment average is "+str(assignmentaverage)+"%")
    print("Your quiz average is "+str(quizaverage)+"%")     
    print("Your Final Course Grade is " + str(finalgrade) +"%")
    
    print(75*"*")
else:
    finalgrade = (0.20*assignmentaverage + 0.15*quizaverage + 0.35*testaverage + 0.30*final)/1
    finalgrade = float(finalgrade)
    finalgrade = round(finalgrade,1)
    testaverage = round(testaverage,1)
    quizaverage = round(quizaverage,1)
    assignmentaverage = round(assignmentaverage,1)
    print(75*"*")
    print("Your test average is "+str(testaverage)+"%")
    print("Your quiz average is "+str(quizaverage)+"%")
    print("Your assignment average is "+str(assignmentaverage)+"%")     
    print("Your Final Course Grade is " + str(finalgrade) +"%")
    
    print(75*"*")



    
        
