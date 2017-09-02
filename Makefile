jekyll:
	docker build --tag alexwlchan/jekyll jekyll

all: jekyll

.PHONY: jekyll
