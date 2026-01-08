from nlp.preprocessor import clean
from nlp.intent_classifier import IntentClassifier
from dialogue.state import DialogueState
from dialogue.policy import decide

classifier = IntentClassifier()
state = DialogueState()

print("🤖 AnerysAI 1.0 siap (ketik 'exit' untuk keluar)")

while True:
    user = input("Kamu: ")
    if user.lower() == "exit":
        break

    state.add("user", user)

    text = clean(user)
    intent, confidence = classifier.predict(text)
    entities = {}

    response = decide(state, intent, confidence, entities)
    state.add("assistant", response)

    print("AnerysAI:", response)