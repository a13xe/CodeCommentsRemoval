comment_symbol = '#'
input_filename = 'file_input.txt'
output_filename = 'file_output.txt'

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        line_without_comment = line.split(comment_symbol, 1)[0].rstrip()
        if line_without_comment or line.strip() == '':
            output_file.write(line_without_comment + '\n')
