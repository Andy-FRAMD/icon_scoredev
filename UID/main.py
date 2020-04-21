from iconservice import *

TAG = 'UIDGen'


class UIDGenerator(IconScoreBase):
    _NAME = "UIDGenerator"

    def __init__(self, db: IconScoreDatabase) -> None:
        self._name = UIDGenerator._NAME
        self._uid = VarDB(f'{self._name}_uid', db, int)
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    # ================================================
    #  Internal methods
    # ================================================
    # def _set_game_id(self):
    #    uid = self._uid.get()
    #    self._uid.set(uid + 1)

    # ================================================
    #  External methods
    # ================================================
    @external
    def set_game_id(self) -> int:
        self._uid.set(self._uid.get() + 1)
        return self._uid.get()

    @external(readonly=True)
    def get_game_id(self) -> int:
        self._uid.get()

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
