# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, it worked, but several parts of the logic were incorrect. It looked okay at first glance but whn you try guessing I was able to find few errors/bugs. The game did not match with intended gameplay.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The Hard difficulty range was set to 1–50, which was easier than the Normal range of 1–100.
The attempts counter started at 1 instead of 0.
The hint messages were backwards, telling the player to go higher when the guess was too high and lower when the guess was too low. It told me to go lower even at 0.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input   | Expected Behavior | Actual Behavior | Console Output / Error |
|-------  |-------------------|-----------------|------------------------|
|Hard mode|Range should be harder than Normal mode |Range was only 1–50 |No error |
|Guess 80 when secret is 50 | Hint should say Go LOWER! | Hint said "Go HIGHER!"| No error|
|Type a guess and click outside the input box without pressing enter and submit |The guess should not be counted and attempts should not change until Submit is clicked |An attempt was counted even though submit was not clicked |No error|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used chatgpt to help identify bugs in the code and understand why certain behaviors were happening. And suggested where i should be focusing on, which parts needs to be changed. There was a misleading advice as well and I had to double check it.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It helped me to identify that hard mode used a range of 1–50 while normal mode used 1–100. It pointed out that this made hard mode easier than normal mode. checked it with get_range_for_difficulty() function and running the game with both difficulty settings. After changing the hard range to 1–500, the difficulty levels made more sense.

- Give one example of an ai suggestion that was incorrect or misleading (including what the ai suggested and how you verified the result).
It was not completely accurate was when it suggested several additional bugs that were not part of the issues I ended up fixing. Example for when it pointed out that the attempt counter logic was incorrect and implied that the main issue was simply where the increment line was placed. I initially assumed that moving st.session_state.attempts += 1 would fully fix the issue, but it did not make much difference.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
It was by running the application after each change and checking whether the gameplay matched my expectations. I tested one issue at a time so I could clearly see the effect of each fix.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran was changing Hard mode and checking the displayed range. After changing the range to 1–500, the game correctly showed the new difficulty level. I also tested the hint logic by making guesses that were higher and lower than the secret number to confirm the correct messages appeared.

- Did AI help you design or understand any tests? How?
Yes. It suggested specific inputs I should try in the guessing box to see how the program reacts. One example was when it told me to enter an invalid value like a word instead of a number. This helped me test the parse_guess() function and confirm that the game correctly detects non numeric input and shows the error message “That is not a number.”

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns mean the whole code runs again every time you click or type something. Session state is like memory for the app. It remembers things like your score and attempts so they don’t reset every time.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
One habit is testing every bug one at a time instead of changing many things at once. This helped me clearly see what each fix actually changed and made debugging easier.

  - This could be a testing habit, a prompting strategy, or a way you used Git.

- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently when working with ai is double checking every suggestion by running the code and not assuming it is correct.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
A code can run without errors and still contain logic bugs. So i learned that ai is a useful tool for finding issues and explaining code, but every suggestion should be tested and verified. Testing the code is important as some bugs are not obvious until you try different inputs and scenarios.