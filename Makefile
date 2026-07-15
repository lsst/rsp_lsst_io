.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  init              to initialize a dev environment"
	@echo "  refresh-fixtures  re-capture the discovery test fixtures"
	@echo "  clean             clear tox environments and builds"

.PHONY: init
init:
	pip install -U tox pre-commit
	rm -rf .tox
	pre-commit install
	pip install -e ".[dev]"

.PHONY: refresh-fixtures
refresh-fixtures:
	uv run --script scripts/refresh_discovery_fixtures.py

.PHONY: clean
clean:
	rm -rf _build/*
	rm -rf .tox
