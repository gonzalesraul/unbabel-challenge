# Unbabel Challenge

Provide a simple CLI to calculate the average took to delivery translations in a stream of data. 

## Table of content:

1. [The challenge](docs/unbabel-challenge.md)
2. [Introduction](#introduction)
3. [Installation](#Installation)
4. [Usage](#usage)
   1. [Examples](#examples)
5. [Creating Development Environment](#creating-development-environment)
   1. [Testing](#testing)
6. [License](#license)

For more information check [Additional Documentation](#additional-documentation)

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

`TBD`

## Usage

`TBD`

### Examples

`TBD`

## Creating Development Environment

`TBD`

### Testing

`TBD`

## License

Copyright (c) 2019, Raul Gonzales. Distributed under BSD-3-Clause. See [LICENSE](LICENSE).