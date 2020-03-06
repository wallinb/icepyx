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
except: 
    pass

sys.path.append(os.path.abspath('../../icepyx/core'))
print(sys.path)

try:
    import icepyx
except: 
    pass    

ipdf = icepyx.is2class.Icesat2Data('ATL06',[-55, 68, -48, 71],['2019-02-20','2019-02-20'], \
                           start_time='00:00:00', end_time='23:59:59', version='2')


print(ipdf)
