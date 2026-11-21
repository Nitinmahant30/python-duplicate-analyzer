# Beginner-Level Python 3 Program: Text File Duplicate Analyzer & Unique Entry Extractor
# Problem Statement No. 19

def read_entries(filename):
    """Reads lines from a text file and handles missing file errors."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return None


def prepare_entries(raw_lines, mode):
    """Prepares entries based on Option 1 (Exact match) or Option 2 (Ignore case & spaces)."""
    cleaned_entries = []

    for line in raw_lines:
        if mode == "1":
            # Keep exact text, only removing newline characters at the end
            entry = line.rstrip("\r\n")
        else:
            # Ignore case and extra leading/trailing spaces
            entry = line.strip().lower()

        if entry != "":
            cleaned_entries.append(entry)

    return cleaned_entries


def find_unique_and_duplicates(entries):
    """Finds unique entries (preserving order) and counts duplicate occurrences."""
    unique_list = []
    seen = set()

    # Use a set to track unique entries without losing order
    for item in entries:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)

    # Count how many times each item appears using loops
    duplicates = {}
    for unique_item in unique_list:
        count = 0
        for entry in entries:
            if entry == unique_item:
                count += 1
        if count > 1:
            duplicates[unique_item] = count

    return unique_list, duplicates


def save_unique_entries(unique_list, output_filename="unique.txt"):
    """Writes unique entries to unique.txt, one entry per line."""
    with open(output_filename, "w", encoding="utf-8") as out_file:
        for item in unique_list:
            out_file.write(item + "\n")


def main():
    print("=== Text File Duplicate Analyzer & Unique Entry Extractor ===")
    filename = input("Enter file name (default: data.txt): ").strip()
    if filename == "":
        filename = "data.txt"

    raw_lines = read_entries(filename)
    if raw_lines is None:
        return

    print("\nChoose an option:")
    print("1. Exact match")
    print("2. Ignore case and extra spaces")
    mode = input("Enter option (1 or 2): ").strip()

    if mode not in ("1", "2"):
        print("Invalid option. Defaulting to Option 1 (Exact match).")
        mode = "1"

    entries = prepare_entries(raw_lines, mode)

    if len(entries) == 0:
        print("File is empty. Nothing to check.")
        return

    unique_list, duplicates = find_unique_and_duplicates(entries)

    print(f"\nTotal items: {len(entries)} | Unique items: {len(unique_list)}")

    if len(duplicates) == 0:
        print("No duplicates found.")
    else:
        dup_summary = [f"{item} ({count} times)" for item, count in duplicates.items()]
        print("Duplicates: " + " | ".join(dup_summary))
        save_unique_entries(unique_list, "unique.txt")
        print("Unique list saved to unique.txt")


if __name__ == "__main__":
    main()
          
