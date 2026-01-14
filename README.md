🧠 TypeTest — A Typing Speed Game in Tkinter
TypeTest is a simple yet engaging typing speed game built with Python's tkinter and ttkthemes. It challenges users to type randomly displayed phrases as quickly and accurately as possible, tracking their score in real time.
🎮 Features
- 📝 Random phrase generation from a curated list of 30 descriptive sentences
- ⌨️ Real-time input validation and score tracking
- 🎨 Themed GUI using ttkthemes with Ubuntu styling
- 📏 Fixed-size window for consistent layout
- 🐍 Built entirely in Python with no external dependencies beyond ttkthemes
🚀 How to Run
- Install dependencies:
pip install ttkthemes
- Run the game:
python TypeTest.py
- Play:
- Press Enter to start.
- Type the phrase shown and press Enter again.
- Score increases for each correct match.
🧩 Code Structure
- phrases: A list of predefined sentences used for typing challenges.
- startGame(event): Starts the game when Enter is pressed.
- nextPhrase(): Validates input, updates score, and shows a new phrase.
- GUI elements:
- label_title: Game title
- label_score: Score display
- label_phrase: Phrase to type
- entry: Input field
📸 Screenshot
You can include a screenshot of the game interface here to showcase the layout.
🛠️ Requirements
- Python 3.x
- ttkthemes
- tkinter (comes pre-installed with Python)
