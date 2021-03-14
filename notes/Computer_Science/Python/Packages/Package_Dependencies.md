```bash
.project/
├── mypkg
│   ├── app.py
│   └── helper.py
└── run.py
```

Incorrect
: A common mistake is to have modules use ambiguous imports.
	``` py
	# project/mkpkg/app.py
	import helper

	def foo():
		return helper.bar()
	```

Solution
: Instead use relative imports, because you always means the `helper` module in the current directory of `project/mpkg/app.py`

	``` py
	# project/mkpkg/app.py
	import .helper
	# or the more verbose but more semantically intuitive way
	from . import helper

	def foo():
		return helper.bar()
	```