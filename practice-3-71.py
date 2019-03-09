#import glob         # not glob2 - can't find??
from _datetime import datetime
# from glob import glob
# from glob2 import glob

import glob2
import colorama

# https://stackoverflow.com/questions/14295680/unable-to-import-a-module-that-is-definitely-installed
# https://stackoverflow.com/questions/23417941/import-error-no-module-named-does-exist/40883739#40883739

combined_content = []

filenames = glob2.glob('file*.txt')

for input_file in filenames:
    with open(input_file, 'r') as content_file:
        print(input_file)
        combined_content += content_file.readlines()

timestamp = datetime.now()
timestamp_str = timestamp.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'

with(open(timestamp_str,'a+')) as combined_content_file:
    combined_content_file.writelines(combined_content)

