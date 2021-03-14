local:
	.venv/bin/flask run -p 8080 --host=0.0.0.0

debug:
	FLASK_ENV=development make local

static:
	make build freeze

build:
	.venv/bin/python app.py build

freeze:
	.venv/bin/python app.py freeze

