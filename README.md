# Text File Duplicate Analyzer & Unique Entry Extractor

**Problem Statement No. 19** | **Language:** Python 3  
**Institution:** Rungta International Skills University — School of Computer Science and Engineering

---

## Overview

The **Text File Duplicate Analyzer & Unique Entry Extractor** is a beginner-level, console-based Python 3 program that reads a text file with one entry per line, identifies duplicate entries, counts how many times each duplicate repeats, displays a summary report on the console, and writes all unique entries into a new file named `unique.txt`.

---

## Features

- **Two Comparison Modes:**
  - **Option 1 (Exact Match):** Compares entries strictly as written (after removing newline characters).
  - **Option 2 (Ignore Case & Extra Spaces):** Normalizes entries using `.strip().lower()` so variations like `Apple`, `apple`, and `APPLE` are treated as the same item.
- **Statistics & Frequency Reporting:** Displays total item count, unique item count, and repetition counts for every duplicate entry.
- **Deduplicated Output File:** Saves unique entries (one per line) into `unique.txt`.
- **Error & Edge-Case Handling:** Uses `try-except FileNotFoundError` for missing files and checks for empty input files.

---

## Concepts & Tools Used

- **Language:** Python 3 (Standard Library only — no external packages required)
- **Core Concepts:** Lists, Sets, Dictionaries, Loops, Conditional Statements, File Handling, and `try-except`
- 
