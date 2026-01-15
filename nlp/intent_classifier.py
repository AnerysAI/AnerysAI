import torch
import os
from pathlib import Path

from nlp.model import IntentNet
from nlp.preprocessor import clean

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class IntentClassifier:
    def __init__(self):
        model_path = os.path.join(BASE_DIR, "model/intent_model.pt")
        
        if not Path(model_path).exists():
            raise FileNotFoundError(f"❌ Model tidak ditemukan di {model_path}. Jalankan train.py terlebih dahulu!")
        
        try:
            checkpoint = torch.load(model_path, map_location="cpu")
        except Exception as e:
            raise RuntimeError(f"❌ Error loading model: {e}")

        self.vocab = checkpoint["vocab"]
        self.intent2idx = checkpoint["intent2idx"]
        self.idx2intent = {v: k for k, v in self.intent2idx.items()}

        self.model = IntentNet(len(self.vocab), len(self.intent2idx))
        self.model.load_state_dict(checkpoint["model"])
        self.model.eval()

    def vectorize(self, text):
        vec = [0] * len(self.vocab)
        for w in text.split():
            if w in self.vocab:
                vec[self.vocab[w]] += 1
        return torch.tensor([vec], dtype=torch.float32)

    def predict(self, text: str, threshold: float = 0.5):
        """
        Predict intent dari text
        Args:
            text: Input text
            threshold: Confidence minimum untuk valid prediction
        Returns:
            (intent, confidence)
        """
        text = clean(text)
        X = self.vectorize(text)

        with torch.no_grad():
            logits = self.model(X)
            probs = torch.softmax(logits, dim=1)

        confidence, idx = torch.max(probs, dim=1)
        confidence_val = confidence.item()
        intent = self.idx2intent[idx.item()]
        
        # Return "unknown" jika confidence terlalu rendah
        if confidence_val < threshold:
            return "unknown", confidence_val
            
        return intent, confidence_val
