import sys
from nlp.preprocessor import clean
from nlp.intent_classifier import IntentClassifier
from dialogue.state import DialogueState
from dialogue.policy import decide

try:
    classifier = IntentClassifier()
except FileNotFoundError as e:
    print(f"❌ {e}")
    sys.exit(1)

state = DialogueState()

print("🤖 AnerysAI 1.0 siap (ketik 'exit' untuk keluar)")
print("=" * 50)

while True:
    try:
        user = input("\nKamu: ").strip()
        
        if not user:
            continue
            
        if user.lower() == "exit":
            print("AnerysAI: Sampai jumpa 👋")
            break

        state.add("user", user)

        text = clean(user)
        intent, confidence = classifier.predict(text, threshold=0.5)
        entities = {}

        response = decide(state, intent, confidence, entities)
        state.add("assistant", response)

        print(f"AnerysAI: {response}")
        print(f"[Intent: {intent}, Confidence: {confidence:.2%}]")
        
    except KeyboardInterrupt:
        print("\n\nAnerysAI: Sampai jumpa 👋")
        break
    except Exception as e:
        print(f"❌ Error: {e}")
        continue
