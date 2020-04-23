from iconservice import *
from ..scorelib.id_factory import *
from ..scorelib.utils import *


# ================================================
#  Exception
# ================================================

class InvalidDifficulty(Exception):
    pass


class GameFactory(IdFactory):
    _NAME = 'GAME_FACTORY'

    def __init__(self, db: IconScoreDatabase):
        name = GameFactory._NAME
        super().__init__(name, db)
        self._name = name
        self._db = db

    def create_game(self, difficulty: int) -> dict:
        game_id = self.get_uid()
        game = Game(game_id, self._db)
        game.difficulty[game_id] = difficulty
        game.level[game_id] = 0
        game.status[game_id] = GameStatus.IN_PROGRESS
        return game_id

    def finish_game(self, game_id):
        game = Game(game_id, self._db)
        game.status[game_id] = GameStatus.GAME_OVER


class GameDifficulty:
    EASY = 0
    MEDIUM = 1
    HARD = 2


class GameStatus:
    NOT_STARTED = 0
    IN_PROGRESS = 1
    GAME_OVER = 2


class Game(object):
    _NAME = 'GAME'

    # DictDB pointer that will hold the value of the difficulty the user selected when creating a new game
    _DIFFICULTY = 'difficulty'
    # DictDB pointer that will keep track of what row the user is currently on
    _LEVEL = 'levels'
    # DictDB pointer that will keep track of the status of the game
    _GAME_STATUS = 'status'

    # ================================================
    #  Initialization
    # ================================================
    def __init__(self, uid: int, db: IconScoreDatabase):
        self._name = Game._NAME
        self._difficulty = DictDB(f'{self._name}_{self._DIFFICULTY}', db, value_type=int)
        self._level = DictDB(f'{self._name}_{self._LEVEL}', db, value_type=int)
        self._status = DictDB(f'{self._name}_{self._GAME_STATUS}', db, value_type=int)
        self._uid = uid
        self._db = db

    # ================================================
    #  Checks
    # ================================================
    @staticmethod
    def check_difficulty(difficulty: int) -> None:
        # only supports 3 difficulty levels
        if not 1 <= difficulty < 4:
            raise InvalidDifficulty

    # ================================================
    #  Public methods of the Game Class
    # ================================================
    def get_game_details(self) -> dict:
        game_id = self._uid
        status = self._status[game_id]
        difficulty = self._difficulty[game_id]
        return {
            'game_id': game_id,
            'level': self._level[game_id],
            'status': Utils.enum_names(GameStatus)[status],
            'difficulty': Utils.enum_names(GameDifficulty)[difficulty]
        }

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def level(self):
        return self._level

    @property
    def status(self):
        return self._status
