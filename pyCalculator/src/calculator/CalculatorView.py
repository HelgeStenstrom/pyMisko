# Originalet till denna fil är i Java. Kanske jag borde skriva om det
# till något GUI-framework som Python förstår, på både Windows och
# Mac. Finns sådana?

# Annars får jag försöka göra det i ett terminalfönster.

# Jag behöver strängt taget inte se något annat än min display;
# knapparna behövs inte.

class JLabel:
    def __init__(self):
        pass

class CalculatorView:
    BUTTON_LABELS = [
		"7", "8", "9", "+",
		"4", "5", "6", "-",
		"1", "2", "3", "*",
		"0", ".", "=", "\u00F7",
		"C", "\u00B1", "\u221A", "^"]
    

    def __init__(self, model, controller):
        self.displayLabel = ""
        self.model = model
        self.controller = controller


    def materializeView(self, container):
        pass

    def updateView(self):
        displayLabel.setText(model.getDisplay())

