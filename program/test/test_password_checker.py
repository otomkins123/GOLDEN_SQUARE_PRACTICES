from lib.password_checker import *
import pytest # pyright: ignore[reportMissingImports]

def test_valid_password():
    password_checker = PasswordChecker()
    result = password_checker.is_valid("Valid1@password")
    assert result == True

# Individual tests for each validation rule
def test_empty_password_raises_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.is_valid("")
    error_message = str(e.value)
    assert error_message == "Invalid password, cannot be empty."

def test_short_password_raises_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.is_valid("Short1@")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_without_special_character_raises_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.is_valid("NoSpecial1")
    error_message = str(e.value)
    assert error_message == "Invalid password, must include at least one special character (!@$%&`)."

def test_password_without_number_raises_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.is_valid("NoNumber@")
    error_message = str(e.value)
    assert error_message == "Invalid password, must include at least one number."

def test_password_without_uppercase_raises_exception():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.is_valid("nouppercase1@")
    error_message = str(e.value)
    assert error_message == "Invalid password, must include at least one uppercase letter."