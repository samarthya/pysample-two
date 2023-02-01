# Sample2

Code is organized in structure like below

```bash
> tree .
.
├── README.md
├── filer
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── filer.cpython-310.pyc
│   ├── filer.py
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── test_filer.cpython-310.pyc
│       ├── test_file.txt
│       └── test_filer.py
└── main.py
```

Where the `main.py` is the entry point python script and can be invoked using the command as below

```bash
> ./main.py
- Welcome - 
System Version :3.10.9 (main, Dec 15 2022, 17:11:09) [Clang 14.0.0 (clang-1400.0.29.202)]


usage: main.py [-h] -f FILE [-l LINES] [-v]
```

Detailed help can be looked up by using

```bash
> ./main.py -h -v
- Welcome - 
System Version :3.10.9 (main, Dec 15 2022, 17:11:09) [Clang 14.0.0 (clang-1400.0.29.202)]


usage: main.py [-h] -f FILE [-l LINES] [-v]

Parses the file and dumps a line

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file path
  -l LINES, --lines LINES
                        Line to read from file
  -v, --verbose         Turn on verbose mode
```

## feature

This script is a simple script, that expects a file as input and a line number. In case the line number is not found it will throw exception of type `FilerException` and if the file is not found the exceptions would be the same but with different mesage.


### `argparse`

I am using module `argparse`. It is a standard Python module for parsing command-line arguments. It provides a convenient and easy-to-use way of defining and handling command-line arguments in a structured manner. With argparse, you can define the arguments and options your script accepts, specify the types of arguments, assign default values, and display help messages to the user. Additionally, argparse automatically generates usage and error messages, making it a powerful tool for creating command-line applications in Python.

## Coverage

You can run coverage by installing `coverage.py`

```bash
> pip3 install coverage

Collecting coverage
  Downloading coverage-7.1.0-cp310-cp310-macosx_11_0_arm64.whl (198 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 199.0/199.0 kB 1.0 MB/s eta 0:00:00
Installing collected packages: coverage
Successfully installed coverage-7.1.0
```

You can run the `unittest` coverage as below

```bash
coverage run -m unittest filer.tests.test_filer
```

You can see the text report as under

```bash
> coverage report
Name                                                                     Stmts   Miss  Cover
--------------------------------------------------------------------------------------------
/opt/homebrew/lib/python3.10/site-packages/_distutils_hack/__init__.py      98     93     5%
filer/__init__.py                                                            1      0   100%
filer/filer.py                                                              30      1    97%
filer/tests/__init__.py                                                      0      0   100%
filer/tests/test_filer.py                                                   19      1    95%
--------------------------------------------------------------------------------------------
TOTAL                                                                      148     95    36%
```

You can also generate HTML report as under

```bash
> coverage html
Wrote HTML report to htmlcov/index.html
```

It will generate html files under `htmlcov` folder


