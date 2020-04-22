from iconservice import *
from ..scorelib.id_factory import *


# ================================================
#  Exception
# ================================================


class GameFactory(IdFactory):
    _NAME = 'GAME_FACTORY'

    def __init__(self, db: IconScoreDatabase):
        name = GameFactory._NAME
        super().__init__(name, db)
        self._name = name
        self._db = db

    def create_game(self, difficulty: int) -> int:
        game_id = self.get_uid()
        game = Game(game_id, self._db)
        game.difficulty[game_id] = difficulty
        game.row[game_id] = 0
        game.status[game_id] = GameStatus.IN_PROGRESS
        return game_id


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

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def row(self):
        return self._row

    @property
    def status(self):
        return self._status


