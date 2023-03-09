from dino_runner.utils.constants import HEART_TYPE

from dino_runner.components.power_ups.power_up import PowerUp

class Heart(PowerUp):
    def __init__(self, image):
        super().__init__(image)
        self.type = HEART_TYPE