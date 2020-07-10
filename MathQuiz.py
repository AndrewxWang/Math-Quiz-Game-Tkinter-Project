from tkinter import *
import random
import time

q_num = 0
r_num = 0
root = Tk()
root.withdraw()

start_game = False
while (not start_game):
    q_num = input("Enter the number of questions: ")
    time.sleep(1)
    if q_num.isdigit() and int(q_num) > 0:
        q_num = int(q_num)
        while (not start_game):
            r_num = input("Enter highest randomly generated number: ")
            time.sleep(1)
            if r_num.isdigit() and int(r_num) > 0:
                print("Starting game...")
                time.sleep(1)
                print("Click the \"new question\" button to start!")
                time.sleep(1)
                root.lift()
                root.deiconify()
                r_num = int(r_num)
                start_game = True
                break
            else:
                print("That is not a valid input!")
    else:
        print("That is not a valid input!")

root.geometry("675x400")
root.focus_set()
ans =IntVar()
questions = 1
choice = -1
score=0
equation = []
rand = []
submit_button = Button
startt = Button
#a,b,c,d choices
ansA = Radiobutton
ansB = Radiobutton
ansC = Radiobutton
ansD = Radiobutton

def createEq(signs):
    eq=[]
    a= random.randint(1,r_num)
    b= random.randint(1,r_num)
    eq.append(a)
    eq.append(b)
    sign= random.choice(signs)
    eq.append(sign)
    eq.append(correctAnswer(a,b,sign))
##    print(eq)
    return eq

def correctAnswer(a,b,sign):
    result = 0
    if sign in["+"]:
        result = float(a+b)
    elif sign in["-"]:
        result = float(a-b)
    elif sign in["*"]:
        result = float(a*b)
    else:   #division
        result = round(a/b,3)
    return result

#ANSWERS
def createAns(equation):
    a = equation[0]
    b = equation[1]
    answers = [float(a+b),float(a-b),float(a*b),round(a/b,3)]
##    print(answers)
    return answers

#RANDOMIZE
def randomAns(answers):
    rand=[]
    for x in range(4):
        rando = random.choice(answers)
        rand.append(rando)
        answers.remove(rando)
    return rand

def createQuestion():
    signs=["+","-","*","/"]
    equation = createEq(signs)
    answers = createAns(equation)
    rand = randomAns(answers)

def buttonPressed():
    global submit_button, startt
    global score
    canvas.delete("all")
    answ = equation[3]
    print("Correct Answer: " + str(answ))
    if rand[choice] == answ:
        score+=1
        canvas.create_text(150,100, text="Correct! Score: " + str(score) + "/" + str(q_num))
    else:
        canvas.create_text(150,100,text="Wrong! Score: " + str(score) + "/" + str(q_num))
    submit_button["state"] = DISABLED
    startt["state"] = NORMAL
    ansA["state"] = DISABLED
    ansB["state"] = DISABLED
    ansC["state"] = DISABLED
    ansD["state"] = DISABLED
    print("Score: " + str(score))
    
def answA():
    global choice
    choice=0
    ans.set(1)
    submit_button["state"] = NORMAL
def answB():
    global choice
    choice=1
    ans.set(2)
    submit_button["state"] = NORMAL
def answC():
    global choice
    choice=2
    ans.set(3)
    submit_button["state"] = NORMAL
def answD():
    global choice
    choice=3
    ans.set(4)
    submit_button["state"] = NORMAL

def createGame():
    canvas.delete("all")
    signs=["+","-","*","/"]
    global submit_button, startt
    global equation, questions, ans, rand
    global score
    global ansA, ansB, ansC, ansD
    equation = createEq(signs)
    answers = createAns(equation)
    rand = randomAns(answers)
    ans.set(0)
    #BUTTONS
    if questions <= q_num:
        print("Question: " + str(questions))
        eq = Button(root, font='Helvetica 10 bold',text=" Question " + str(questions) + ": " + str(equation[0]) + " " + str(equation[2]) + " " + str(equation[1]) + " = ?   ",borderwidth=0)
        ansA=Radiobutton(root,text="A. " + str(rand[0]), variable=ans, value=1,command=answA)
        ansB=Radiobutton(root,text="B. " + str(rand[1]), variable=ans, value=2,command=answB)
        ansC=Radiobutton(root,text="C. " + str(rand[2]), variable=ans, value=3,command=answC)
        ansD=Radiobutton(root,text="D. " + str(rand[3]), variable=ans, value=4,command=answD)
        if questions > 1:
            eq.config(text=" Question " + str(questions) + ": " + str(equation[0]) + " " + str(equation[2]) + " " + str(equation[1]) + " = ?   ",borderwidth=0)
            ansA.config(text="A. " + str(rand[0]) + "          ")
            ansB.config(text="B. " + str(rand[1]) + "          ")
            ansC.config(text="C. " + str(rand[2]) + "          ")
            ansD.config(text="D. " + str(rand[3]) + "          ")

        submit_button = Button(root, text="submit", command = buttonPressed)    #SUBMIT

        submit_button.place(x=325,y=60)
        ansA.place(x=100,y=30)
        ansB.place(x=250,y=30)
        ansC.place(x=400,y=30)
        ansD.place(x=550,y=30)
        eq.place(x=275,y=2.5)
        questions+=1
        startt["state"] = DISABLED
        submit_button["state"] = DISABLED
    else:
        Score_label = Label(root,font="Arial 10 bold",text="Quiz complete! Final Score: " + str(score) + "/" + str(q_num))
        Score_label.place(x=250,y=200)
        startt["state"] = DISABLED
##    print(rand)
##    print(equation)
##    print(questions)

canvas = Canvas(root, bg="gainsboro", height=250, width=300)
canvas.place(x=200, y=100)
startt = Button(root, text="new question", command = createGame)
startt.place(x=305,y=365)
root.mainloop()
