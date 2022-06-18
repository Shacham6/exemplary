# Local repo management
.PHONY: tests docs examples

SRC_DIR = exemplary

BANDIT = bandit --skip B101,B301,B403,B506

prepare-dev:
	@pip install -r requirements-dev.txt

clean:
	@rm -rf **/__pycache__ **/.pytest_cache/ ./dist/ ./.mypy_cache/

fix-format:
	@black

pylint:
	@pylint $(SRC_DIR)/

flake8:
	@flake8 $(SRC_DIR)/

typecheck:
	@mypy $(SRC_DIR) --pretty

lint: pylint flake8 typecheck

pytest:
	@coverage run \
		--source $(SRC_DIR) \
		-m pytest \
		-v tests

check-coverage:
	@coverage report \
		--show-missing

tests: | pytest check-coverage

examples:
	@pytest -c examples/pytest.ini examples

bandit:
	@$(BANDIT) --recursive $(SRC_DIR)

prepare-docs:
	exemplary generate examples/1_scanner.py > docs/1_gen_scanner.md

clean-generated-docs:
	rm docs/1_gen_scanner.md

publish-docs:
	make prepare-docs
	mkdocs gh-deploy
	make clean-generated-docs

watch-docs:
	make prepare-docs
	mkdocs serve
	make clean-generated-docs

build:
	@pip install --upgrade build
	@python -m build

publish:
	@pip install --upgrade twine
	@twine upload dist/*
