class Counter:
    def __init__(self):
        self.count = 0

    def set_count(self, num):
        self.count += num

    def increment(self):
        self.count +=1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def report(self):
        return f"Counter: {self.count}"
