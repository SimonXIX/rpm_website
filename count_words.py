# @name: count_words.py
# @creation_date: 2023-09-04
# @license: The MIT License <https://opensource.org/licenses/MIT>
# @author: Simon Bowie <simon.bowie.19@gmail.com>
# @purpose: Parses the word counts from RPM reviews, counts them, and presents the total
# @acknowledgements:

import os
import re
import markdown
import pathlib

# VARIABLES
input_directory = '/Users/ad7588/projects/rpm_website/rpm_website/content/posts'

# SUBROUTINES

# function to count words
def count_words(directory):
    count_total = 0
    # iterate over files in input directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        data = pathlib.Path(f).read_text(encoding='utf-8')
        md = markdown.Markdown(extensions=['meta'])
        md.convert(data)
        count_string = re.search("(\d+)\s*(?:/[^/]*)?\s*mins", str(md.Meta['title']))
        count_int = int(count_string.groups(1)[0])
        count_total += count_int

    return(count_total)

# MAIN PROGRAM
total = count_words(input_directory)
print(total)