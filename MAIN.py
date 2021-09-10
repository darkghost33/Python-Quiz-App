from tkinter import *
import random

root = Tk()

root.title("OBJECTIVE | MCQ QUIZ 2020")
root.iconbitmap("quiz_icon.ico")
root.geometry("700x600")
root.config(background="light blue")
root.resizable(0,0)
img1 = PhotoImage(file="python_name.png")
img2 = PhotoImage(file="python.png")
img3 = PhotoImage(file="submit_img.png")
img4 = PhotoImage(file="start_btn.png")

#Questions of the quiz are stored here
questions = [
    "• What is the output for -\n\n'you are doing well'[2:999]",
    "• What is output for −\n\nb = [11,13,15,17,19,21]\nprint(b[::2])",
    "• For tuples and list which is correct?",
    "• What is output for − \nmin(''hello world'')",
    "• What is output of the following code −\n\nl = [1,2,6,5,7,8]\nl.insert(9)",
    "• What is the output?\ni = 2\nwhile True:\n  if i%3 == 0:\n  break\nprint(i)\ni += 2",
    "• Analyze the code −\n\nprint(''Recursive Function'')\ndef factorial(n):\n         return(n*factorial(n-1))\nfactorial(4)",
    "• What is the output of the following code?\n\na = lambda x,y : x+y\nprint(a(5, 6))",
    "• How are lambda functions useful?",
    "• What is the value of a, b, c in the given below code?\n\na, b = c = 2 + 2, ''TutorialsPoint''",
    ]

#Options of the questions are stored in an array
choice = [
    ["A) 'you are doing well'","B) ' '","C) Index error.","D) 'u are doing well'"],
    ["A) [19,21]","B) [11,15]","C) [11,15,19]","D) [13,17,21]"],
    ["A) List and tuples both are mutable.","B) List is mutable whereas tuples are immutable.","C) List and tuples both are immutable.","D) List is immutable whereas tuples are mutable."],
    ["A) e","B) a blank space character","C) w","D) None of the above."],
    ["A) l=[9,1,2,6,5,7,8]","B) l=[1,2,6,5,9.7,8] (insert randomly at any position)","C) l=[1,2,6,5,7,8,9]","D) Type Error"],
    ["A) 2 4 6 8 10 …","B) 2 4","C) 2 3","D) error"],
    ["A) Recursive Function 24.","B) Recursive Function.","C) Function runs infinitely and causes a StackOverflowError.","D) Syntax Error."],
    ["A) 5","B) 11","C) 6","D) 1"],
    ["A) They are useful in allowing quick calculations or processing as the input to other functions","B) Lambda functions makes it difficult to read the code","C) They can be useful as quick, throwaway single line function","D) Lambda functions are used for functional programming"],
    ["A) a=4, 'TutorialsPoint' , b= 4, 'TutorialsPoint' , c= 4, 'TutorialsPoint'","B) a=2 , b= 'TutorialsPoint' , c=4, 'TutorialsPoint'","C) a=4 , b= 'TutorialsPoint' , c=4, 'TutorialsPoint'","D) a=4 , b= 'TutorialsPoint' , c= NULL."],

    ]

#The correct answers are stored here
answers = [3,2,1,1,3,1,2,1,3,2]

#User answer will be stored here
user_answer = []

#To generate random question index
indexes = []

ques = 1

#The first page of the app
def login():
    
    global L1, E1, L2, E2, submit_btn, f, f_img

    f = LabelFrame(root,
                   text="LOGIN",
                   background="orange",
                   font=("Comic sans MS",16,"bold"),
                   padx=120,

                   )
    f.pack(pady=(20,0))

    f_img = Label(f,
                   image=img1,
                   background="orange")
    f_img.pack(pady=(0,20))

    L1 = Label(f,
               text="User Name",
               background="orange",
               font=("Comic sans MS",12,"bold")
               )
    L1.pack(pady=(0,5))
    E1 = Entry(f, bd =5)
    E1.pack()

    L2 = Label(f, text="College Name",
               background="orange",
               font=("Comic sans MS", 12, "bold")
               )
    L2.pack(pady=(15,5))
    E2 = Entry(f, bd=5 )
    E2.pack()

    submit_btn = Button(f,
                      text="Submit",
                      image=img3,
                      #relief=FLAT,
                      border=5,
                      font=("Times", 16, "bold"),
                      background="grey",
                      activebackground="orange",
                      command=submit_btn_pressed      #Pressing the button will call this function
                      )
    submit_btn.pack(pady=(30,20))

#Every time we will clear the screen then add new things to it
def submit_btn_pressed():
    global username, college
    username = E1.get()         #Storing the username for the result screen
    college = E2.get()          #Storing the college for the result screen
    L1.destroy()
    E1.destroy()
    L2.destroy()
    E2.destroy()
    f.destroy()
    f_img.destroy()
    submit_btn.destroy()
    post_login()

