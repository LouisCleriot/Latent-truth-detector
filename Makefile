.PHONY: data clean requirements model

PYTHON_INTERPRETER = python3

requirements:
	@echo "Installing requirements..."
	pip install -r requirements.txt

data:
	@echo "Downloading data..."
	$(PYTHON_INTERPRETER) src/data/download_data.py

clean:
	@echo "Cleaning up..."
	rm -rf data/*

model:
	@echo "Downloading model..."
	$(PYTHON_INTERPRETER) model/get_model.py