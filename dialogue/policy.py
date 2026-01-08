from nlp.lm_generator import SmallLM

lm = SmallLM()

def decide(state, intent, confidence, entities):
    if confidence < 0.25 or intent == "chat":
        return lm.generate("aku ")

    if intent == "greet":
        return "Halo 👋 Ada yang ingin kamu bicarakan?"

    if intent == "thanks":
        return "Sama-sama 😄"

    if intent == "bye":
        state.reset()
        return "Sampai jumpa 👋"

    return lm.generate("menurutku ")
