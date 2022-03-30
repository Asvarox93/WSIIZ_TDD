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

    @mark.input
    def test_palindrom_args_is_array(self):
        """Test that exception is raised for invalid args"""
        with pytest.raises(ValueError):
            assert palindrome("Test")
            assert palindrome(1)

    @mark.input
    def test_palindrom_array_len_more_then_1(self):
        """Test that input array is longer then 1 element"""
        with pytest.raises(ValueError):
            assert palindrome(['test',])

    @mark.input
    def test_palindrom_array_not_contains_numbers(self):
        """Test that arrays element is not a number"""
        with pytest.raises(ValueError):
            assert palindrome(['test', 1])
            assert palindrome(['test', "1"])

    @mark.value
    def test_palindrom_check_if_value_return_in_defined_pattern(self):
        """Test that returned value is a dict with key as a number of palindrome
         and value as list with this palindromes """
        test = ['test', 'ala', 'to nie palindrom', "Jeż leje lwa, paw leje lżej"]
        result_pattern = {2:['ala',"Jeż leje lwa, paw leje lżej"]}
        result = palindrome(test)
        assert result == result_pattern
