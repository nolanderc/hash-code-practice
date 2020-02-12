# Calculate the score of a solution by running a command on a sample input.
#
# Usage:
#   
#   python score.py <sample> -- <command>
#
# Where <sample> is a path to the sample input and <command> a command that
# executes your solution.  The contents of <sample> will be sent to the stdin
# of <command>.
#
# Example:
#
#   python score.py a_example.in -- ./mock.sh
#
# Would run the script in `mock.sh` (the example output in the problem
# statement) and calculate the total score for that sample.
#

import sys
import subprocess

USAGE = "python score.py <sample> -- <command>"

def error(message):
    sys.exit("Error: " + message)

if not '--' in sys.argv:
    error(f"missing command: {USAGE}")

command_split = sys.argv.index('--')
if command_split < 2:
    error(f"missing sample: {USAGE}")

sample = sys.argv[1]
run_commands = sys.argv[command_split + 1:]


with open(sample, 'r') as sample_file:
    print(f"Testing '{sample}' with: " + " ".join(run_commands))
    result = subprocess.run(run_commands, stdout=subprocess.PIPE, stdin=sample_file)

output = result.stdout.decode("utf-8").strip()

print("---OUTPUT---")
print(str(output))
print("------------")


def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None

def parse_answer(text):
    lines = text.splitlines()
    if len(lines) != 2:
        error(f"expected two lines in the output: found {len(lines)} lines")

    # Parse first line in answer
    header = lines[0].split()
    if len(header) != 1 or parse_int(header[0]) is None:
        error(f"on the first line: expected a single integer, found '{lines[0]}'")
    count = parse_int(header[0])

    # Parse second line in answer
    content = lines[1].split()
    if len(content) != count:
        error(f"on the second line: expected {count} integers, found {len(content)} integers")

    order = []
    for item in content:
        index = parse_int(item)
        if index is None:
            error(f"on the second line: expected integer, found '{item}'")
        order.append(index)

    return order

def parse_input(text):
    lines = text.splitlines()

    header = lines[0].split()
    slices = int(header[0])
    count = int(header[1])

    pizzas = [int(pizza) for pizza in lines[1].split()]

    return slices, pizzas


order = parse_answer(output)

with open(sample, 'r') as sample_file:
    sample_input = sample_file.read()
    slices, pizzas = parse_input(sample_input)

score = 0

for item in order:
    if item >= len(pizzas): 
        error(f"no pizza with index '{item}'")

    score += pizzas[item]

if score > slices:
    error(f"more than {slices} slices ordered, found {score}")

print(f"Score: {score}")

