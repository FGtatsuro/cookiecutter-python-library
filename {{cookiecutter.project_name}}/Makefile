CONTAINER_TAG = {{cookiecutter.project_name|lower|replace('-', '_')}}:0.1
CONTAINER_NAME = {{cookiecutter.project_name|lower|replace('-', '_')}}_container
TIME_ZONE = Asia/Tokyo
SRC = $(wildcard {{cookiecutter.project_name|lower|replace('-', '_')}}/*.py)

.PHONY: all build run clean lint format

all: run

build: .build

# Ref: https://www.gnu.org/software/make/manual/html_node/Wildcard-Examples.html#Wildcard-Examples
.build: Dockerfile requirements.txt setup.cfg setup.py $(SRC)
	docker build -t $(CONTAINER_TAG) .
	touch .build

run: build
	docker run -i -d --name $(CONTAINER_NAME) \
		-e TZ=$(TIME_ZONE) \
		-e PYTHONPATH=. \
		$(CONTAINER_TAG) \
		/bin/bash

clean:
	-docker rm -f $(CONTAINER_NAME)
	rm -f .build

# This target always return 0 as exit code.
# If you want to fail this target(ex. CI), you must create a wrapper script like:
# 	make lint 2>&1 | grep Error; if [ $? -eq 0 ]; then exit 1; fi
lint:
	-flake8 .
	-pydocstyle .
	-mypy -p {{cookiecutter.project_name|lower|replace('-', '_')}}
	-isort --diff --recursive .

format:
	autopep8 --in-place --aggressive --recursive .
	isort --recursive .

tags: Dockerfile requirements.txt setup.cfg setup.py $(SRC)
	ctags -R --exclude=.mypy_cache
