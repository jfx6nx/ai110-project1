# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  1) Hints were backwards (app.py lines 38 - 40)
  2) Scoring schema rewards odd numbered attempts (app.py lines 55 - 60)
  3) Game mechanics for the different settings (easy, normal, difficult) seem to be mislabeled (app.py lines 4 - 11)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

1) I primarily used Claude (Sonnet 4.6 Extended mode) as a teacher/helping hand in navigating my terminal and setting things up (something that was very crucial as I am new to coding in many respects). I then used GitHub Copilot Chat  (v0.39.1) to ask questions pertaining to the code 
2) AI caught how the number of attempts for each difficultly were odd (i.e., less for easy than normal). The verification for this is intuitive, but it's a detail could've more easily been overlooked when focusing on more complex game mechanics.
3) When I would select blocks of code for the AI to explain the functionality/mechanics behind it, it would almost automatically just jump to trying to fix errors/refactor the code, despite my insistence that it merely explain. This showed me the utility of having distinct agent/ask/plan modes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

1) For the actual game mechanics, bugs "being fixed" was clear due to there only being but only 3 distinct outcomes for a given guess (higher, lower, or correct). Then, simply checking to make sure the correct message got printed (which I built into the test cases using copilot) was the second (but still easy) layer of verification
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
