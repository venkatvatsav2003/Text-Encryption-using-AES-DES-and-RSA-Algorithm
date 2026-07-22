.PHONY: all gen-key encrypt decrypt bench test clean docker

VERSION ?= 2.0.0

all: install

install:
	pip install cryptography pyyaml

gen-key:
	./crypto.sh $(ALGO) gen

encrypt:
	./crypto.sh $(ALGO) enc "$(DATA)"

decrypt:
	./crypto.sh $(ALGO) dec "$(DATA)"

bench:
	python3 crypto.py benchmark

test:
	python3 -m pytest tests/ -v

clean:
	rm -rf keys/ *.pyc __pycache__ .pytest_cache

docker:
	docker build -t crypto-toolkit:$(VERSION) .
