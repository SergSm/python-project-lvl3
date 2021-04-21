install:
	poetry install

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check

build:
	poetry build

run:
	poetry run page-loader 'sergsm.github.io'

test:
	poetry run pytest --junit-xml=./tests/coverage.xml

coverage:
	poetry run coverage xml

.PHONY: page_loader test