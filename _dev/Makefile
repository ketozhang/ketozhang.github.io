local:
	.venv/bin/flask run -p 8080 --host=0.0.0.0

debug:
	FLASK_ENV=development \
	.venv/bin/flask run -p 8080 --host=0.0.0.0

build:
	.venv/bin/python app.py build

.PHONY: static
static:
	.venv/bin/python app.py build freeze
	find ../ -maxdepth 1 \
		! \( -name ".*" -o -name "_*" \) -exec rm -r {} \; && \
	rsync -a --remove-source-files docs/ ../  && \
	make clean

freeze:
	.venv/bin/python app.py freeze

clean:
	rm -rf docs/ && \
	rm -rf templates/*.bak

push:
	make static && \
	git commit -a && \
	git push origin master
