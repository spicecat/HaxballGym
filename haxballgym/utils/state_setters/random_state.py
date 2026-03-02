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

    def is_valid_position(self, disc: Disc, placed: list[Disc]) -> bool:
        for other in placed:
            if np.linalg.norm(disc.position - other.position) < (
                other.radius + disc.radius
            ):
                return False
        return True

    def randomize_position(
        self,
        width: float,
        height: float,
        disc: Disc,
        placed: list[Disc],
        max_velocity: float = 1.0,
    ):
        max_attempts = 100
        for _ in range(max_attempts):
            disc.position = np.array(
                [
                    self._rng.uniform(-width + disc.radius, width - disc.radius),
                    self._rng.uniform(-height + disc.radius, height - disc.radius),
                ],
                dtype=float,
            )
            if self.is_valid_position(disc, placed):
                break
        placed.append(disc)

        disc.velocity = np.array(
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
        self.randomize_position(width, height, ball, placed)
        for player in game.players:
            self.randomize_position(width, height, player.disc, placed)
