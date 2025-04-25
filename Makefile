.PHONY: format lint test

format:
	isort .
	black .

lint:
	flake8 .

check: format lint test
