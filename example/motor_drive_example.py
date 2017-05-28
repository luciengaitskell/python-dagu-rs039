from dagurs039 import DaguRS039, data
import time

d = DaguRS039()
d.cfg(data.motor_config['INDIV'], data.low_battery_voltage['2S'], 2, 2, 2, 2)
time.sleep(0.5) # from tests I have found 0.2 also works, but this is for safety
d.encoder_cfg(13500, 800, 10, 10)
time.sleep(0.5)

num_mtrs = 4
for m in range(0, num_mtrs):
    mp = [0] * num_mtrs
    mp[m] = 10
    print("Set Motor {} to 10".format(m))
    d.set_mtr(*mp)
    time.sleep(1)

# Disable all motors:
d.set_mtr(*([0]*num_mtrs))
