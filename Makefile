# Check make version.
MAKE_MIN_VERSION := 3.82  # MacOS comes with lower version
MAKE_OK := $(filter $(MAKE_MIN_VERSION),$(firstword $(sort $(MAKE_VERSION) $(MAKE_MIN_VERSION))))
ifeq ($(MAKE_OK),)
	$(error Make version required $(MAKE_MIN_VERSION)+, current version: $(MAKE_VERSION))
endif

# Versions.
PYTHON = python3.10
PIP_VERSION = 22.3.1
SETUPTOOLS_VERSION = 65.6.3
WHEEL_VERSION = 0.38.4

# Paths.
PROJECT_PATH = $(CURDIR)
export VIRTUAL_ENV ?= $(PROJECT_PATH)/.venv_$(PYTHON)

# Bin.
VENV_ACTIVATE = $(VIRTUAL_ENV)/bin/activate

# Tests.
APP_NAME = "com.playrix.township"
DEVICE_UDID = "AQKSLVH002M41600014"

# Other.
SHELL = /bin/bash  # Using bash as default shell
CHECK_PYTHON = $(shell which $(PYTHON))
UID = $(shell id -u)
GID = $(shell id -g)

export PATH := $(VIRTUAL_ENV)/bin:$(PATH)


all: help

$(VENV_ACTIVATE):
	# Check if correct python is installed.
ifeq ($(CHECK_PYTHON), )
	$(error $(PYTHON) was not found but needed to continue. Please install $(PYTHON))
endif
	$(PYTHON) -m venv $(VIRTUAL_ENV)
	pip install pip==$(PIP_VERSION) setuptools==$(SETUPTOOLS_VERSION) wheel==$(WHEEL_VERSION)

## Prepare environment for develop autotests.
install: $(VENV_ACTIVATE)
	# Check user uid.
ifeq ($(UID),0)
	$(error Can not run this command as root user)
endif
	pip install --upgrade -r $(PROJECT_PATH)/requirements.txt

## Run linter.
lint: $(VENV_ACTIVATE)
	black --check --diff --color $(PROJECT_PATH)
	pylint $(PROJECT_PATH)/tests $(PROJECT_PATH)/township_qa settings.py
	mypy $(PROJECT_PATH) --config-file=pyproject.toml

## Run code formatter.
style: $(VENV_ACTIVATE)
	black $(PROJECT_PATH)

## Create an emulator
emulator:
	echo "The emulator created and started"

## Start appium server
appium:
	appium

## Start emulation and the app
start: appium emulator
	echo "The app installed"

## Run autotests.
test: $(VENV_ACTIVATE)
	pytest tests


HELP_TARGET_MAX_CHAR_NUM = 20

.PHONY:
help:
	@echo Usage:
	@echo '  make <target>'
	@echo '  make <target> <VAR>=<value>'
	@echo ''
	@awk '/^[a-zA-Z\-\_0-9\/]+:/ \
		{ \
			helpMessage = match(lastLine, /^## (.*)/); \
			if (helpMessage) { \
				helpCommand = substr($$1, 0, index($$1, ":")-1); \
				helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
				helpGroup = match(helpMessage, /^@([^ ]*)/); \
				if (helpGroup) { \
					helpGroup = substr(helpMessage, RSTART + 1, index(helpMessage, " ")-2); \
					helpMessage = substr(helpMessage, index(helpMessage, " ")+1); \
				} \
				printf "%s|  %-$(HELP_TARGET_MAX_CHAR_NUM)s %s\n", \
					helpGroup, helpCommand, helpMessage; \
			} \
		} \
		{ lastLine = $$0 }' \
		$(MAKEFILE_LIST) \
	| sort -t'|' -sk1,1 -k2,2 \
	| awk -F '|' ' \
			{ \
			cat = $$1; \
			if (cat != lastCat || lastCat == "") { \
				if ( cat == "0" ) { \
					print "\033[1;37m Targets:\033[0m " \
				} else { \
					gsub("_", " ", cat); \
					printf "\033[1;37m Targets %s:\033[0m\n", cat; \
				} \
			} \
			print $$2 \
		} \
		{ lastCat = $$1 }'
