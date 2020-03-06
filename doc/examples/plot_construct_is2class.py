"""
==================
Construct is2class
==================

This example shows how to instantiate an is2class object
"""

print("starting at the beginning")
import sys
print("sys was imported")
sys.path.append('../../icepyx/core/')
print(sys.path)

#
import is2class as ipd
#

ipdf = ipd.Icesat2Data('ATL06',[-55, 68, -48, 71],['2019-02-20','2019-02-20'], \
                           start_time='00:00:00', end_time='23:59:59', version='2')


print(ipdf)
