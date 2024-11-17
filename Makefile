.PHONY: all

test:
	pytest -vs

lint:
	mypy src/

test-all: test lint

tag: test-all edit-version
	git commit -am "Bump version" && git tag -a ${version} -m "${message}"

edit-version:  # call like make tag version=''
	python -m version_editor "${version}" ${message}
