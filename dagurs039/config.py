class MotorLayout:
    OMNI3 = 0
    OMNI4 = 1
    MEC = 2
    INDIV = 3

    def __init__(self, base_layout: int, enc_enable: bool=False):
        self.base = base_layout
        if enc_enable:
            self.enc = 0
        else:
            self.enc = 16

    def as_num(self):
        return self.base + self.enc
