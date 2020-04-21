from iconservice import *
from .scorelib.id_factory import *

TAG = 'HelloWorld'


class HelloWorld(IconScoreBase, IdFactory):
    _NAME = "helloworld"

    def __init__(self, db: IconScoreDatabase) -> None:
        name = HelloWorld._NAME
        self._uid = VarDB(f'{name}_uid', db, int)
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    # ================================================
    #  Internal methods
    # ================================================
    def _set_game_id(self) -> int:
        return self.get_uid()

    # ================================================
    #  External methods
    # ================================================
    @external
    def set_game_id(self) -> int:
        return self._set_game_id()

    @external(readonly=True)
    def name(self) -> str:
        return "HelloWorld"

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
