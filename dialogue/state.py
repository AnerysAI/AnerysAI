class DialogueState:
    def __init__(self):
        self.history = []
        self.slots = {}
        self.last_intent = None

    def add(self, role, text):
        self.history.append({"role": role, "text": text})
        if len(self.history) > 10:
            self.history.pop(0)

    def remember(self, key, value):
        self.slots[key] = value

    def recall(self, key, default=None):
        return self.slots.get(key, default)

    def reset(self):
        self.history = []
        self.slots = {}
        self.last_intent = None
