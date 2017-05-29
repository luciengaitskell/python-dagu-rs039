from dagurs039 import DaguRS039, data
from dagurs039.config import MotorLayout
import time

d = DaguRS039()
d.cfg(MotorLayout(MotorLayout.INDIV), data.lipo_low_bty_preset['2S'], 2, 2, 2, 2, 13500, 800, 10, 10)

num_mtrs = 4
for m in range(0, num_mtrs):
    mp = [0] * num_mtrs
    mp[m] = 10
    print("Set Motor {} to 10".format(m))
    d.set_mtr(*mp)
    time.sleep(1)

# Disable all motors:
d.set_mtr(*([0]*num_mtrs))
