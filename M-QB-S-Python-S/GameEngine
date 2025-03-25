from Character import Character
from Scene import Scene
# GameEngine Class: Orchestrates character creation, scene setup, and game flow.
class GameEngine:
    def __init__(self):
        self.character = None
        self.scenes = {}

    def create_character(self):
        print("Welcome to QB Road to Glory!")
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        jersey = self.get_valid_jersey()
        self.character = Character(first_name, last_name, jersey)
        print(f"\nCharacter created: {self.character}\n")

    def get_valid_jersey(self):
        while True:
            jersey_input = input("Enter your jersey number (1-19): ").strip()
            if jersey_input.isdigit():
                jersey = int(jersey_input)
                if 1 <= jersey <= 19:
                    return jersey
                else:
                    print("Error: Jersey number must be between 1 and 19.")
            else:
                print("Error: Please enter a valid number.")

    def setup_scenes(self):
        # Setting up a simple introduction scene.
        self.scenes["intro"] = Scene(
            "Let the journey begin! Are you ready for your first challenge?",
            choices={"yes": "Proceed to training", "no": "Quit game"}
        )

    def run(self):
        self.create_character()
        self.setup_scenes()
        current_scene_key = "intro"
        
        while current_scene_key in self.scenes:
            scene = self.scenes[current_scene_key]
            scene.display()

            # End loop if no further choices.
            if not scene.choices:
                print("\nThe End.")
                break

            choice = input("\nWhat is your decision? ").strip().lower()

            # In this simple example, we don't loop back or have multiple scenes.
            if choice in scene.choices:
                print(f"\nYou chose: {scene.choices[choice]}")
                # For this example, we'll exit after one decision.
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    engine = GameEngine()
    engine.run()


if __name__ == "__main__":
    main()