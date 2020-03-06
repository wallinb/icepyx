"""
==================
Construct is2class
==================

This example shows how to instantiate an is2class object
"""

import os
import sys
sys.path.append(os.path.abspath('../..'))

print(sys.path)

try:
    import icepyx


sys.path.append(os.path.abspath('../../icepyx/core'))
print(sys.path)

try:
    import icepyx