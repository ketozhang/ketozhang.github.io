local:
	FLASK_ENV=development \
	pipenv run flask run -p 8080 --host 0.0.0.0

build:
	pipenv run python app.py build

.PHONY: static
static:
	pipenv run python freeze.py
	find ../ -maxdepth 1 \
		! \( -name ".*" -o -name "_*" \) -exec rm -r {} \; && \
	rsync -a --remove-source-files docs/ ../  && \
	rm -rf docs

freeze:
	make static

clean:
	rm -rf docs/ && \
	rm -rf templates/*.bak && \
	rm -rf templates/notes/ && \
	rm -rf templates/posts/

push:
	make static && \
	git add -A && \
	git commit && \
	git push origin master
