package calculator;

public class CalculatorController {

	private final CalculatorModel model;

	public CalculatorController(CalculatorModel model) {
		this.model = model;
	}

	public void push(char charAt) {
		model.setDisplay("0.");
	}

}
