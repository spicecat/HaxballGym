import numpy as np
from ursinaxball import Game

from haxballgym.utils.state_setters import StateSetter


class RandomState(StateSetter):
    def __init__(self):
        super().__init__()
        self._rng = np.random.default_rng()

    def reset(self, game: Game, save_recording: bool):
        game.reset(save_recording)
        width = game.stadium_game.width
        height = game.stadium_game.height
        for disc in game.stadium_game.discs:
            disc.position = np.array(
                [
                    self._rng.uniform(-width, width),
                    self._rng.uniform(-height, height),
                ],
                dtype=float,
            )
