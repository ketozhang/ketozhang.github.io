FLASK_HOST ?= 0.0.0.0

local:
	.venv/bin/flask run -p 8080 --host=${FLASK_HOST}

debug:
	FLASK_ENV=development make local

static:
	make build freeze

build:
	.venv/bin/python app.py build

freeze:
	.venv/bin/python app.py freeze

