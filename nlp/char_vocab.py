class CharVocab:
    def __init__(self):
        self.ch2i = {}
        self.i2ch = {}

    def build(self, text):
        chars = sorted(set(text))
        self.ch2i = {c: i for i, c in enumerate(chars)}
        self.i2ch = {i: c for c, i in self.ch2i.items()}

    def encode(self, text):
        return [self.ch2i[c] for c in text if c in self.ch2i]

    def decode(self, ids):
        return "".join(self.i2ch[i] for i in ids)

    def __len__(self):
        return len(self.ch2i)
