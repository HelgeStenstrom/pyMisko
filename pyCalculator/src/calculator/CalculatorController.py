class CalculatorController:
    def __init__(self, model):
        self.model = model
        
    def push(self, charAt):
        self.model.setDisplay("0")
        
