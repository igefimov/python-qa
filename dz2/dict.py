import pytest

class TestDict:

    test_data = [{'pear': 9}, {'cherry': 12}, {'plumb': 4}]
    myDict = {'peach': 15, 'blueberry': 23, 'orange': 10, 'apple': '7'}

    def test_get_method(self):
        assert self.myDict.get('orange') == 10, "Price of orange is 10"

    def test_has_key_method(self):
        assert self.myDict.has_key('peach'), "peach is present in the price list"

    def test_copy_method(self):
        assert self.myDict == self.myDict.copy(), "Original dict is equal with its copy"

    @pytest.mark.parametrize("x", test_data)
    def test_update_method(self, x):
        self.myDict.update(x)
        print(self.myDict)
        assert self.myDict[x.keys()[0]] == x.values()[0], "{0} is in the myDict".format(x)

    def test_clear_method(self):
        self.myDict.clear()
        assert len(self.myDict) == 0, "myDict has 0 elements"
