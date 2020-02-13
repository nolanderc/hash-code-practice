
# Hash Code Practice

This repo contains files for the practice problem in this years Google HashCode
competition (2020).

- `practice_problem.pdf`: contains the problem statement.
- `score.py`: a python script which can be used to calculate the score of your
  solution.
- `mock.sh`: a reference solution for the example in the problem statement.
- `*.in`: test cases to calculate the total score from.


# Using `score.py`

Calculate the score of a solution by running a command on a sample input.

Usage:
  
    python score.py <samples> -- <command>

Where <sample> is a list of path to the samples input and <command> a command
that executes your solution. The contents of each sample in <samples> will be
sent to the stdin of <command>.

Example:

    python score.py a_example.in -- ./mock.sh

Would run the script in `mock.sh` (the example output in the problem
statement) and calculate the total score for that sample.


If you already have a file containing the solution. You may simple `cat` that
file:

    python score.py a_example.in -- cat a_answer.ans


To test every sample in this directory:

    python score.py *.in -- <command>

