import pytest

from desim.signal import Signal, SIG_START_DEFAULT, SIG_UNDEFINED


class TestCreate:
    @pytest.fixture(autouse=True)
    def sig(self):
        return Signal("s1")

    def test(self, sig):
        assert sig.name == "s1"
        assert sig.value == SIG_START_DEFAULT
        assert sig.previous_value == SIG_UNDEFINED
        assert sig.connected_clients == []
        assert sig._trace_connection is None

    @pytest.mark.parametrize("val", ["one", 17, 3.21, None, "no-assign"])
    def test_repr(self, sig, val):
        if val != "no-assign":
            sig.update(0, val)
        else:
            val = 0  # original expected
        expect = f"Signal<s1 = {val!r}>"
        print(f"Expected: {expect}")
        assert repr(sig) == expect

    @pytest.mark.parametrize("val", ["one", 17, 3.21])
    def test_update(self, sig, val):
        sig.update(0, val)
        assert sig.value == val
