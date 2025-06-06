import json
import os

FILENAME = "slambook.json"

questions = [
    "What is your name?",
    "What's your nickname?",
    "What's your favorite color?",
    "Your best memory with me?",
    "One word to describe me?",
    "Your favorite song?",
    "Your dream job?",
    "A message for me:"
]

def load_entries():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_entries(entries):
    with open(FILENAME, 'w') as file:
        json.dump(entries, file, indent=4)

def add_entry():
    print("\n--- Fill Out the Slambook ---")
    entry = {}
    for question in questions:
        answer = input(question + " ")
        entry[question] = answer
    entries.append(entry)
    save_entries(entries)
    print("Thanks! Your entry has been saved.\n")

def view_entries():
    if not entries:
        print("\nNo entries found.\n")
        return
    print("\n--- All Slambook Entries ---")
    for i, entry in enumerate(e
