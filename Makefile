.PHONY: all

test:
	pytest

lint:
	mypy src/

test-all: test lint
