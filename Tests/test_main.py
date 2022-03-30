from pytest import mark


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