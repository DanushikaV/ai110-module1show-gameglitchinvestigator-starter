# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game lets the player guess a secret number and gives hints until the correct number is guessed within certain attempts.

- [ ] Detail which bugs you found.
Found few logic bugs and display bugs.
1. Hard range is easier than normal range. It was 1-50.
2. Changed hard range. 1-500
3. Attempts state starts at 1 instead of 0
4. Attempts are incremented before scoring.
5. Low, higher error.

- [ ] Explain what fixes you applied.
1. Changed the hard range to 1-500 to make it more challenging than Normal mode.
2. Initialized the attempts counter to 0 instead of 1.
3. Moved the attempt increment logic so attempts are counted correctly after a guess is processed.
4. Corrected the hint messages, guesses that are too high display Go LOWER! and guesses that are too low display Go HIGHER!.
5. Tested each difficulty level and made sure that the gameplay matched the rules after the fixes.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the game.
2. Enter a guess, enter and click Submit.
3. Read the Higher or Lower hint.
4. Keep guessing until the correct number is entered.
5. The game shows a win message when the correct number is guessed.
6. If you want replay click on New Game button.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
PS C:\Users\sewwa\ai110-module1show-gameglitchinvestigator-starter> python -m pytest
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\sewwa\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 3 items                                                                                                                                  

tests\test_game_logic.py ...                                                                                                                 [100%]

================================================================ 3 passed in 0.03s ================================================================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
