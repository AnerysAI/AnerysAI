import json
import os
import torch
import torch.nn as nn
import torch.optim as optim

from nlp.preprocessor import clean
from nlp.vocab import Vocabulary
from nlp.model import IntentNet

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, "data/intents.json")) as f:
    data = json.load(f)

texts = []
labels = []
intent2idx = {}

for i, intent in enumerate(data):
    if intent == "meta":
        continue
    intent2idx[intent] = len(intent2idx)
    for p in data[intent]["patterns"]:
        texts.append(clean(p))
        labels.append(intent2idx[intent])

# vocab
vocab = Vocabulary()
vocab.build(texts)

X = torch.tensor([vocab.vectorize(t) for t in texts], dtype=torch.float32)
y = torch.tensor(labels)

model = IntentNet(len(vocab), len(intent2idx))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(200):
    optimizer.zero_grad()
    out = model(X)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()

os.makedirs("model", exist_ok=True)

torch.save({
    "model": model.state_dict(),
    "vocab": vocab.word2idx,
    "intent2idx": intent2idx
}, "model/intent_model.pt")

print("✅ Model PyTorch berhasil dilatih")