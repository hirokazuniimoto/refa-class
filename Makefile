.PHONY: lint, format

lint:
	black . --check ; \
	flake8 . ; \
	isort . --check-only

format:
	black .
	isort .
