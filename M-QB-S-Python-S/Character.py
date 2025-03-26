# Character Class: Manages player information.
class Character:
    def __init__(self, first_name, last_name, jersey):
        self.first_name = first_name
        self.last_name = last_name
        self.jersey = jersey

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Jersey Number: {self.jersey}"