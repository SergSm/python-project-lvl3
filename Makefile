install:
	poetry install

package-install:
	pip3 install --user dist/*.whl

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check

build:
	poetry build

run:
	poetry run page-loader https://sergsm.github.io/index.html

test:
	poetry run pytest --junit-xml=./tests/coverage.xml

coverage:
	poetry run coverage xml

.PHONY: page_loader test