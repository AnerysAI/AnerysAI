"""Configuration untuk AnerysAI v3.0 - Large-scale NLP"""

# Model settings
MODEL_CONFIG = {
    "input_size": 64,
    "hidden_size": 128,
    "num_classes": 26,  # 26 intents
    "vocab_size": 2000,
}

# Training settings
TRAIN_CONFIG = {
    "epochs": 500,
    "batch_size": 32,
    "learning_rate": 0.01,
    "weight_decay": 1e-5,
    "train_test_split": 0.2,
    "early_stopping_patience": 20,
}

# Prediction settings
PREDICT_CONFIG = {
    "confidence_threshold": 0.5,
    "device": "cpu",
}

# Dialogue settings
DIALOGUE_CONFIG = {
    "max_history": 10,
    "greet_intents": ["greet", "greeting_casual"],
    "unknown_response": "Maaf, aku kurang paham. Bisa diulang?",
}

# File paths
PATHS = {
    "intent_model": "model/intent_model.pt",
    "lm_model": "model/lm.pt",
    "intents_data": "data/intents.json",
    "logs": "logs",
}


