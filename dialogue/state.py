class DialogueState:
    def __init__(self):
        self.history = []

    def add(self, role, text):
        self.history.append({"role": role, "text": text})

        if len(self.history) > 10:
            self.history.pop(0)

    def reset(self):
        self.history = []