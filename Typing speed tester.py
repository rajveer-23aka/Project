import csv
import os
import random
import time

# ---------- Settings (all in one place) ----------
RESULTS_FILE = "typing_results.csv"
MIN_WORDS = 3
MAX_WORDS = 25

WORD_LIST = [
    "time", "code", "python", "simple", "practice", "keyboard", "quick",
    "screen", "logic", "function", "variable", "loop", "system", "typing",
    "speed", "learn", "build", "test", "error", "data", "file", "input",
    "output", "small", "clear", "focus", "steady", "improve", "daily",
    "program", "result", "accuracy", "player", "random", "word", "sentence",
    "fast", "smooth", "careful", "review", "skill", "brain", "hands",
    "rhythm", "pattern", "memory", "design", "module", "debug", "count",
]


# ---------- Building a random sentence ----------
def generate_sentence(word_count):
    chosen_words = []
    for i in range(word_count):
        word = random.choice(WORD_LIST)
        chosen_words.append(word)

    sentence = " ".join(chosen_words)
    # Make the first letter capital and add a full stop at the end
    sentence = sentence[0].upper() + sentence[1:] + "."
    return sentence


# ---------- Scoring ----------
def count_correct_letters(target, typed):
    correct = 0
    shortest_length = min(len(target), len(typed))
    for i in range(shortest_length):
        if target[i] == typed[i]:
            correct = correct + 1
    return correct


def calculate_results(target, typed, seconds):
    if seconds <= 0 or target == "":
        return {"wpm": 0, "accuracy": 0, "errors": len(target)}

    correct = count_correct_letters(target, typed)
    longer_length = max(len(target), len(typed))
    errors = longer_length - correct

    minutes = seconds / 60
    wpm = (correct / 5) / minutes
    accuracy = (correct / longer_length) * 100

    results = {
        "wpm": round(wpm, 1),
        "accuracy": round(accuracy, 1),
        "errors": errors,
    }
    return results


# ---------- Saving and loading results ----------
def make_results_file_if_missing():
    if os.path.exists(RESULTS_FILE) == False:
        new_file = open(RESULTS_FILE, "w", newline="")
        writer = csv.writer(new_file)
        writer.writerow(["date", "mode", "wpm", "accuracy", "errors", "seconds"])
        new_file.close()


def save_result(mode, results, seconds):
    make_results_file_if_missing()
    current_time = time.strftime("%Y-%m-%d %H:%M")

    try:
        results_file = open(RESULTS_FILE, "a", newline="")
        writer = csv.writer(results_file)
        writer.writerow([current_time, mode, results["wpm"], results["accuracy"],
                          results["errors"], round(seconds, 1)])
        results_file.close()
        print("Result saved. You can open", RESULTS_FILE, "to see all your stats.")
    except:
        print("Sorry, the result could not be saved.")


def show_history():
    make_results_file_if_missing()

    results_file = open(RESULTS_FILE, "r", newline="")
    reader = csv.reader(results_file)

    all_rows = []
    for row in reader:
        all_rows.append(row)
    results_file.close()

    data_rows = all_rows[1:]

    if len(data_rows) == 0:
        print("\nNo results yet. Take a test first!")
        return

    print("\n--- Last 10 results ---")
    print("Date              Mode          WPM   Accuracy   Errors")

    # Only show the last 10 rows
    last_ten = data_rows[-10:]
    for row in last_ten:
        date = row[0]
        mode = row[1]
        wpm = row[2]
        accuracy = row[3]
        errors = row[4]
        print(date + "   " + mode + "   " + wpm + "   " + accuracy + "   " + errors)

    # Find the best wpm and the average wpm
    best_wpm = 0
    best_date = ""
    total_wpm = 0

    for row in data_rows:
        row_wpm = float(row[2])
        total_wpm = total_wpm + row_wpm
        if row_wpm > best_wpm:
            best_wpm = row_wpm
            best_date = row[0]

    average_wpm = total_wpm / len(data_rows)

    print("\nBest speed so far:", best_wpm, "WPM on", best_date)
    print("Average speed:", round(average_wpm, 1), "WPM over", len(data_rows), "tests")
    print("(All of this is stored in", RESULTS_FILE, "- open it anytime.)")


# ---------- Getting input from the user safely ----------
def get_choice(question, valid_choices):
    while True:
        answer = input(question)
        answer = answer.strip()
        if answer in valid_choices:
            return answer
        print("That is not a valid choice. Please try again.")


def get_sentence_length():
    while True:
        answer = input("How many words should the sentence have (3-25)? ")
        if answer.isdigit() == False:
            print("Please type a whole number.")
            continue

        number = int(answer)
        if number >= MIN_WORDS and number <= MAX_WORDS:
            return number
        else:
            print("Please choose a number between 3 and 25.")


def countdown():
    print("\nGet ready...")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("GO!\n")


# ---------- The two test modes ----------
def run_sentence_mode(length):
    target = generate_sentence(length)

    countdown()
    start_time = time.perf_counter()
    print(target)
    typed = input("> ")
    end_time = time.perf_counter()

    seconds = end_time - start_time
    results = calculate_results(target, typed, seconds)
    return "sentence", results, seconds


def run_timed_mode(limit, length):
    all_targets = ""
    all_typed = ""

    countdown()
    start_time = time.perf_counter()

    while True:
        elapsed = time.perf_counter() - start_time
        if elapsed >= limit:
            break

        sentence = generate_sentence(length)
        print(sentence)
        typed = input("> ")

        all_targets = all_targets + sentence + " "
        all_typed = all_typed + typed + " "

    end_time = time.perf_counter()
    seconds = end_time - start_time

    results = calculate_results(all_targets, all_typed, seconds)
    mode_name = "timed-" + str(limit) + "s"
    return mode_name, results, seconds


def show_results(results, seconds):
    print("\n===== RESULTS =====")
    print("Speed:", results["wpm"], "WPM")
    print("Accuracy:", results["accuracy"], "%")
    print("Errors:", results["errors"])
    print("Time taken:", round(seconds, 1), "seconds")
    print("====================")


# ---------- Starting a test ----------
def start_test():
    print("\n1. Sentence mode (type one random sentence)")
    print("2. Timed mode (type until time runs out)")
    mode = get_choice("Choose mode (1 or 2): ", ["1", "2"])

    length = get_sentence_length()

    if mode == "1":
        mode_name, results, seconds = run_sentence_mode(length)
    else:
        print("\nChoose a time limit:")
        print("1. 15 seconds")
        print("2. 30 seconds")
        print("3. 60 seconds")
        time_choice = get_choice("Choose (1, 2 or 3): ", ["1", "2", "3"])

        if time_choice == "1":
            limit = 15
        elif time_choice == "2":
            limit = 30
        else:
            limit = 60

        mode_name, results, seconds = run_timed_mode(limit, length)

    show_results(results, seconds)
    save_result(mode_name, results, seconds)


# ---------- Main program ----------
def main():
    print("=== TYPING SPEED TESTER ===")

    while True:
        print("\n1. Start test")
        print("2. View history")
        print("3. Quit")
        choice = get_choice("Choose (1, 2 or 3): ", ["1", "2", "3"])

        if choice == "1":
            start_test()
        elif choice == "2":
            show_history()
        else:
            print("Goodbye!")
            break


main()