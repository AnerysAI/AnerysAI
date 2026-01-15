from nlp.lm_generator import SmallLM
from nlp.code_generator import CodeGenerator

lm = SmallLM()
code_gen = CodeGenerator()

# Intent response mapping
INTENT_RESPONSES = {
    "greet": ["Halo 👋 Ada yang ingin kamu bicarakan?", "Hai! Senang dengar dari kamu."],
    "thanks": ["Sama-sama 😄", "Dengan senang hati! 😊"],
    "bye": ["Sampai jumpa 👋", "Dadah, semoga harimu baik!"],
    "who_are_you": ["Aku AnerysAI, chatbot AI kamu. 🤖"],
    "help": ["Aku siap membantu! Apa yang kamu butuhkan?", "Tentu, apa yang bisa aku bantu?"],
    "joke": ["Apa bedanya AI dan manusia? AI gak butuh tidur! 😄"],
    "how_are_you": ["Aku baik-baik saja! Bagaimana denganmu? 😊"],
    "name": ["Nama kamu siapa? Ajari aku dong! 😊"],
    "compliment": ["Terima kasih! Kamu juga keren! 😄"],
    "negative": ["Maaf ya, aku akan coba lebih baik lagi. 😔"],
    "chat": ["Cerita lebih lanjut dong! Aku tertarik mendengarnya."],
    "ask": ["Bagus pertanyaannya! Mari kita diskusi. 🤔"],
}

def decide(state, intent, confidence, entities):
    """
    Dialogue policy untuk menentukan response
    
    Args:
        state: DialogueState
        intent: Detected intent
        confidence: Confidence score (0-1)
        entities: Extracted entities
    
    Returns:
        Response string
    """
    # Threshold yang lebih tinggi untuk response umum
    if intent == "unknown" or confidence < 0.5:
        return "Maaf, aku kurang paham. Bisa diulang?"
    
    # Handle code generation intents
    if intent == "code_python":
        code = code_gen.generate("hello_world")
        return f"""Ini kode Python sederhana:

```python
{code}
```

Kamu bisa request tipe kode lain seperti:
- function, loop, list, dictionary
- class, calculator, fibonacci, factorial
- api_get, api_post, html"""
    
    elif intent == "code_html_css":
        code = code_gen.generate("html")
        return f"""Ini HTML template sederhana:

```html
{code[:400]}...
```

Mau saya generate HTML yang lebih spesifik? 🎨"""
    
    elif intent == "code_api":
        code = code_gen.generate("api_get")
        return f"""Ini Flask API endpoint:

```python
{code[:300]}...
```

Kamu bisa request GET atau POST endpoint! 🔌"""
    
    elif intent == "code_other":
        available = code_gen.list_templates()
        return f"""Tipe kode yang bisa saya generate:

{', '.join(available)}

Mana yang kamu mau? 💻"""
    
    # Check untuk predefined responses
    if intent in INTENT_RESPONSES:
        responses = INTENT_RESPONSES[intent]
        # Rotate responses untuk variety
        response_idx = len(state.history) % len(responses)
        return responses[response_idx]
    
    # Fallback ke language model
    return lm.generate("menurutku ")
