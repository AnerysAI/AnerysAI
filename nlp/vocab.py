from collections import Counter

class Vocabulary:
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}

    def build(self, texts):
        counter = Counter()
        for text in texts:
            for w in text.split():
                counter[w] += 1

        # Sort by frequency untuk konsistensi
        sorted_words = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        self.word2idx = {w: i for i, (w, _) in enumerate(sorted_words)}
        self.idx2word = {i: w for w, i in self.word2idx.items()}

    def vectorize(self, text):
        vec = [0] * len(self.word2idx)
        for w in text.split():
            if w in self.word2idx:
                vec[self.word2idx[w]] += 1
        return vec

    def __len__(self):
        return len(self.word2idx)