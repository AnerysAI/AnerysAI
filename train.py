import json
import os
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split

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

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = IntentNet(len(vocab), len(intent2idx))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=1e-5)

print(f"📊 Training: {len(X_train)} samples, Testing: {len(X_test)} samples")

best_loss = float('inf')
patience = 20
patience_counter = 0

for epoch in range(500):
    optimizer.zero_grad()
    out = model(X_train)
    loss = criterion(out, y_train)
    loss.backward()
    optimizer.step()
    
    # Validation
    with torch.no_grad():
        val_out = model(X_test)
        val_loss = criterion(val_out, y_test)
        val_acc = (torch.argmax(val_out, dim=1) == y_test).float().mean()
    
    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1}/500 | Train Loss: {loss.item():.4f} | Val Loss: {val_loss.item():.4f} | Val Acc: {val_acc.item():.4f}")
    
    # Early stopping
    if val_loss.item() < best_loss:
        best_loss = val_loss.item()
        patience_counter = 0
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print(f"⏹️  Early stopping di epoch {epoch+1}")
            break

os.makedirs("model", exist_ok=True)

torch.save({
    "model": model.state_dict(),
    "vocab": vocab.word2idx,
    "intent2idx": intent2idx
}, "model/intent_model.pt")

print("✅ Model berhasil dilatih dan disimpan")
