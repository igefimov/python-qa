import pytest


class TestSet:
    test_data = [
        {"yes", "no", "MAYBE"},
        {"yes", "no", "Maybe"}
    ]
    mySet = {"yes", "no", "maybe"}

    def test_add_method(self):
        self.mySet.add("probably")
        assert len(self.mySet) == 4, "Should be 4 elements in mySet"

    def test_pop_method(self):
        assert self.mySet.pop() == "maybe", "Maybe was last element in mySet"
        assert len(self.mySet) == 3, "Now length of mySet is 3"

    def test_discard_method(self):
        self.mySet.discard("no")
        for i in self.mySet:
            assert i != "no", "'no' element is not present anymore"

    @pytest.mark.parametrize("x", test_data)
    def test_update_method(self, x):
        self.mySet.update(x)
        assert x.pop() in self.mySet

    def test_clear_method(self):
        self.mySet.clear()
        assert len(self.mySet) == 0, "Length of mySet is 0"