#The start page of the app
def post_login():

    global l_logo, l_text, start_btn, l_ins, l_rules

    # Python logo
    l_logo=Label(root,
              image=img2,
              background="light blue")
    l_logo.pack(pady=(40,0))

    #Objective | MCQ Quiz 2020 label
    l_text=Label(root,text="Objective | MCQ Quiz 2020",
               font=("Comic sans MS",24,"bold"),
               background="light blue")
    l_text.pack(pady=(0,50))

    #Start Button
    start_btn= Button(root,
                   image= img4,
                   border=8,
                      background="blue",
                   command = start_btn_pressed      #Pressing the button will call this function
                   )
    start_btn.pack()

    #Instructions
    l_ins =Label(root,
                 text="Read The Rules Given Below And\nClick Start Once You Are Ready",
                 font=("Consolas",14),
                 background="red",
                 foreground="yellow",
                 justify="center")
    l_ins.pack(pady=(10,10))

    #Rules
    l_rules = Label(root,
                    text="This quiz contains 10 questions of PYTHON\nOnce you select an option that will be your FINAL CHOICE\nTherefore think CAREFULLY before you SELECT",
                    font=("Times",14),
                    width=100,
                    background="black",
                    foreground="yellow",
                    justify="center")
    l_rules.pack(pady=(110,0))

    
def start_btn_pressed():
    
    l_logo.destroy()
    l_text.destroy()
    l_ins.destroy()
    l_rules.destroy()
    start_btn.destroy()
    ques_generator()
    quiz_start()

#Here random numbers will be generated and stored in indexes[]
def ques_generator():

    global indexes

    while (len(indexes) < 10):
        x = random.randint(0, 9)
        if x in indexes:                #If else block is used here to prevent repetition of questions
            continue
        else:
            indexes.append(x)


#In the starting of the quiz_start() we will simply show the first question as it is ,
# then we will update further questions in selected()
def quiz_start():

    global f2, no_of_question, l_question, r1, r2, r3, r4

    f2 = LabelFrame(root,
                    text="Questions",
                    background="#92f7c2",
                    font=("Times New Roman", 16, "bold"),
                    )
    f2.pack(pady=(20, 0))

    no_of_question = Label(
        f2,
        text="Question 1 out of 10",
        font=("Consolas", 12, "bold", "italic"),
        width=500,
        wraplength=400,
        background="#8ad8f9"
    )
    no_of_question.pack(pady=10)


    l_question = Label(
        f2,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        # width = 500,
        # justify = "center",
        wraplength=400,
        background="Green"
    )
    l_question.pack(pady=(20, 30), padx=20, anchor=W)

    global r
    r = IntVar()
    r.set(-1)           #To keep the radio button unselected at starting

    r1 = Radiobutton(
        f2,
        text=choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=r,
        command=selected,
        background="light blue",
        activeforeground="white",
        activebackground="blue"
    )
    r1.pack(pady=5, anchor=W)

    r2 = Radiobutton(
        f2,
        text=choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=r,
        command=selected,
        background="light blue",
        activeforeground="red",
        activebackground="blue"
    )
    r2.pack(pady=5, anchor=W)

    r3 = Radiobutton(
        f2,
        text=choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=r,
        command=selected,
        background="light blue",
        activeforeground="red",
        activebackground="blue"
    )
    r3.pack(pady=5, anchor=W)

    r4 = Radiobutton(
        f2,
        text=choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=r,
        command=selected,
        background="light blue",
        activeforeground="red",
        activebackground="blue"
    )
    r4.pack(pady=(5, 100), anchor=W)


def selected():

    global r, l_question, r1, r2, r3, r4, ques
    x = r.get()
    user_answer.append(x)           #Adding the user selected answer to user_answer[]


    #If else is use to check whether the remaining 9 questions are displayed or not completely
    if ques < 10:

        no_of_question.config(text="Question " + str(ques+1) + " out of 10")
        l_question.config(text=questions[indexes[ques]])
        r1.config(text=choice[indexes[ques]][0])
        r2["text"] = choice[indexes[ques]][1]
        r3["text"] = choice[indexes[ques]][2]
        r4["text"] = choice[indexes[ques]][3]

        ques += 1

    else:

        calculate()

#Here we calculate the score by mathing the user_answer[] to the answers[]
def calculate():

    global indexes, user_answer, answers

    x = 0
    score = 0
    for i in indexes:  #0,9
        if user_answer[x] == answers[i]:
            score = score+5
        x = x + 1

    showresult(score)


def showresult(score):

    no_of_question.destroy()
    l_question.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    f2.destroy()

    rf = LabelFrame(root,
                    text="RESULT",
                    background="#92f7c2",
                    font=("Times New Roman", 16, "bold"),
                    padx =150,
                    pady=40
                    )
    rf.pack(pady=(40,0))

    a=(score/50)*100
    r9 = LabelFrame(root,
                    text="Average is - " + str(score),
                    background="#92f7c2",
                    font=("Times New Roman", 16, "bold"),
                    padx=150,
                    pady=40
                    )
    r9.pack(pady=(40, 0))

    congrats = Label(
        rf, text="Thank You For Taking This Quiz",
        font=("Consolas", 18, "bold",),
        padx=80,
        background="#92f7c2",
        justify="center")
    congrats.pack(pady=(20, 40))

    l_result = Label(
        rf,text = username+" of "+college+ " college,\n\nYour SCORE is = "+str(score)+" out of 50",
        font=("Consolas",14,"bold","italic"),
        background="#f5fb62",
        justify = "center")
    l_result.pack(padx=5,pady=(20,50))

    
login()
root.mainloop()







