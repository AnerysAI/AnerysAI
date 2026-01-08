import torch
import os

from nlp.model import IntentNet
from nlp.preprocessor import clean

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class IntentClassifier:
    def __init__(self):
        checkpoint = torch.load(
            os.path.join(BASE_DIR, "model/intent_model.pt"),
            map_location="cpu"
        )

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

    def predict(self, text: str):
        text = clean(text)
        X = self.vectorize(text)

        with torch.no_grad():
            logits = self.model(X)
            probs = torch.softmax(logits, dim=1)

        confidence, idx = torch.max(probs, dim=1)
        return self.idx2intent[idx.item()], confidence.item()