# Text File Duplicate Analyzer & Unique Entry Extractor

A beginner-friendly, console-based Python 3 utility developed for **Problem Statement No. 19** (Bachelor of Technology in Computer Science and Engineering — Rungta International Skills University).

This tool reads a plain text file containing one entry per line, identifies duplicate records, calculates exact repetition frequencies, prints a clear summary report in the console, and exports all deduplicated entries to `unique.txt`.

---

## Features

* **Two Comparison Modes:**
  * **Option 1 (Exact Match):** Compares lines strictly as written (case-sensitive).
  * **Option 2 (Ignore Case & Extra Spaces):** Strips leading/trailing whitespace and converts text to lowercase before comparing (e.g., `Apple`, `apple`, and `APPLE` are treated as the same entry).
* **Frequency Reporting:** Displays total items, unique items, and the exact repetition count for each duplicate entry.
* **Clean Export:** Saves the unique entries (preserving original order) into `unique.txt`.
* **Safe Error Handling:** Gracefully handles non-existent files using `try-except FileNotFoundError` and checks for empty files without crashing.
* **Zero External Dependencies:** Built using only Python 3's standard library (`lists`, `sets`, `loops`, `dictionaries`, and built-in file I/O).

---

## Project Structure

```text
python-duplicate-analyzer/
├── duplicate_analyzer.py                            # Main beginner-level Python 3 script
├── data.txt                                         # Sample input text file
├── unique.txt                                       # Generated output file with unique entries
├── Text_File_Duplicate_Analyzer_Project_Report.docx # Project synopsis & report
├── Text_File_Duplicate_Analyzer_Presentation.pptx   # 6-slide project presentation
└── README.md                                        # Project documentation
```

---

## Requirements

* **Python 3.8 or higher**
* Any terminal / command prompt (Windows Command Prompt, PowerShell, Linux/macOS Terminal, or mobile Python IDE)

---

## How to Run

1. **Clone or download** this repository to your device.
2. Ensure you have an input text file (such as `data.txt`) in the same folder with one entry per line:
   ```text
   apple
   banana
   apple
   orange
   banana
   apple
   ```
3. Run the Python script from your terminal:
   ```bash
   python duplicate_analyzer.py
   ```
4. Enter the input file name when prompted (or press **Enter** to use the default `data.txt`), then select **Option 1** or **Option 2**.

---

## Test Cases & Sample Output

### Test Case 1: Normal Input (Option 1 — Exact Match)
* **Input (`data.txt`):** `apple`, `banana`, `apple`, `orange`, `banana`, `apple`
* **Console Output:**
  ```text
  Total items: 6 | Unique items: 3
  Duplicates: apple (3 times) | banana (2 times)
  Unique list saved to unique.txt
  ```

### Test Case 2: Boundary / Single Entry (Option 1)
* **Input (`data.txt`):** `apple`
* **Console Output:**
  ```text
  Total items: 1 | Unique items: 1
  No duplicates found.
  ```

### Test Case 3: Invalid / Empty File Handling
* **Missing File (`dta.txt`):** `File 'dta.txt' not found. Please enter a valid file name.`
* **Empty File (`0 lines`):** `File is empty. Nothing to check.`

### Test Case 4: Case-Insensitive Comparison (Option 2)
* **Input (`data.txt`):** `Apple`, `apple`, `banana`, `APPLE`
* **Console Output:**
  ```text
  Total items: 4 | Unique items: 2
  Duplicates: apple (3 times)
  Unique list saved to unique.txt
  ```

---

## Author

* **Name:** [Your Name]
* **Roll No.:** [Your Roll Number]
* **Department:** School of Computer Science and Engineering, Rungta International Skills University