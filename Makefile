# Local repo management
.PHONY: tests docs

SRC_DIR = exemplary

BANDIT = bandit --skip B101,B301,B403,B506

prepare-dev:
	@pip install -r requirements-dev.txt

clean:
	@rm -rf **/__pycache__ **/.pytest_cache/ ./dist/ ./.mypy_cache/

fix-format:
	@black

run-pylint:
	@pylint $(SRC_DIR)/

run-flake8:
	@flake8 $(SRC_DIR)/

typecheck:
	@mypy $(SRC_DIR)

lint: run-pylint run-flake8 typecheck

run-pytest:
	@coverage run \
		--source $(SRC_DIR) \
		-m pytest \
		-v tests

check-coverage:
	@coverage report \
		--show-missing

tests: | run-pytest check-coverage

bandit:
	@$(BANDIT) --recursive $(SRC_DIR)

prepare-docs:

clean-generated-docs:

build:
	@pip install --upgrade build
	@python -m build

publish:
	@pip install --upgrade twine
	@twine upload dist/*
