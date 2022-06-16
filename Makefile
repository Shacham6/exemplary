# Local repo management
.PHONY: tests docs

SRC_DIR = exemplary

BANDIT = bandit --skip B101,B301,B403,B506

prepare-dev:
	pip install -r requirements-dev.txt

clean:
	rm -rf **/__pycache__ **/.pytest_cache/ ./dist/ ./.mypy_cache/

fix-format:
	yapf --recursive --in-place --parallel $(SRC_DIR)/ tests/

check-format:
	flake8 $(SRC_DIR)/

typecheck:
	pytype $(SRC_DIR) --config pytype.cfg

run-tests:
	coverage run \
		--source $(SRC_DIR) \
		-m pytest \
		-v tests

coverage:
	coverage report \
		--show-missing

bandit:
	$(BANDIT) --recursive $(SRC_DIR)

lint: | typecheck check-format

check: | check-format typecheck run-tests coverage

prepare-docs:

clean-generated-docs:

build:
	pip install --upgrade build
	python -m build

publish:
	pip install --upgrade twine
	twine upload dist/*
