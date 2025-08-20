# 📚 Bookbot

**Bookbot** is a simple command-line Python program that analyzes a `.txt` book and provides insights into its content — including total word count and frequency of each character used.

## 🧰 Tech Stack

- **Python 3.8+**
- Standard Python libraries only (no external dependencies)

## ⚙️ How It Works

When you run `bookbot`, it does the following:

1. Reads the contents of a plain text file (e.g., `frankenstein.txt`)
2. Cleans and processes the text
3. Calculates:
   - Total number of words
   - Frequency of each character (case-insensitive)
4. Outputs the results neatly in your terminal

Example output:
```
Analyzing book found at books/frankenstein.txt...

Found 75767 total words
Character Count
---------------

e: 44538
t: 29493
a: 25894
...
```

## 🖥️ How to Use

You can use `bookbot` on any system with Python installed. Follow these steps:

### Option 1: Using Git (if installed)

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/bookbot.git
   cd bookbot
   ```

2. **Run the program**

   ```bash
   uv run main.py books/frankenstein.txt
   ```

### Option 2: Without Git

1. **Download the ZIP file**

   * Click the green **"Code"** button > **Download ZIP**
   * Extract the folder to your desired location

2. **Navigate into the folder**

   ```bash
   cd path/to/bookbot
   ```

3. **Run the program**

   ```bash
   python main.py books/frankenstein.txt
   ```

## 📝 Notes

* Works with any plain `.txt` book file — just replace `books/frankenstein.txt` with your own.
* Make sure you have Python installed. Check using:

  ```bash
  python --version
  ```


## 🚀 Future Improvements

* Add support for visualizing statistics
* Export results to a file
* Add word frequency analysis

Happy reading with **Bookbot**! 🧠📖