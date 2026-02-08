import numpy as np
from haxballgym.utils.state_setters import StateSetter
from ursinaxball import Game
from ursinaxball.objects.base.disc_object import Disc


class RandomState(StateSetter):
    def __init__(self):
        super().__init__()
        self._rng = np.random.default_rng()

    def get_valid_position(
        self, width: float, height: float, radius: float, placed: list[Disc]
    ):
        max_attempts = 100
        for _ in range(max_attempts):
            pos = np.array(
                [
                    self._rng.uniform(-width + radius, width - radius),
                    self._rng.uniform(-height + radius, height - radius),
                ],
                dtype=float,
            )

            for other in placed:
                if np.linalg.norm(pos - other.position) < (radius + other.radius):
                    break
            else:
                return pos

        return pos

    def reset(self, game: Game, save_recording: bool):
        game.reset(save_recording)
        width = game.stadium_game.width
        height = game.stadium_game.height
        ball, *placed = game.stadium_game.discs

        ball.position = self.get_valid_position(width, height, ball.radius, placed)
        placed.append(ball)

        for player in game.players:
            player.disc.position = self.get_valid_position(
                width, height, player.disc.radius, placed
            )
            placed.append(player.disc)
