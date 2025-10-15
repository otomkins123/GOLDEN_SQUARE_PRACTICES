from lib.string_builder import *

def test_initial_length_is_zero():
    string_builder = StringBuilder()
    result = string_builder.length()
    assert result == 0

def test_add_increases_length():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.length()
    assert result == 5

def test_reset_sets_length_to_zero():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.reset()
    result = string_builder.length()
    assert result == 0

def test_return_string_returns_current_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.return_string()
    assert result == "Hello"

def test_return_upper_returns_uppercase_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.return_upper()
    assert result == "HELLO"

def test_return_lower_returns_lowercase_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.return_lower()
    assert result == "hello"

def test_return_reversed_returns_reversed_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.return_reversed()
    assert result == "olleH"

def test_is_palindrome_identifies_palindromes():
    string_builder = StringBuilder()
    string_builder.add("Racecar")
    result = string_builder.is_palindrome()
    assert result == True

def test_is_palindrome_identifies_non_palindromes():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    result = string_builder.is_palindrome()
    assert result == False

def test_count_vowels_counts_vowels_correctly():
    string_builder = StringBuilder()
    string_builder.add("Hello World")
    result = string_builder.count_vowels()
    assert result == 3

def test_count_vowels_with_no_vowels():
    string_builder = StringBuilder()
    string_builder.add("Rhythm")
    result = string_builder.count_vowels()
    assert result == 0

def test_add_multiple_times():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(" ")
    string_builder.add("World")
    result = string_builder.return_string()
    assert result == "Hello World"