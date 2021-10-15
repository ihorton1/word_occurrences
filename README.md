# Website Word Occurrence Counter

## Table of Contents

- [Tech Stack Overview](#Tech Stack Overview)
- [Prerequisites](#prerequisites)
- [Build](#build)
- [Run](#run)
- [Test](#test)

## Tech Stack Overview <a name="Tech Stack Overview"></a>

- Flask web application
- Gunicorn web server

## Prerequisites <a name="prerequisites"></a>

- Git
- [Docker](https://docs.docker.com/docker-for-mac/install/)

## Build <a name="build"></a>

Run the build make target via:

`make -f Makefile.mk build`

## Run <a name="run"></a>

You can run this flask application by running the run_app make target via:

`make -f Makefile.mk run_app`

Note: the run_app make target will also build the image, if not done so already.

## Test <a name="test"></a>

You can run tests (functional and unit) by running the run_tests make target via:

`make -f Makefile.mk run_tests`

For a test coverage report run:

`make -f Makefile.mk run_test_coverage`