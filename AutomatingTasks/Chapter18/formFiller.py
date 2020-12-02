#! python3

#formFiller.py - Automatically fill out the form

import pyautogui, time

#Set the mouse coordinates
nameField = (267, 356)
submitButton = (191, 880)
submitColor = (75, 141, 249)
submitAnotherLink = (303, 229)



formData = [{'name': 'Alice', 'fear': 'eavesdropping', 'source': 'wand', 'robocop': 4, 'comments': 'tell Bob I sat hi'}, {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'}]