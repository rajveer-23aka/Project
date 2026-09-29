# Project Statement: Typing Speed Tester

## 1. Problem Statement

Typing is a basic skill for students, programmers and office workers, yet most people never measure how fast or how accurately they type. Many online typing tests need an internet connection, show ads, ask for sign-ups, or use the same fixed passages, so users end up memorizing the text instead of improving their typing. They also rarely keep a simple record of progress over time.

There is a need for a small, free, offline tool that:

- gives new, random text every time so results are honest,
- lets the user decide how long the text should be,
- measures both **speed** and **accuracy**, and
- remembers past results so progress can be tracked.

This project solves that problem with a terminal-based typing speed tester written in Python.

---

## 2. Scope of the Project

### In scope

- A command-line (terminal) program with a simple numbered menu.
- Two test modes: **Sentence mode** (one sentence) and **Timed mode** (15, 30 or 60 seconds).
- Random sentences generated from a large word list, with the sentence length (3 to 25 words) chosen by the user.
- Calculation of words per minute (WPM), accuracy percentage and error count.
- Saving every result to a CSV file and showing history, best score and average score.
- Input validation and error handling so bad input never crashes the program.
- Documentation (README) for first-time Python users.

### Out of scope

- A graphical interface (windows, buttons) or a web/mobile version.
- User accounts, online leaderboards or cloud storage.
- Real-time on-screen feedback while typing (for example, coloring wrong letters live).
- Punctuation, numbers or code-typing practice.
- A hard stop of the timer in the middle of typing a sentence. Basic Python `input()` cannot be interrupted, so the time limit is checked after each sentence.

---

## 3. Target Users

- **Beginners learning Python:** the code is short, modular and commented, so it works as a readable example project.
- **Students and general users** who want to check and improve their typing speed without internet or sign-ups.
- **Teachers and evaluators** who want a small project that demonstrates functional modules, input/output handling and file storage.

No prior programming knowledge is needed to run the program, only Python installed on the computer.

---

## 4. High-Level Features

**Functional modules**

1. **Test Engine:** runs Sentence mode and Timed mode, shows a countdown and displays random sentences of the chosen length.
2. **Scoring Module:** compares what was typed with the target text and calculates WPM, accuracy and errors.
3. **History Module:** saves each result to a CSV file, and shows the last 10 tests, the personal best and the average speed.

**Input and output**

- *Input:* menu choices, test mode, time limit, sentence length and the typed text.
- *Output:* the target sentence, a results report (speed, accuracy, errors, time), a history table, and a saved CSV file you can open anytime to see all your stats.

**Workflow**

Main menu, then choose mode, then choose length, then countdown, then type, then view results, then automatic save, then back to the main menu (or view history / quit).

**Non-functional qualities**

| Quality | How it is achieved |
|---------|--------------------|
| Performance | Precise timing with `time.perf_counter()`; light calculations only |
| Usability | Simple numbered menus, countdown, clear results |
| Reliability | CSV file is created automatically the first time it is needed; results are appended safely |
| Error handling | All menu and number inputs are validated with retry loops; save errors are caught without crashing |
| Maintainability | Small single-purpose functions and settings kept as constants at the top of the file |
| Resource efficiency | Runs in the terminal using only Python's built-in modules; history is read only when requested |
