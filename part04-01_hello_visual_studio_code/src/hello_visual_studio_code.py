# Write your solution here
while True:
    editor=input("Editor:")
    editor=editor.lower()
    if editor=="emacs" or editor== "atom" or editor== "vim":
        print("not good")
    if editor=="word" or editor=="notepad":
        print("awful")
    if editor=="visual studio code":
        print("an excellent choice!")
        break