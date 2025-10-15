class PasswordChecker:

    def __init__(self):
        pass

    def is_valid(self, password):
        if not password:
            raise Exception("Invalid password, cannot be empty.")
        if len(password) < 8:
            raise Exception("Invalid password, must be 8+ characters.")
        if not any((c in "!@$%&`") for c in password):
            raise Exception("Invalid password, must include at least one special character (!@$%&`).")
        if not any(char.isdigit() for char in password):
            raise Exception("Invalid password, must include at least one number.")
        if not any(char.isupper() for char in password):
            raise Exception("Invalid password, must include at least one uppercase letter.")
        else:   
            return True