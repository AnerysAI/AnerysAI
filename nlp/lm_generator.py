import torch
from nlp.lm_model import CharLM
from nlp.char_vocab import CharVocab

class SmallLM:
    def __init__(self):
        ckpt = torch.load("model/lm.pt", map_location="cpu")
        self.vocab = CharVocab()
        self.vocab.ch2i = ckpt["vocab"]
        self.vocab.i2ch = {i: c for c, i in self.vocab.ch2i.items()}

        self.model = CharLM(len(self.vocab))
        self.model.load_state_dict(ckpt["model"])
        self.model.eval()

    def generate(self, start="aku ", max_len=100):
        ids = self.vocab.encode(start)
        x = torch.tensor([ids])

        h = None
        for _ in range(max_len):
            out, h = self.model(x, h)
            probs = torch.softmax(out[0, -1], dim=0)
            idx = torch.multinomial(probs, 1).item()
            ids.append(idx)
            x = torch.tensor([[idx]])

        return self.vocab.decode(ids)
