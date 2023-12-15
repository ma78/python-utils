#!/usr/bin/env make

include Makehelp.mk


## Create/activate python virtualenv
venv:
	./scripts/make.sh venv
.PHONY: venv


## Format python code using black
fmt:
	. .venv/bin/activate && black --line-length 256 .


## Perform code format using black
check-fmt:
	. .venv/bin/activate && black --line-length 256 --check .
.PHONY: check-fmt


## Perform pylint check
check-lint:
	. .venv/bin/activate && pylint datetimeutils tests
.PHONY: check-lint


## Perform mypy check
check-type:
	. .venv/bin/activate && mypy datetimeutils tests
.PHONY: check-type


## Perform fmt, lint and type checks
check: check-fmt check-lint check-type
.PHONY: check


## Perform unit tests
test:
	. .venv/bin/activate && ./scripts/make.sh test
.PHONY: test
