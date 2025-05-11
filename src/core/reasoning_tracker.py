class ReasoningTracker:
    def __init__(self):
        self.steps = []

    def add_step(self, step: str, detail: str):
        self.steps.append({"step": step, "detail": detail})
