jekyll:
	docker build --tag alexwlchan/jekyll jekyll

travis:
	docker build --tag alexwlchan/travis travis

all: jekyll travis

.PHONY: all jekyll travis
