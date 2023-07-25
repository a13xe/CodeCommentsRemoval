import re

single_line_comment_regex = r'//.*?$'  # regular expression to match single-line comments
multi_line_comment_regex = r'/\*.*?\*/'  # to match multi-line comments
empty_lines_regex = r'^\s*?$'  # regular expression to match empty lines

with open('file_input.txt', 'r') as file:
    content = file.read()

# remove all single-line/multi-line comments
content = re.sub(single_line_comment_regex, '', content, flags=re.MULTILINE)
content = re.sub(multi_line_comment_regex, '', content, flags=re.DOTALL)

# remove empty lines
content = re.sub(empty_lines_regex, '', content, flags=re.MULTILINE)

with open('file_output.txt', 'w') as file:
    file.write(content)
