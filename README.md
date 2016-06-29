# Hypothesis Training Examples

## What is this?

If you've come here because I linked to this repo in a training course
you can skip this section and move on to the next one.

These are examples for the structured training course with Hypothesis
for Python.

They each consist of an implementation of some specification and a small
set of tests for it. Each implementation is entirely flake8 clean, has
100% test coverage and is wrong (the tests are all right, they're just
inadequate to the task).

The goal of the training course is to write tests that can find the
bugs in these implementations.

Each of these does have some use of Hypothesis in the tests already to
get you started, as the goal here is to learn more about what to test
with Hypothesis rather than the comparatively easy but time consuming
mechanical details of how to use the library.

The order I currently use in courses is:

1. Run Length Encoding
2. Binary Search
3. Cron
4. Flood Fill (this is a bonus question for if we do well on time)

The course is evolving fairly constantly, so this will change over time.
As examples get cycled out they will remain in this repository even if
they are not currently being used.

## Getting Set Up

If you use Vagrant, the Vagrantfile at the root of this repository will
give you an environment you can work in. This is not necessary and is
merely a convenience for people who prefer to work that way.

If you use [Tox], you can also run the tests by invoking the `tox` command.

Otherwise, you will need to install Hypothesis and py.test. If you want
to work in a virtualenv (which I'd encourage) the following will get you
started (assuming you are on Linux or OSX and already have virtualenv
installed):

```
python -m virtualenv training
source training/bin/activate
pip install -r requirements.txt
```

If you get an error like 'no module named virtualenv' you need to run
`pip install virtualenv` (this may require sudo depending on your
system).

[Tox]: http://tox.testrun.org/

## Running the tests

You can run the tests for a particular example by cding to the directory
for it and then running `python -m pytest`. This will run all the tests
in Python files with names starting with test_ in the current directory.

You can also run tests in a specific file with
`python -m pytest some_file.py`, or tests of a specific name with
`python -m pytest -ksome_test_jname`

Other useful test flags:

* --lf will run all tests that failed last time pytest was run (or all
  tests if none did)
* --pdb will drop you into a pdb console (somewhere between a python
  console and a debugger) at the point of test failure.
