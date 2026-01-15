# 🤖 AnerysAI - Chatbot Indonesia

AI chatbot dengan pemahaman natural language Indonesia yang mendalam.

## ✨ Fitur Utama

- **26 Intent Categories**: Pemahaman mendalam terhadap berbagai niat pengguna
- **1448 Training Patterns**: Dataset NLP terbesar untuk akurasi maksimal
- **Deep Learning Architecture**: Neural network dengan dropout regularization
- **State Management**: Conversation memory dan context awareness
- **Error Handling**: Robust error handling & comprehensive logging
- **Early Stopping**: Prevent overfitting dengan validation monitoring
- **Type Hints**: Full type annotations untuk code quality

## 🚀 Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Training Model
```bash
python train.py
```

### Run Chatbot
```bash
python run.py
```

## 📊 Dataset v3.0

**Total: 26 Intents | 1,448 Patterns | Avg 55.7 patterns/intent**

| Category | Intents | Patterns | Examples |
|----------|---------|----------|----------|
| **Greetings** | greet, greeting_casual | 116 | halo, pagi, assalamu alaikum |
| **Communication** | chat, ask, say | 156 | cerita, jelaskan, ngobrol |
| **Gratitude** | thanks | 63 | terima kasih, makasih, appreciate |
| **Parting** | bye | 70 | bye, sampai jumpa, goodbye |
| **Identity** | who_are_you, name | 105 | siapa kamu, nama aku apa |
| **Support** | help | 68 | bantuan, tolong, support |
| **Entertainment** | joke | 52 | lawak, bercanda, funny |
| **Status** | how_are_you, emotion_* | 138 | apa kabar, senang, sedih |
| **Semantic** | affirmative, negative_response, agreement, disagreement | 170 | ya, tidak, setuju, beda |
| **Knowledge** | knowledge_request | 69 | belajar, teori, pengetahuan |
| **Context** | time, place, person, object, activity | 305 | kapan, dimana, siapa, apa, melakukan |

## 📁 Project Structure

```
AnerysAI/
├── run.py                 # Main chatbot
├── train.py              # Training dengan validation
├── config.py             # Config centralized (26 intents)
├── requirements.txt      # Dependencies
├── test_nlp.py          # Unit tests
├── data/
│   └── intents.json     # 1448 patterns, 26 intents (v3.0)
├── model/
│   └── intent_model.pt  # Trained weights
├── nlp/
│   ├── model.py         # Neural network
│   ├── intent_classifier.py
│   ├── preprocessor.py
│   ├── vocab.py
│   ├── logger.py
│   └── lm_generator.py
└── dialogue/
    ├── policy.py
    └── state.py
```

## 📈 Dataset Evolution

| Version | Intents | Patterns | Growth |
|---------|---------|----------|--------|
| v1.0 | 6 | ~30 | - |
| v2.0 | 12 | 153 | +410% |
| v3.0 | 26 | 1448 | +846% |

## 🎯 26 Intent Categories

```
Core Intents (Original 6):
  greet, thanks, bye, ask, chat, who_are_you

Extended Intents (v2.0):
  help, joke, how_are_you, name, compliment, negative

Semantic Intents (v3.0):
  affirmative, negative_response, agreement, disagreement
  greeting_casual, context_continuation
  
Knowledge Intents:
  knowledge_request
  
Contextual Intents:
  time, place, person, object, activity
  
Emotion Intents:
  emotion_positive, emotion_negative
```

## 🧠 Model Architecture

```
Input (Vocab)
    ↓ 
Linear(2000 → 64)
    ↓
ReLU + Dropout(0.2)
    ↓
Linear(64 → 26 intents)
    ↓
Output (Logits)
```

## 🧪 Testing

```bash
python -m unittest test_nlp.py -v
```

## 📝 Configuration

Edit `config.py`:
- `num_classes: 26` (intents)
- `vocab_size: 2000` (words)
- Learning rate, epochs, batch size
- Confidence threshold
- File paths

## 🔧 Recent Changes

- ✅ Dataset expanded: 153 → 1448 patterns (+846%)
- ✅ Intents increased: 12 → 26 categories
- ✅ Added semantic intents (agreement, disagreement, etc)
- ✅ Added contextual understanding (time, place, person)
- ✅ Added emotion recognition (positive/negative)
- ✅ Enhanced dialogue policy
- ✅ Improved token usage

## 🐛 Known Issues & TODOs

- [ ] Named Entity Recognition (NER)
- [ ] Multi-language support
- [ ] REST API (Flask/FastAPI)
- [ ] Conversation persistence
- [ ] Sentiment analysis refinement
- [ ] Intent confidence calibration
- [ ] Response generation improvement

## 📄 License

MIT License
