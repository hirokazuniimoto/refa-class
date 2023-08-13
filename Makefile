.PHONY: lint, format

lint:
	black . --check ; \
	flake8 . ; \
	isort . --check-only

format:
	black .
	isort .

mypy:
	mypy --ignore-missing-imports --follow-imports=skip --strict-optional --warn-unused-ignores --warn-redundant-casts --warn-unused-variables --no-implicit-optional --show-error-codes --pretty --html-report mypy-report --no-error-summary --no-strict-optional --no-warn-no-return --no-warn-unreachable --no-warn-unused-ignores --no-warn-unused-variables --no-warn-redundant-casts --no-warn-redundant-

rm-pypi-dir:
	rmdir /s /q dist
	rmdir /s /q build
	rmdir /s /q refaclass.egg-info

pypi-build:
	python setup.py sdist bdist_wheel
	python setup.py bdist_wheel

pypi-test:
	twine upload --repository pypitest dist/*

pypi:
	twine upload --repository pypi dist/*