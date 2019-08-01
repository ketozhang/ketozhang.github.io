local:
	pipenv run python app.py

build:
	pipenv run python app.py build

.PHONY: static
static:
	pipenv run python freeze.py
	find ../ -maxdepth 1 ! \( -name ".*" -o -name "_*" \) -exec rm -r {} \;
	cp -r docs/* ../

freeze:
	make static

push:
	make static
	git add -A
	git commit
	git push origin master
