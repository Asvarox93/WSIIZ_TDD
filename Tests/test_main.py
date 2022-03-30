import pytest
from pytest import mark
from main import palindrome

@mark.palindrome
class PalindromeTests:
    @mark.input
    def test_palindrom_function_is_exist(self):
        try:
            from main import palindrome
            pal = palindrome
            assert True
        except:
            assert False

    def test_palindrom_args_is_array(self):
        """Test that exception is raised for invalid args"""
        with pytest.raises(ValueError):
            assert palindrome("Test")
            assert palindrome(1)

    def test_palindrom_array_len_more_then_1(self):
        """Test that input array is longer then 1 element"""
        with pytest.raises(ValueError):
            assert palindrome(['test',])

    def test_palindrom_array_not_contains_numbers(self):
        """Test that arrays element is not a number"""
        with pytest.raises(ValueError):
            assert palindrome(['test', 1])
            assert palindrome(['test', "1"])
