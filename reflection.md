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
2) Manually, I would test different combinations of inputs (e.g., a low, low, high, low) and then do so at various attempts in the game. Although covering all cases this way would grow exponentially, the few, random cases I did do ended up revealing issues with the state behavior of the hints
3) AI made all of the tests. I asked for "tests that cover every unique combination of secret, being higher or lower, and game mode" and it provided the tests now shown in the test_game_logic.py file
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit is useful because it allows a simple python script to be used as an interactive web app. It does this, however, byt rerunning the entire script each time the page is interacted with; this causes issues with possibly re-initializing variables with each click. The concept of session state solves this issue by essentially telling streamlit what variables (and their associated values) ought to persist. It also seems useful in creating different use cases/regimes (e.g., making easy, normal, and ahrd modes with differing settings for each)

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git. (1)
- What is one thing you would do differently next time you work with AI on a coding task? (2)
- In one or two sentences, describe how this project changed the way you think about AI generated code. (3)

(1) Through this project, I was introduced to intergating Github Copilot into VSCode. I had previously used tools like Claude or ChatGPT via copying and pasting code, but the ability to use things like inline chats and agent/ask/plan modes was new and exciting

(2) Now knowing both the strength of the github copilot AI--as well as some of its limitations--I will more effectively use the tools to first ensure I have a deep understanding of what the code is seeking to do. Lacking this knowledge at some points in this project, I ended up being somewhat blindly led by the AI.

(3) Coding with AI is truly about knowing what you want, and to a certain extent, how it needs to look. Anyone can prompt for a bunch of code; someone good at it, however, will know what particular specifications (and in what ways to share them) that will provide the best possible code.
