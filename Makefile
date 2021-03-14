FLASK_HOST ?= 0.0.0.0

local:
	poetry run flask run -p 8080 --host=${FLASK_HOST}

debug:
	FLASK_ENV=development make local

.PHONY: static
static:
	make build freeze

build:
	.venv/bin/python app.py build

freeze:
	.venv/bin/python app.py freeze

