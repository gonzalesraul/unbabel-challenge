# Unbabel Challenge

  Provide a simple CLI to calculate the average took to delivery translations in a stream of data. 

## Table of content:

1. [The challenge](docs/unbabel-challenge.md)
2. [Introduction](#introduction)
3. [Installation](#Installation)
4. [Usage](#usage)
   1. [Options](#options)
   2. [Examples](#examples)
5. [Development Environment](#development-environment)
   1. [Pre-requirements](#pre-requirements)
   2. [Running locally](#running-locally)
   3. [Testing](#testing)
6. [License](#license)

## Introduction

  Meet **SAM** (**S**tream **A**verage **M**etric for short) is a command-line interface app.
  Goal: Provide a simple CLI to calculate the average took to delivery translations in stream of data

  **What is it not:**

  * It is not a monitoring solution. Use properly monitoring tools;
  * It does not provide any other metrics other than [moving average](https://en.wikipedia.org/wiki/Moving_average) for delivering events;

  **Considerations:**

  * The process compute the data as streaming, you can pipe (|) your stdout or use any other POSIX standard (files, sockets, stderr ...)
  * The outcome is grouped by each minute in a sequential order, data with timestamps delayed will be ignored

## Installation

  If you are [running locally](#running-locally) you can install with pipenv:

  ```
  $ pipenv install -e .
  Installing -e .…
  Adding sam to Pipfile's [packages]…
  Installation Succeeded
  Installing dependencies from Pipfile.lock (5e21fa)…
  ================================ 5/5 - 00:00:02
  ```


## Usage

  ```sh
  sam [OPTIONS]
  ```

### Options

  ```
  -i, --input_file FILENAME
        Path to input file stream (default: stdin)
  ```
  ```
  -w, --window_size INTEGER  
        Time window for the past N seconds (default: 10) Needs to be a positive integer
  ```
  ```
  -h, --help
        Usage help.
  ```

### Examples

  1. Redirect commands output to SAM:
      ```
      $ echo '{"duration":10,"timestamp":"2019-12-31 00:11:59","event_name":"translation_delivered"}' | sam
      { "date": "2019-12-31 00:11:00", "average_delivery_time": 0 }
      { "date": "2019-12-31 00:12:00", "average_delivery_time": 10 }
      ```
  2. Use file as input stream:
      ```sh
      #Option 1 (inform file with -i/--input_file)
      sam -i tests/files/sample.jsonl
      #Option 2 (with cat)
      cat tests/files/sample.jsonl |sam
      #Option 3 (simply type sam to read from stdin)
      sam
      ```
  3. Redirect runtime errors to a file:
      ```
      $ sam --input_file tests/files/coverall.jsonl 2>/tmp/error.log
      { "date": "2018-12-26 18:11:00", "average_delivery_time": 0 }
      { "date": "2018-12-26 18:12:00", "average_delivery_time": 20 }
      { "date": "2018-12-26 18:13:00", "average_delivery_time": 20 }
      { "date": "2018-12-26 18:14:00", "average_delivery_time": 20 }
      { "date": "2018-12-26 18:15:00", "average_delivery_time": 20 }
      { "date": "2018-12-26 18:16:00", "average_delivery_time": 25.5 }
      { "date": "2018-12-26 18:17:00", "average_delivery_time": 25.5 }
      { "date": "2018-12-26 18:18:00", "average_delivery_time": 25.5 }
      { "date": "2018-12-26 18:19:00", "average_delivery_time": 25.5 }
      { "date": "2018-12-26 18:20:00", "average_delivery_time": 25.5 }
      { "date": "2018-12-26 18:21:00", "average_delivery_time": 25.5 }
      { "date": "2018-12-26 18:22:00", "average_delivery_time": 31 }
      { "date": "2018-12-26 18:23:00", "average_delivery_time": 31 }
      { "date": "2018-12-26 18:24:00", "average_delivery_time": 42.5 }
      $ cat /tmp/error.log
      {"name": "sam", "message": "invalid literal for int() with base 10: 'invalid'\nTraceback (most recent call last):\n  File \"/path/to/file\", line 11, in getdata\n    assert int(data['duration']) >= 0", "levelno": 40, "levelname": "ERROR", "pathname": "/path/to/file", "filename": "stream.py", "module": "stream", "lineno": 14, "funcName": "getdata", "created": 1561653261.3696609, "asctime": "2019-06-27 17:34:21,369", "msecs": 369.6608543395996, "relativeCreated": 6.094217300415039, "thread": 4708, "threadName": "MainThread", "process": 8052, "processName": "MainProcess"}
      ```

## Development environment

  For portable installation method (that works on Windows, Mac OS X, Linux), make sure to have all pre-requirements.

### Pre-requirements

  * [Git](https://git-scm.com/)
  * [Python 3.7+](https://www.python.org/downloads/)
  * [Pip](https://pip.pypa.io/en/stable/installing/)
  > *Verify both versions of pip and setuptools are up-to-date* `pip install --upgrade pip setuptools`

### Running locally
  To get a environment ready to work follow the steps below:
  ```sh
  git clone git@github.com:gonzalesraul/unbabel-challenge.git unbabel-challenge
  cd unbabel-challenge
  pip install pipenv
  pipenv install --dev
  pipenv shell
  ```

### Testing

  SAM uses [pytest](https://docs.pytest.org/) and [tox](https://tox.readthedocs.io/en/latest/) for testing.

  **Running all**
  ```sh
  # Run tests and coverage
  python setup.py test
  # To generate HTML report for coverage use --html-report
  python setup.py test --html-report
  # Run all checks, tests, coverage and linter via Tox
  tox
  ```

  **Running specific**
  ```sh
  # Run specific tests on the current Python
  python -m pytest -v tests/test_main.py
  # Run specific test case
  python -m pytest -v tests/test_stream.py::test_getdata_no_input
  ```

## License

  Copyright (c) 2019, Raul Gonzales. Distributed under BSD-3-Clause. See [LICENSE](LICENSE).