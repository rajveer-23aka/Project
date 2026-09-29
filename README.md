# Typing Speed Tester

A simple terminal game that measures how fast and how accurately you type. Written in Python, made for beginners: no complicated setup, just run it and start typing.

---

## Menu

Click any item to jump to that section.

1. [Overview](#1-overview)
2. [Features](#2-features)
3. [Technologies and Tools Used](#3-technologies-and-tools-used)
4. [Steps to Install and Run](#4-steps-to-install-and-run)
5. [How to Use the Program](#5-how-to-use-the-program)
6. [How Your Score Is Calculated](#6-how-your-score-is-calculated)
7. [Instructions for Testing](#7-instructions-for-testing)
8. [Screenshots](#8-screenshots)
9. [Project Files](#9-project-files)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. Overview

This program shows you a random sentence and times how long you take to type it. When you finish, it tells you:

- your **speed** (in WPM, words per minute)
- your **accuracy** (in %)
- how many **mistakes** you made

Every result is saved in a file, so you can check your progress later.

**Who is this for?** Anyone new to Python. The code is split into small, clearly named functions with comments, so it is easy to read and learn from.

[Back to menu](#menu)

---

## 2. Features

- **Two test modes**
  - *Sentence mode*: type one random sentence.
  - *Timed mode*: keep typing sentences for 15, 30 or 60 seconds.
- **You choose the sentence length** (3 to 25 words).
- **Random sentences every time**, built from a built-in word list.
- **Score report**: speed, accuracy, errors and time taken.
- **History**: see your last 10 tests, your best speed and your average.
- **Results saved automatically** in a CSV file, so you can check your stats anytime, even outside the program, by opening it in Excel, Google Sheets or a text editor.
- **Friendly error messages**: wrong input never crashes the program.

[Back to menu](#menu)

---

## 3. Technologies and Tools Used

| Tool | What it is used for |
|------|---------------------|
| Python 3.8 or newer | The programming language |
| `time` | Timing your typing and the countdown |
| `random` | Choosing random words for each sentence |
| `csv` | Saving and reading your results |
| `os` | Checking if the results file exists |

All of these come built into Python, so there is nothing extra to install.

[Back to menu](#menu)

---

## 4. Steps to Install and Run

### Step 1: Check that Python is installed

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```
python --version
```

You should see something like `Python 3.11.4`. If you get an error, try `python3 --version`. If that also fails, download Python from https://www.python.org/downloads/ and install it. On Windows, tick **"Add Python to PATH"** during installation.

### Step 2: Get the project

Either download the ZIP from GitHub (green **Code** button, then **Download ZIP**) and unzip it, or use git:

```
git clone <your-repository-link>
```

### Step 3: Open the project folder in your terminal

```
cd typing-speed-tester
```

(Use the real folder name if it is different.)

### Step 4: Run the program

```
python typing_speed_tester.py
```

On Mac/Linux you may need `python3` instead of `python`.

[Back to menu](#menu)

---

## 5. How to Use the Program

When the program starts you will see a main menu:

```
1. Start test
2. View history
3. Quit
```

Type the number and press **Enter**.

### Taking a test

1. Choose **1** (Start test).
2. Choose a mode:
   - **1** = Sentence mode
   - **2** = Timed mode (then choose 1 for 15s, 2 for 30s, or 3 for 60s)
3. Enter how many words you want in each sentence (between 3 and 25).
4. A countdown (3, 2, 1, GO!) appears, then a sentence is shown.
5. Type the sentence exactly as shown and press **Enter**.
6. See your results. They are saved automatically.

**Tips for Timed mode:** after each sentence you press Enter and a new one appears. The timer is checked when you press Enter, so your last sentence may finish a little after the time limit. That is normal.

### Viewing your history

Choose **2** from the main menu to see your last 10 tests, your best speed and your average speed. This same information is stored in `typing_results.csv`, so you can also open that file directly anytime, even without running the program.

### Quitting

Choose **3**, or press **Ctrl + C** at any time.

[Back to menu](#menu)

---

## 6. How Your Score Is Calculated

- **Correct characters**: letters that match the sentence in the same position.
- **WPM** = (correct characters / 5) / minutes taken. In typing tests, 5 characters count as 1 word.
- **Accuracy** = correct characters / total characters x 100.
- **Errors** = missing, extra or wrong characters.

Example: if you type a 50-character sentence perfectly in 10 seconds, your WPM is (50 / 5) / (10 / 60) = **60 WPM** with **100% accuracy**.

[Back to menu](#menu)

---

## 7. Instructions for Testing

You can check that the program works correctly by trying these tests by hand.

| # | What to do | What should happen |
|---|------------|--------------------|
| 1 | Start the program and choose `5` at the main menu | Message says the choice is invalid and asks again |
| 2 | Choose Start test, Sentence mode, then enter `abc` as the length | Message asks for a whole number |
| 3 | Enter `100` as the length | Message asks for a number between 3 and 25 |
| 4 | Enter `5` and type the sentence exactly | Accuracy is **100%** and errors is **0** |
| 5 | Take another test and type something completely different | Accuracy is low and errors is high |
| 6 | Take another test and press Enter without typing | Speed is **0**, no crash |
| 7 | Choose View history | Your tests appear in the table with a best and average speed |
| 8 | Start a test and press **Ctrl + C** | "Test cancelled" is shown, nothing is saved |
| 9 | Open `typing_results.csv` | One new row per finished test, with date, mode, WPM, accuracy, errors and seconds |

[Back to menu](#menu)

---

## 8. Screenshots

Add your own screenshots here after running the program. Save the images in a folder called `screenshots` and link them like this:

```
![Main menu](screenshots/main_menu.png)
![Test in progress](screenshots/test.png)
![Results](screenshots/results.png)
```

[Back to menu](#menu)

---

## 9. Project Files

```
typing-speed-tester/
├── typing_speed_tester.py   The whole program
├── README.md                This file
├── statement.md             Problem statement and scope
└── typing_results.csv       Created automatically after your first test
```

The program has three main parts:

1. **Test engine**: shows sentences and runs the two modes.
2. **Scoring**: calculates speed, accuracy and errors.
3. **History**: saves and reads your results from the CSV file.

[Back to menu](#menu)

---

## 10. Troubleshooting

| Problem | What to try |
|---------|-------------|
| `'python' is not recognized` | Python is not installed or not on PATH. Reinstall and tick "Add Python to PATH", or use `python3`. |
| My results are not saved | Check that the folder the program is running from is not read-only, so it is allowed to create and write `typing_results.csv`. |
| Accuracy looks very low | The comparison is position by position, so one missed letter early on can shift everything after it. Type carefully and do not skip characters. |
| I want to reset my history | Delete `typing_results.csv`. A new one is created next time. |

[Back to menu](#menu)
