# Quuize-Game-IN-Tkinter
A small quiz game using Python library tkinter
# Quiz Game

A desktop quiz app built with Python and Tkinter. Pick a difficulty, answer multiple-choice questions, and see your score at the end.

##Preview 📸



## Features

- Multi-page interface: Home, Difficulty, Questions, and Score screens
- Three difficulty levels: Easy, Medium, and Hard
- Questions are loaded from a JSON file, so you can add your own without touching the code
- Questions are shuffled every game
- Progress indicator (for example, "Question 3 of 10")
- Final score shown as a count and a percentage
- Play again without restarting the app
- Friendly error messages if the question file is missing or broken

## Tech stack

- Python 3
- Tkinter (included with Python)
- `json` and `random` from the standard library

No extra packages to install.

## How to run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/quiz-game.git
   cd quiz-game
   ```
3. Run the app:
   ```bash
   python main.py
   ```

Keep `questions.json` in the same folder as `quiz.py`.

## Project structure

```
quiz-game/
├── main.py            # the application
├── questions.json     # the question bank
└── README.md
```

## Adding your own questions

Open `questions.json` and add a new item to the list. Each question needs four fields:

```json
{
  "question": "What is the capital of France?",
  "options": ["Berlin", "Madrid", "Paris", "Rome"],
  "answer": "Paris",
  "difficulty": "easy"
}
```

Rules to remember:

- `difficulty` must be `easy`, `medium`, or `hard`
- `answer` must match one of the `options` exactly, including capital letters and spaces
- Each question should have 4 options

## How it works

- **Pages:** every screen is a `Frame` placed in the same grid cell. `show_page()` calls `tkraise()` to bring the chosen page to the front.
- **Answer selection:** the four `Radiobutton` widgets share one `StringVar`, so only one option can be selected at a time.
- **Filtering:** a list comprehension keeps only the questions that match the chosen difficulty.
- **State:** `global` variables track the current question number and the score. Both are reset each time a new quiz starts.
- **Reusing widgets:** the option buttons are created once, and their text is updated with `.config()` for each question.

## What I learned

- Building multi-page Tkinter apps with `Frame` and `tkraise()`
- Reading JSON data with error handling (`try` / `except` and `with`)
- Using `StringVar` with `Radiobutton`
- Passing functions to `command` and using `lambda` correctly inside loops
- Updating widgets with `.config()` instead of creating new ones
- Managing program state with global variables

## A note on how this was built

I built this project while learning Tkinter, with help from AI. I went through the code afterward, tested myself on how each part works, and made improvements on my own. I'm continuing to practice by building more projects from scratch.

## Future improvements

- [ ] Show the correct answer after each question
- [ ] Add a timer for each question
- [ ] Save and display high scores
- [ ] Add a "Back to Home" button on the questions page
- [ ] Add an in-app screen for adding new questions

## License

This project is open source and free to use for learning.
