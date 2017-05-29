from dagurs039 import DaguRS039, data
import time

d = DaguRS039()
d.cfg(data.motor_config['INDIV'], data.lipo_low_bty_preset['2S'], 2, 2, 2, 2, 13500, 800, 10, 10)
