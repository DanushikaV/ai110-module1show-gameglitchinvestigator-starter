# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
I asked ai to help me with guessing game code and identify bugs in the game logic including display bugs.
<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**
It identified bugs in the game logic and gave example/suggestions how to fix those errors.
<!-- List the steps the agent took (files edited, commands run, etc.) -->
Gave me error locations and deleted the broken string fallback.
Showed the new game reset code respectively to the difficulty level.
Showed how to remove the secret stringifying glitch.

**What did you have to verify or fix manually?**

I had to manually run the code and test each bug to confirm it actually works. Some ai suggestions were correct, but others were just improvements and not required fixes for the projects. There were some misleading/wrong fixes, si I had to manually check those as well.
---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Invalid input | Check the errors in this code | Type abc in guess box | Yes | Game shows error message and does not crash |
| Secret comparison test | check the errors in this code | Guess numbers above and below secret | Yes | Correct too high and too low messages appear |
| Attempts tracking test | check errors in code | make multiple guesses | Yes | attempts increase correctly starting from 0 |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Check my game code for bugs and errors and suggest fixes.
```

**Linting output before:**

```
- Inconsistent attempts starting value (1 instead of 0)
- Hint messages are reversed
- New Game does not reset all game state properly
- Secret number type changes during gameplay causing errors```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->
I fixed the attempts starting value to 0, corrected the hard difficulty range so it is harder than normal, fixed the hint messages so they match the correct logic, and updated new game to reset all game values properly.
---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** |chatgpt | |
| **Response summary** |found logic bugs and explained why they happen| |
| **More Pythonic?** |Yes | |
| **Clearer explanation?** |Yes | |

**Which did you prefer and why?**
I only used chatgpt. It explains the bugs clearly and helped me understand how to fix them, not just what was wrong.

<!-- Your conclusion -->
This project showed me that ai can be very helpful for finding bugs, suggesting fixes, and explaining code, but it is not always fully correct. So we have to manually test and check each part.