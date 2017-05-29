from dagurs039 import DaguRS039, data
from dagurs039.config import MotorLayout
import time

d = DaguRS039()
d.cfg(MotorLayout(MotorLayout.INDIV), data.lipo_low_bty_preset['2S'], 2, 2, 2, 2, 13500, 800, 10, 10)
