"""
Training script untuk Language Model (CharLM) berbasis character-level text generation.
Menggunakan data dari data/lm_text.txt untuk belajar pola bahasa.

Usage:
    python train_lm.py
"""

import torch
import torch.nn as nn
import torch.optim as optim
import os
from nlp.lm_model import CharLM
from nlp.char_vocab import CharVocab

BASE_DIR = os.path.dirname(__file__)

# 1. Load training data
print("📖 Loading language model training data...")
with open(os.path.join(BASE_DIR, "data/lm_text.txt"), "r", encoding="utf-8") as f:
    text = f.read()

print(f"✅ Loaded {len(text)} characters from lm_text.txt")
print(f"📝 Sample: {text[:100]}...")

# 2. Build character vocabulary
print("\n🔤 Building character vocabulary...")
vocab = CharVocab()
vocab.build(text)
print(f"✅ Vocabulary size: {len(vocab)} unique characters")

# 3. Prepare training data - sequence to sequence format
print("\n⚙️  Preparing training sequences...")
seq_len = 50  # Length of input sequence
step = 5      # Step between sequences (overlap for more training data)

X = []
y = []

for i in range(0, len(text) - seq_len, step):
    sequence = text[i:i + seq_len]
    target = text[i + seq_len]
    
    X.append(vocab.encode(sequence))
    y.append(vocab.ch2i[target])

X = torch.tensor(X, dtype=torch.long)
y = torch.tensor(y, dtype=torch.long)

print(f"✅ Created {len(X)} training sequences")
print(f"   Each sequence: {seq_len} characters → predict 1 next character")

# 4. Initialize model
print("\n🧠 Initializing CharLM model...")
model = CharLM(len(vocab), embed=32, hidden=64)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print(f"✅ Model parameters: {sum(p.numel() for p in model.parameters())} total")

# 5. Training loop
print("\n🚀 Starting training...")
epochs = 50
batch_size = 32
best_loss = float('inf')
patience = 10
patience_counter = 0

for epoch in range(epochs):
    total_loss = 0
    num_batches = 0
    
    # Shuffle indices
    indices = torch.randperm(len(X))
    
    for i in range(0, len(X), batch_size):
        batch_indices = indices[i:i + batch_size]
        batch_X = X[batch_indices]
        batch_y = y[batch_indices]
        
        optimizer.zero_grad()
        
        # Forward pass - use full sequence to predict next char
        out, _ = model(batch_X)
        loss = criterion(out[:, -1, :], batch_y)  # Use last output
        
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        num_batches += 1
    
    avg_loss = total_loss / num_batches
    
    # Print progress
    if (epoch + 1) % 5 == 0:
        print(f"Epoch {epoch+1}/{epochs} | Loss: {avg_loss:.4f}")
    
    # Early stopping
    if avg_loss < best_loss:
        best_loss = avg_loss
        patience_counter = 0
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print(f"⏹️  Early stopping di epoch {epoch+1}")
            break

# 6. Save model
print("\n💾 Saving model...")
os.makedirs("model", exist_ok=True)

torch.save({
    "model": model.state_dict(),
    "vocab": vocab.ch2i,
    "config": {
        "embed": 32,
        "hidden": 64,
        "vocab_size": len(vocab),
        "seq_len": seq_len,
    }
}, os.path.join(BASE_DIR, "model/lm.pt"))

print(f"✅ Model saved to model/lm.pt")

# 7. Test generation
print("\n🎯 Testing generation...")
model.eval()
with torch.no_grad():
    test_prompts = ["aku ", "python ", "kode ", "data "]
    
    for prompt in test_prompts:
        ids = vocab.encode(prompt)
        if not ids:  # Skip if prompt has unknown chars
            continue
            
        x = torch.tensor([ids])
        h = None
        
        generated = prompt
        for _ in range(50):
            out, h = model(x, h)
            probs = torch.softmax(out[0, -1], dim=0)
            next_idx = torch.multinomial(probs, 1).item()
            generated += vocab.i2ch[next_idx]
            x = torch.tensor([[next_idx]])
        
        print(f"  Prompt: '{prompt}' → '{generated[:70]}...'")

print("\n✨ Done! Language model training complete!")
