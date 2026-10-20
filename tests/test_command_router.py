from loftia_trainer.handlers.command_router import CommandRouter


class FakePlayer:
    def __init__(self):
        self.god = False
        self.health = 0.0

    def toggle_godmode(self):
        self.god = not self.god
        return self.god

    def set_health(self, v):
        self.health = v

    def set_stamina(self, v):
        pass

    def set_gold(self, v):
        self.gold = v


class FakeInv:
    def unlock_all_slots(self):
        pass

    def duplicate_item(self, slot):
        pass


class FakeTp:
    def teleport(self, name):
        return name == "market"

    def save_position(self, name):
        class W:
            name = "x"
            x = y = z = 0.0
        return W()


def test_god_toggle():
    p = FakePlayer()
    r = CommandRouter(p, FakeInv(), FakeTp())
    assert r.dispatch("god") == "godmode=on"
    assert r.dispatch("god") == "godmode=off"


def test_unknown():
    r = CommandRouter(FakePlayer(), FakeInv(), FakeTp())
    assert "unknown" in r.dispatch("nope")