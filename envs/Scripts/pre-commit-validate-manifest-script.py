
# -*- coding: utf-8 -*-
import re
import sys

from pre_commit.clientlib import validate_manifest_main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(validate_manifest_main())
