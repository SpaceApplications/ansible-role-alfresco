#!/usr/bin/python3

import hashlib
import os

password = os.getenv('ALFRESCO_PASSWORD')
encrypted = hashlib.new('md4', password.encode('utf-16le')).hexdigest()
print(encrypted)
