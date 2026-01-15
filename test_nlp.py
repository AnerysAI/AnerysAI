import unittest
import torch
from nlp.preprocessor import clean
from nlp.vocab import Vocabulary
from nlp.model import IntentNet

class TestPreprocessor(unittest.TestCase):
    def test_clean_lowercase(self):
        """Test lowercase conversion"""
        assert clean("HALO") == "halo"
    
    def test_clean_punctuation(self):
        """Test punctuation removal"""
        assert clean("Halo!?") == "halo"
    
    def test_clean_whitespace(self):
        """Test whitespace normalization"""
        assert clean("halo    dunia") == "halo dunia"

class TestVocabulary(unittest.TestCase):
    def test_vocab_build(self):
        """Test vocabulary building"""
        vocab = Vocabulary()
        texts = ["halo dunia", "halo apa kabar"]
        vocab.build(texts)
        
        assert len(vocab.word2idx) == 4  # halo, dunia, apa, kabar
        assert "halo" in vocab.word2idx
    
    def test_vocab_vectorize(self):
        """Test text vectorization"""
        vocab = Vocabulary()
        texts = ["halo dunia"]
        vocab.build(texts)
        
        vec = vocab.vectorize("halo halo dunia")
        assert sum(vec) == 3  # 2x halo, 1x dunia

class TestIntentNet(unittest.TestCase):
    def test_model_forward(self):
        """Test model forward pass"""
        model = IntentNet(input_size=10, num_classes=5)
        x = torch.randn(1, 10)
        out = model(x)
        
        assert out.shape == (1, 5)
        assert torch.isnan(out).sum() == 0

if __name__ == "__main__":
    unittest.main()
