class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def length(self):
        return len(self.str)
    
    def reset(self):
        self.str = ""

    def return_string(self):
        return self.str
    
    def return_upper(self):
        return self.str.upper()
    
    def return_lower(self):
        return self.str.lower()

    def return_reversed(self):
        return self.str[::-1]
    
    def is_palindrome(self):
        cleaned_str = ''.join(char.lower() for char in self.str if char.isalnum())
        return cleaned_str == cleaned_str[::-1]
    
    def count_vowels(self):
        vowels = 'aeiouAEIOU'
        return sum(1 for char in self.str if char in vowels)