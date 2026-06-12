# 🚪 Name Gatekeeper & Letter Counter

Creating my first interactive CLI tool while learning core Python concepts!

<div>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Status-Learning%20%26%20Practicing-success?style=for-the-badge" alt="Project Status" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</div>

---

## 📌 Project Overview

This is an interactive Python Command Line Interface (CLI) application. It serves as a playground for learning and mastering **input/output flow**, **loop structures**, and **error handling** in Python. 

The program acts as a "gatekeeper" that checks user permissions before offering to count the characters in the user's name.

---

## 🚀 Key Features

* **Smart Gatekeeper**: Validates usernames against a permitted guest list (`['thumbi', 'tigger']`).
* **Input Validation Loop**: Prevents invalid responses using a persistent `while True` loop.
* **Typo Recovery**: Restarts user prompts on unrecognized key presses without breaking the program.
* **Immediate Exit**: Clean execution termination via `break` statements once a valid flow completes.

---

## ⚙️ How to Run

### Prerequisites
Make sure you have **Python 3** installed on your system.

### Running the App
1. Clone this repository or download the files.
2. Open your terminal in the project directory.
3. Run the following command:

```bash
python practice.py
```

---

## 📸 Demo Session

```text
What is your name?
Atlantic Ocean
Not permitted

What is your name?
Thumbi
Do you want to know how many letters Thumbi has? (Y?N)
j
Error, try again

Do you want to know how many letters Thumbi has? (Y?N)
y
6
```

---

## 🧠 What I Learned

### 🔄 Loop Control & Flow
* **`while True:`**: How to create infinite loop gates that keep checking conditions.
* **`break` vs. `continue`**: 
  * `break` exits the loop cleanly once the goal is reached.
  * `continue` immediately jumps back to the top of the loop to try again.
* **Infinite Loop Prevention**: Placing input prompts *inside* loops to ensure state updates.

### 📐 Structural Python
* **Indentation Rules**: Using `Tab` and `Shift + Tab` in modern code editors to define blocks of code in Python.
* **Condition Operators**: Using `or` to write cleaner logic checks (`if ans == 'Y' or ans == 'y'`).

### 📦 For vs. While Loops
* **`for`**: Iterates over a known sequence (ranges, lists, strings).
* **`while`**: Repeats until a dynamic condition is met (user entering a valid key).