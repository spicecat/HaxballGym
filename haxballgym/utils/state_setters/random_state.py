import numpy as np
from haxballgym.utils.state_setters import StateSetter
from ursinaxball import Game
from ursinaxball.common_values import GameState, TeamID
from ursinaxball.objects.base.disc_object import Disc


class RandomState(StateSetter):
    def __init__(self, red_percent: float = 0.5):
        super().__init__()
        self.red_percent = red_percent
        self._rng = np.random.default_rng()

    def is_valid_position(
        self, position: np.ndarray, radius: float, placed: list[Disc]
    ) -> bool:
        for other in placed:
            if np.linalg.norm(position - other.position) < (other.radius + radius):
                return False
        return True

    def get_random_position(
        self, width: float, height: float, radius: float, placed: list[Disc]
    ) -> np.ndarray:
        max_attempts = 100
        for _ in range(max_attempts):
            pos = np.array(
                [
                    self._rng.uniform(-width + radius, width - radius),
                    self._rng.uniform(-height + radius, height - radius),
                ],
                dtype=float,
            )

            if is_valid_position(pos, radius, placed):
                break

        return pos

    def get_random_velocity(self, max_velocity: float = 1.0):
        return np.array(
            [
                self._rng.uniform(-max_velocity, max_velocity),
                self._rng.uniform(-max_velocity, max_velocity),
            ],
            dtype=float,
        )

    def reset(self, game: Game, save_recording: bool):
        game.reset(save_recording)
        game.state = GameState.PLAYING
        game.team_kickoff = (
            TeamID.RED if self._rng.random() < self.red_percent else TeamID.BLUE
        )
        width = game.stadium_game.width
        height = game.stadium_game.height
        ball, *placed = game.stadium_game.discs

        ball.position = self.get_random_position(width, height, ball.radius, placed)
        ball.velocity = self.get_random_velocity()
        placed.append(ball)

        for player in game.players:
            player.disc.position = self.get_random_position(
                width, height, player.disc.radius, placed
            )
            player.disc.velocity = self.get_random_velocity()
            placed.append(player.disc)
