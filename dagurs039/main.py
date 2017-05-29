from . import data
from .config import MotorLayout
import smbus
import time


def split_high_low(arr):
    return [(arr >> 8) & 0xff, arr & 0xff]


class DaguRS039:
    def __init__(self, addr=0x1e, bus=1):
        self.b = smbus.SMBus(1)
        self.addr = addr

    def cfg(self, mtr_cfg: MotorLayout, btry_lv: int, m1_max: int, m2_max: int, m3_max: int, m4_max: int,
            max_rpm: int, encdr_res: int, res_power: int, stall_ms: int, i2c_offset: int=0):
        self.basic_cfg(mtr_cfg, btry_lv, m1_max, m2_max, m3_max, i2c_offset)
        time.sleep(0.5)  # from tests I have found 0.2 also works, but this is for safety
        self.encoder_cfg(max_rpm, encdr_res, res_power, stall_ms)
        time.sleep(0.5)

    def basic_cfg(self, mtr_cfg: MotorLayout, btry_lv: int, m1_max: int, m2_max: int, m3_max: int, m4_max: int,
                  i2c_offset: int=0):
        """Write general configuration data to the device."""
        self.b.write_i2c_block_data(self.addr, 1, [0, mtr_cfg.as_num(), btry_lv, m1_max, m2_max, m3_max, m4_max,
                                                   i2c_offset, 1])

    def encoder_cfg(self, max_rpm: int, encdr_res: int, res_power: int, stall_ms: int):
        """Write encoder configuration data to the device."""
        darr = []
        darr.extend(split_high_low(max_rpm))
        darr.extend(split_high_low(encdr_res))
        darr.append(res_power)
        darr.append(stall_ms)
        self.b.write_i2c_block_data(self.addr, 2, darr)

    def set_mtr(self, v1: int, v2: int, v3: int, v4: int=None):
        """Set the motor velocities."""
        darr = []
        darr.extend(split_high_low(v1))
        darr.extend(split_high_low(v2))
        darr.extend(split_high_low(v3))
        if v4 is not None:
            darr.extend(split_high_low(v4))
        self.b.write_i2c_block_data(self.addr, 3, darr)
