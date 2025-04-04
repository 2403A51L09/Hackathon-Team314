import speech_recognition as sr
import pyttsx3
import time

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Speak text aloud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen and convert voice to text
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your answer...")
        print("🎤 Listening...")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        print("🗣️ You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Could not request results from the speech service.")
        return ""

# Questions (vocational skill-based)
questions = [
    {"question": "Which tool is used to fruits?", "answer": "knife"},
    {"question": "What safety equipment is worn during welding?", "answer": "helmet"},
    {"question": "What is used to measure body temperature?", "answer": "thermometer"},
]

# Run the quiz
def run_quiz():
    score = 0 
    speak("Welcome to the Voice Controlled Skill Learning Game!")
    time.sleep(1)

    for q in questions:
        speak(q["question"])
        print("❓", q["question"])
        user_answer = get_voice_input()
        if q["answer"] in user_answer:
            speak("Correct!")
            print("✅ Correct!")
            score += 1
        else:
            speak(f"Wrong. The correct answer is {q['answer']}.")
            print(f"❌ Incorrect. Answer: {q['answer']}")

    speak(f"You scored {score} out of {len(questions)}.")
    print(f"\n🎉 Game Over. Final Score: {score}/{len(questions)}")

# Start the game
if __name__ == "__main__":

    run_quiz()
