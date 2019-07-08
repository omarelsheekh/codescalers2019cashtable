#!C:\Users\omarelsheekh\PycharmProjects\codescalers2019cashtable\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pdoc3==0.6.3','console_scripts','pdoc'
__requires__ = 'pdoc3==0.6.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pdoc3==0.6.3', 'console_scripts', 'pdoc')()
    )
