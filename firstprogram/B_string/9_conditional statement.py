age = 21

if(age >= 18):
    print("can vote")
    print("can drive")

    #traffic light code
    light ="green"
    if(light == "red"):
        print("stop")
    elif(light =="yellow"):
        print("look")
    elif(light =="green"):
        print("go")
    else:
        print("light is broken")
    print("end of code")

    
    num = 5

    if(num > 2):
        print("greater than 2")
    elif(num > 3):
         print("greater than 3")

age = 14
if(age >= 18):
    print("can vote") #indentation
else:
    print("cannot vote")

    #grade students based on marks
marks = int(input("enter student marks:"))
if(marks >= 90):
       print("grade A")
elif(marks >= 80 and marks< 90):
       print("grade B")
elif(marks >=70 and marks < 80):
       print("grade C")
else:
     grade = "D"
     print("grade of the student ->", grade)
