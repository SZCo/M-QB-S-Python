# Scene Class: Represents a scene with narrative text and available choices.
class Scene:
    def __init__(self, description, choices=None):
        self.description = description
        self.choices = choices or {}

    def display(self):
        print("\n" + self.description)
        if self.choices:
            print("\nAvailable choices:")
            for key, text in self.choices.items():
                print(f" - {key}: {text}")
