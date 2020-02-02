import pytest


class TestString:

    test_data = [
        "12341234",
        "asdfsfsa", # test will fail
        "23423423fa34a", # test will fail
        "0193"]
    myString = "hello world!"

    def test_islower_method(self):
        assert self.myString.islower()

    def test_capitalize_method(self):
        assert self.myString.capitalize() == "Hello world!"

    def test_isalnum_method(self):
        assert not self.myString.isdigit()

    def test_upper_method(self):
        assert self.myString.upper() == "HELLO WORLD!"

    @pytest.mark.parametrize("str", test_data)
    def test_isdigit(self, str):
        assert str.isdigit()
