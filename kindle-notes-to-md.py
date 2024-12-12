import sys
import pathlib


def parse_kindle_notes(input_file):
    with open(input_file, "r") as file:
        lines = [x.strip() for x in file.readlines()]
    notes_dict = {}
    current_book = None
    current_notes = []

    current_index = 0
    while True:
        current_book = lines[current_index]
        if current_book not in notes_dict:
            notes_dict[current_book] = []
        current_notes = []
        current_index += 2
        while current_index < len(lines) and lines[current_index] != "==========":
            if lines[current_index]:
                current_notes.append(lines[current_index])
            current_index += 1
        notes_dict[current_book] += current_notes
        current_index += 1
        if current_index >= len(lines):
            break

    pathlib.Path("notes").mkdir(exist_ok=True)
    for book, notes in notes_dict.items():
        file_name = f"{book.replace(' ', '_')}.md"
        with open(f"notes/{file_name}", "w") as md_file:
            md_file.write(f"# {book}\n\n")
            md_file.write("\n\n".join(notes))


print("reading " + sys.argv[1])
parse_kindle_notes(sys.argv[1])
