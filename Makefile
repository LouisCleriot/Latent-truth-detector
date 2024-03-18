.PHONY: data clean requirements

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
