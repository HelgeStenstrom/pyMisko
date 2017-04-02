import CalculatorModel
import CalculatorController
import CalculatorView

class JFrame:
    EXIT_ON_CLOSE = None
    def __init__(self, name=""):
        self.name = name
    def pack(self):
        pass
    def setVisible(self, setIfTrue):
        self.visible = setIfTrue
    def setDefaultCloseOperation(self, closeOperation):
        self.closeOperation = closeOperation
    def getContentPane(self):
        return None

class Calculator:


    def __init__(self):
        frame = JFrame("Calculator")
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        model = CalculatorModel.CalculatorModel()
        controller = CalculatorController.CalculatorController(model)
        view = CalculatorView.CalculatorView(model, controller)
        view.materializeView(frame.getContentPane())
        view.updateView()

        frame.pack
        frame.setVisible(true)
        print("Calculator __init__ loaded")

if __name__ == '__main__':
    Calculator()
