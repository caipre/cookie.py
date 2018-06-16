.PHONY: clean clean-build clean-pyc clean-test lint

clean: clean-build clean-pyc clean-test

clean-build::
	rm -rf .eggs/
	rm -rf build/
	rm -rf dist/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -delete

clean-pyc:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-test:
	rm -f .coverage coverage.xml coverage.html
	rm -f junit.xml
	rm -rf .pytest_cache/
	rm -rf .tox/
	rm -rf htmlcov/
