from tkinter import Tk, StringVar
from ttkthemes import ThemedTk
from tkinter import ttk
import random

window = ThemedTk(theme="ubuntu")
window.title("Type Game")
#window.configure(themebg = "ubuntu")
window.geometry("700x300")
window.resizable(False, False)
phrases = [
    "The sun sets behind the hills",
    "She walked quietly through the forest",
    "A dog barked in the distance",
    "Rain fell softly on the roof",
    "They waited patiently at the station",
    "The book lay open on table",
    "Birds flew across the morning sky",
    "He smiled and closed the door",
    "The wind whispered through the trees",
    "Lights flickered in the empty hallway","The old man whispered a secret",
    "Shadows danced across the broken pavement",
    "She carefully folded the torn letter",
    "The engine roared through the silent valley",
    "Raindrops tapped gently on the windowpane",
    "He vanished without leaving a single trace",
    "The candle flickered in the cold breeze",
    "Footsteps echoed down the empty corridor",
    "She stared at the unreadable handwriting",
    "The suitcase lay forgotten under the stairs",
    "Leaves rustled beneath their hurried footsteps",
    "The clock ticked louder than usual tonight",
    "He scribbled notes in the dusty journal",
    "The mirror reflected a strange expression",
    "She locked the door and exhaled slowly",
    "The wind carried whispers from the forest",
    "He paused before crossing the icy bridge",
    "The photograph faded under the harsh sunlight",
    "She traced the map with trembling fingers",
    "The room smelled faintly of old books"
]
style =ttk.Style()
style.theme_use("clam")
score = 0
def startGame(event):
    nextPhrase()

def nextPhrase():
    global score
    current_phrase = label_phrase.cget("text")
    if entry.get() == current_phrase:
        score += 1
        label_score.config(text="Score: " + str(score))
    entry.delete(0, 'end')
    new_phrase = random.choice(phrases)
    label_phrase.config(text=new_phrase)


label_title = ttk.Label(window, text="Type The Text Given")
label_title.pack(pady=10)

label_score = ttk.Label(window, text="Press Enter to start")
label_score.pack()

label_phrase = ttk.Label(window, text="", font=('Helvetica', 16), wraplength=450, justify="center")
label_phrase.pack(pady=20)

entry = ttk.Entry(window, width=50, font=('Helvetica', 12))
entry.pack()
entry.focus_set()


window.bind('<Return>', startGame)
window.mainloop()