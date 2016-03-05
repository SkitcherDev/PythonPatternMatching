#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

f = open(r"..\workfile.txt", "r")
message = f.read()
f.close()

mo = []
mo = phoneNumRegex.findall(message)

print('Phone number found: ' + str([x[1] for x in mo]))
print("Done")

