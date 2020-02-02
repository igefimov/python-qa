import pytest


class TestList:
    test_data = [99, 999, 9999]
    myList = [1, 2, 19, 4, 8, 3, 5, 4, 23, 0]

    def test_index_method(self):
        assert self.myList.index(4) == 3, "Object 4 is located on the third position"

    def test_sort_method(self):
        self.myList.sort()
        assert self.myList.index(min(self.myList)) == 0, "First element is the smallest from the whole list"
        assert self.myList.index(max(self.myList)) == len(self.myList) - 1, "Last element is the biggest from the whole list"

    def test_insert_method(self):
        self.myList.insert(0, 13)
        assert self.myList.index(13) == 0, "Element was inserted in the beginning of the list"

    def test_count_method(self):
        assert self.myList.count(4) == 2, "Object 4 should appear twice in the list"

    @pytest.mark.parametrize("x", test_data)
    def test_append_method(self, x):
        my_list_len = len(self.myList)
        self.myList.append(x)
        assert len(self.myList) == my_list_len + 1, "List length increased by 1"
        print "\n{0}\n".format(self.myList)
