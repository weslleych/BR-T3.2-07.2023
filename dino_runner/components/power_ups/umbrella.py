from dino_runner.utils.constants import UMBRELLA, UMBRELLA_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class umbrella(PowerUp):
    def __init__(self):
        super().__init__(UMBRELLA, UMBRELLA_TYPE)