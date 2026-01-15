import re
import unicodedata

def clean(text: str) -> str:
    """Membersihkan teks dengan mempertahankan karakter Indonesia"""
    text = text.lower()
    
    # Normalize Unicode untuk karakter aksen
    text = unicodedata.normalize('NFKD', text)
    
    # Hapus tanda baca kecuali spasi, tapi pertahankan huruf & angka
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
