from loftia_trainer.utils.address import align, ptr


def test_ptr_chain():
    assert ptr(0x1000, [0x10, 0x20]) == 0x1030


def test_align():
    assert align(0x1003) == 0x1010
    assert align(0x1000) == 0x1000