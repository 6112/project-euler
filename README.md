# Project Euler Solutions

[projecteuler.net](https://projecteuler.net/) is a website that offers several
problems related to various fields of mathematics and algorithmics. Some are
very simple, and some are much more complex. This repository contains solutions
to some of the problems listed on the Project Euler website.

## Running

In order to calculate the solution to a specific problem, simply use the run
script in the project's root directory, and give it the problem number. For
instance, if you want to calculate the answer for problem #42:

	./run 42

For some problems, it may take some time before the answer is calculated. For
most problems, the answer is given within 5 seconds; but it can take a lot more
time, with one problem reaching 90 seconds of calculation.

## Directory Structure

The `data/` directory contains the data files used by a few of the problems,
which are used for calculations or parsing.

The `problems/` directory contains the solutions for each problem I have solved.
Each file corresponds to a problem, and is named after the problem number. The
heading of the file contains the date it was solved, the computed answer, and
the original problem description from the Project Euler website.

The `helpers/` directory contains helper functions and module. Most notably,
there are functions for reading files, and handling prime numbers. Since many
problems on the Project Euler website use prime numbers, I have developed a
library for detecting prime numbers, decomposing a number into its prime
factors, iterating over primes, etc. 

I have deliberately chosen to duplicate code that would be available in
Python's standard library, because that is part of the fun of working on this
project. Coding these algorithms myself also gives me a deeper understanding
of how they work.
