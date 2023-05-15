comment_symbol = '#' # Replace with your desired comment symbol
input_filename = 'file_input.txt'
output_filename = 'file_output.txt'

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        if not line.lstrip().startswith(comment_symbol):
            output_file.write(line)
