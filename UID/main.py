from iconservice import *
from .game.game import *
from .scorelib.id_factory import *

TAG = 'UIDGen'


class UIDGenerator(IconScoreBase):
    _NAME = "UIDGenerator"

    @eventlog(indexed=1)
    def NewGameStarted(self, game_id: int) -> None:
        pass

    def __init__(self, db: IconScoreDatabase) -> None:
        self._name = UIDGenerator._NAME
        self._uid = VarDB(f'{self._name}_uid', db, int)
        self._db = db
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    # ================================================
    #  Internal methods
    # ================================================
    def _create_new_game(self, difficulty: int) -> int:
        game_factory = GameFactory(self.db)
        game_id = game_factory.create_game(difficulty)

        # trigger new game started event
        self.NewGameStarted(game_id)

    # ================================================
    #  External methods
    # ================================================
    @external
    def create_new_game(self, difficulty: int) -> None:
        self._create_new_game(difficulty)

    @external(readonly=True)
    def get_game_details(self, game_id: int) -> dict:
        game = Game(game_id, self._db)
        return game.get_game_details()

    @external
    def brick_selected(self, sq: int, row: int, difficulty: int):
        return

    @external(readonly=True)
    def name(self) -> str:
        return self._name;

    @external(readonly=True)
    def hello(self) -> str:
        Logger.info('Hello, world!', TAG)
        return "Hello"

    @payable
    def fallback(self):
        Logger.info('fallback is called', TAG)

    @external
    def tokenFallback(self, _from: Address, _value: int, _data: bytes):
        Logger.info('tokenFallback is called', TAG)
