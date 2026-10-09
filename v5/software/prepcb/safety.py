"""Independent transition reference for the pre-PCB supervisory RTL."""
STATES = ['POWER_OFF', 'RESET_SAFE', 'BOARD_CHECK', 'ARMED_SAFE', 'CAL_SPARSE',
          'CAL_QUALITY_GATE', 'CAL_READY', 'IDLE_TRAP', 'MOTION_EXEC', 'FAULT_LATCHED', 'ESTOP']


class Safety:
    def __init__(self, long_press=1000, timeout=30000):
        self.state = 'RESET_SAFE'
        self.arm_count = self.cal_count = self.age = 0
        self.long_press, self.timeout = long_press, timeout
        self.arm_released = self.cal_released = False

    def step(self, *, healthy=True, estop_ok=True, arm=False, cal=False,
             clear=False, complete=False, quality=False, trap=False, motion=False,
             done=False, stop=False):
        if not estop_ok:
            self.state = 'ESTOP'
        elif not healthy or self.age >= self.timeout:
            self.state = 'FAULT_LATCHED'
        elif self.state in ('ESTOP', 'FAULT_LATCHED'):
            if clear and not arm and not cal:
                self.state = 'RESET_SAFE'
                self.arm_released = self.cal_released = False
        elif stop:
            self.state = 'RESET_SAFE'
            self.arm_released = self.cal_released = False
        elif self.state == 'RESET_SAFE':
            self.state = 'BOARD_CHECK'
        elif self.state == 'BOARD_CHECK' and self.arm_released and self.arm_count >= self.long_press:
            self.state = 'ARMED_SAFE'
        elif self.state == 'ARMED_SAFE' and self.cal_released and self.cal_count >= self.long_press:
            self.state = 'CAL_SPARSE'
        elif self.state == 'CAL_SPARSE' and complete:
            self.state = 'CAL_QUALITY_GATE'
        elif self.state == 'CAL_QUALITY_GATE':
            self.state = 'CAL_READY' if quality else 'FAULT_LATCHED'
        elif self.state == 'CAL_READY' and trap:
            self.state = 'IDLE_TRAP'
        elif self.state == 'IDLE_TRAP' and motion:
            self.state = 'MOTION_EXEC'
        elif self.state == 'MOTION_EXEC' and done:
            self.state = 'IDLE_TRAP'
        self.arm_count = min(self.long_press, self.arm_count+1) if arm and self.arm_released else 0
        self.cal_count = min(self.long_press, self.cal_count+1) if cal and self.cal_released else 0
        if not arm:
            self.arm_released = True
        if not cal:
            self.cal_released = True
        self.age = self.age+1 if self.state in ('BOARD_CHECK', 'ARMED_SAFE', 'CAL_SPARSE', 'CAL_QUALITY_GATE') else 0
        return self.state

    @property
    def emit(self):
        return self.state in ('CAL_SPARSE', 'IDLE_TRAP', 'MOTION_EXEC')
