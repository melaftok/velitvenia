from fix_lavamoat import *

# Define the input and output paths
input_path = "input.txt"
output_path = "output.txt"

# Read the input file
with open(input_path, "r") as f:
    input_text = f.read()

# Fix the lavamoat
fixed_text = fix_lavamoat(input_text)

# Write the fixed text to the output file
with open(output_path, "w") as f:
    f.write(fixed_text)
