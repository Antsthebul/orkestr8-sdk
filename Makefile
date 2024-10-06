.PHONY: all

test:
	pytest

lint:
	mypy src/
