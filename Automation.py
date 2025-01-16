import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# main window
root=tk.Tk()
root.title("Your AI Assistant")

# Adding background color
root.configure(bg='blue')

# Function to automate YouTube search
def search_youtube():
    query = entry.get()
    url=f"https://www.youtube.com/resultes?search_query={query}"
    webbrowser.open(url)

# Function to automate google search
def search_google():
    query = entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Function to automate instagram
def search_instagram():
    Username = entry.get().replace('@',"")
    url=f"https://www.instagram.com/{Username}/"
    webbrowser.open(url)

# Function to automate Twitter search
def search_twitter_X():
    query = entry.get()
    url = f"https://twitter.com/search?q={query}&src=typed_query"
    webbrowser.open(url)

# Create Input field,Labels and Buttons
Label(root,text="Enter your command below :").pack(pady=10)
entry=Entry(root,width=50)
entry.pack(pady=10)
Button(root,text="Search on YouTube",command=search_youtube).pack(pady=5)
Button(root,text="Search on google",command=search_google).pack(pady=5)
Button(root,text="Search on Instagram",command=search_instagram).pack(pady=5)
Button(root, text="Search on Twitter/X", command=search_twitter_X).pack(pady=5)

# Run the GUI event
root.mainloop()