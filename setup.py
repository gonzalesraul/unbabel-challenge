#!/usr/bin/env python3
import sys
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand
from sam import __version__ as version


# More info at https://docs.pytest.org/en/latest/goodpractices.html#manual-integration
class PyTest(TestCommand):

    user_options = [('html-report', None, 'Generate html report')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['--cov', 'sam', '--cov-report', 'term-missing', '-v']
        self.html_report = False

    def finalize_options(self):
        TestCommand.finalize_options(self)
        if self.html_report:
            self.pytest_args.extend(['--cov-report', 'html'])
        self.pytest_args.extend(['tests'])

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


tests_require = ['pytest', 'pytest-cov']


setup(
    packages=find_packages(exclude=['tests']),
    version=version,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    cmdclass={'test': PyTest},
    test_suite='tests',
    entry_points={'console_scripts': ['sam=sam.main:main']}
)
