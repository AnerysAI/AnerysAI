import random

def decide(state, intent, confidence, entities):
    # confidence rendah → jawab natural
    if confidence < 0.25:
        return (
            "Aku belum sepenuhnya yakin dengan maksudmu 🤔\n"
            "Coba jelaskan sedikit lagi."
        )

    # greeting
    if intent == "greet":
        return "Halo 👋 Ada yang ingin kamu bicarakan?"

    # pertanyaan
    if intent == "ask":
        return (
            "Pertanyaan yang bagus.\n"
            "Bisa kamu jelaskan konteksnya lebih detail?"
        )

    # ngobrol santai
    if intent == "chat":
        return "Aku di sini buat ngobrol. Lanjutkan 😊"

    # terima kasih
    if intent == "thanks":
        return "Sama-sama 😄"

    # keluar
    if intent == "bye":
        state.reset()
        return "Sampai jumpa 👋"

    # fallback cerdas
    return (
        "Aku masih belajar, tapi aku tertarik dengan topik ini.\n"
        "Boleh kamu jelaskan lebih lanjut?"
    )