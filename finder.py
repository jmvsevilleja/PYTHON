from pathlib import Path
import re

for filename in Path('.').glob('*/config/install/webcomposer*.yml'):
    textfile = open(filename, 'r')
    filetext = textfile.read()
    textfile.close()

    string = re.findall(r': [\'"](.*?)[\'"]\n',filetext)
    string = list(filter(None, string))

    string = set([x for x in string if string.count(x) > 1])
    if string:
       print(filename, string)
