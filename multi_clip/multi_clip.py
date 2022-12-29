import sys
import pyperclip
import json

if len(sys.argv) == 2:
    command = sys.argv[1]
    contents = {}
    try:
        with open("clipboard.json", 'r') as openfile:
            contents = json.load(openfile)
    except FileNotFoundError:
        print("Nothing on clipboard yet.")

    # save a new clipboard element with a specific key
    if command == "save":
        key = input("Enter a key to save this data under: ")
        data = pyperclip.paste()  # data which is currently on clipboard
        contents[key] = data
        print("Data saved.")

    # load -> load an element which is stored in contents to clipboard, by entering a key as a second command line argument
    if command == "load":
        key = input("Enter the key to load the data from: ")
        pyperclip.copy(contents[key])
        print("Data copied to clipboard.")

    # list -> list current data
    if command == "list":
        print(contents)

    # Save the data im json file
    json_object = json.dumps(contents, indent=4)
    with open("clipboard.json", "w") as outfile:
        outfile.write(json_object)
else:
    print("You can only enter one command: (save/load/list).")
