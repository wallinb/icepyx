"""
==================
Construct is2class
==================

This example shows how to instantiate an is2class object
"""

import sys
sys.path.append('../../icepyx/core/')



#
import is2class as ipd
#

ipdf = ipd.Icesat2Data('ATL06',[-55, 68, -48, 71],['2019-02-20','2019-02-20'], \
                           start_time='00:00:00', end_time='23:59:59', version='2')


print(ipdf)
