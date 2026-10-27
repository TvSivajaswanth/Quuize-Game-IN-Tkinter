from tkinter import*
import json 
import random
from tkinter import messagebox
root = Tk()

container = Frame(root)
container.pack(fill = "both", expand=True)


home_page = Frame(container)
difficulty_page = Frame(container)
questions_page = Frame(container)
score_page = Frame(container)


pages = [
    home_page,
    difficulty_page,
    questions_page,
    score_page
]


for page in pages:
    page.grid(row=0,column=0,sticky="nsew")
    
def show_page(page):
    page.tkraise()
    
def load_data():
    try:
        with open("qustions.json","r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [
            messagebox.showerror(
                        "Error",
                        "Could not load qustions.json"
                    )
        ]

   
all_questions = load_data()
quiz_questions = []
current_question = 0
score = 0
selected_answer = StringVar(value="")
# --------Home Page-----------
Label(
    home_page,
    text="Welcome to Quiz Game!",
    font=("Arial", 22, "bold")
).pack(pady=35)


Label(
    home_page,
    text="Test your knowledge!",
    font=("Arial", 13)
).pack(pady=10)

Button(
    home_page,
    text="Start Quiz",
    width=20,
    height=2,
    command=lambda: show_page(difficulty_page)
).pack(pady=15)

Button(
    home_page,
    text="Exit",
    width=20,
    command=root.quit
).pack(pady=5)

# ---------------- DIFFICULTY PAGE ----------------
Label(
    difficulty_page,
    text="Choose Difficulty",
    font=("Arial", 20, "bold")
).pack(pady=30)

def start_quize(level):
    global quiz_questions, current_question, score
    
    quiz_questions = [
        q for q in all_questions
        if q.get("difficulty","").lower() == level
    ]
    if not quiz_questions:
        messagebox.showwarning(
            "No Questions",
            f"No questions found for {level} difficulty."
        )
        return
    
    random.shuffle(quiz_questions)
    current_question = 0
    score = 0
    show_page(questions_page)
    display_qustions()
    
    
for level in ["easy","medium","hard"]:
    
    Button(
        difficulty_page,
        text=level.capitalize(),
         width=20,
        height=2,
        command=lambda l = level:start_quize(l)
    ).pack(pady=10)


Button(
    difficulty_page,
    text="Back",
    command=lambda: show_page(home_page)
).pack(pady=10)
# ---------------- QUESTIONS PAGE ----------------

question_label = Label(
    questions_page,
    text="",
    font=("Arial", 16, "bold")
)

question_label.pack(pady=25, padx=20)

progress_label = Label(
    questions_page,
    text="",
    font=("Arial", 11)
)
progress_label.pack(pady=5)


options_frame = Frame(questions_page)
options_frame.pack(pady=10)

option_buttons = []

for i in range(4):
    
    rb = Radiobutton(
        options_frame,
        text="",
        variable=selected_answer,
        value="",
        font=("Arial", 12),
        anchor="w",
        wraplength=450
    )
    rb.pack(anchor="w", pady=5)
    option_buttons.append(rb)
    
def display_qustions():
    selected_answer.set("")
    
    q = quiz_questions[current_question]
    question_label.config(text=q["question"])
    progress_label.config(
       text = f"Question {current_question + 1} of {len(quiz_questions)}"
    )
    for i, op in enumerate(q["options"]):
        option_buttons[i].config(
            text = op,
            value = op,
            state = NORMAL
        )
def submit_answer():
    global current_question,score
    
    
    user_answer = selected_answer.get()
    
    if not user_answer:
            messagebox.showwarning(
                "Choose an answer",
                "Please select an option first."
            )
            return
    answer = quiz_questions[current_question]["answer"]
    
    
    if answer == user_answer:
        display_answer.config(text=f"You are currect {answer}!")
        score+=1
    else:    
       display_answer.config(text= f"Worng the answer is {answer}!")
    current_question+=1    
    
    if current_question < len(quiz_questions):
        display_qustions()
    else:
        show_score()    
    
display_answer = Label(questions_page,text="",font=("Arial",10,"bold"))
display_answer.pack(pady=10)
Button(
    questions_page,
    text="Next",
    width=15,
    height=2,
    command=submit_answer
).pack(pady=15)

# ---------------- SCORE PAGE ----------------
Label(
    score_page,
    text="Quiz Completed!",
    font=("Arial", 22, "bold")
).pack(pady=35)

score_label = Label(
    score_page,
    text="",
    font=("Arial", 18)
)
score_label.pack(pady=15)
    
def show_score():
    
    total = len(quiz_questions)
    percentage = (score / total) * 100 if total else 0
    
    score_label.config(
        
        text=f"Your score: {score}/{total}\n Percentage: {percentage:.1f}%"
    )
    
    show_page(score_page)
    
Button(
    score_page,
    text="Play Again",
    width=20,
    height=2,
    command=lambda: show_page(difficulty_page)
).pack(pady=10)

Button(
    score_page,
    text="Home",
    width=20,
    command=lambda: show_page(home_page)
).pack(pady=5)

Button(
    score_page,
    text="Exit",
    width=20,
    command=root.quit
).pack(pady=5)

show_page(home_page)
root.mainloop()