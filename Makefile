.PHONY: all

test:
	pytest

lint:
	mypy src/

test-all: test lint

tag: # call like make tag version=''
	python -m version_editor ${version} ${message} && git commit -am "Bump version" && git tag -a ${version} -m ${message}
