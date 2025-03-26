from Character import Character
from Attributes import Attributes

class GameEngine:
    """
    The GameEngine class manages the high school phase of Masters Quarterback Simulation.
    It handles:
      - Collecting cosmetic information (name, jersey number)
      - Presenting and selecting overall presets
      - Creating and assigning attributes to the Character based on the preset choice
    """
    
    def __init__(self):
        self.character = None

    def create_character(self):
        """
        Collects cosmetic information and creates a Character instance.
        """
        print("Welcome to Masters Quarterback Simulation: High School Phase")
        
        # Collect cosmetic information.
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        
        # Validate jersey number input.
        while True:
            jersey_input = input("Enter your jersey number (1-19): ").strip()
            if jersey_input.isdigit():
                jersey = int(jersey_input)
                if 1 <= jersey <= 19:
                    break
                else:
                    print("Error: Jersey number must be between 1 and 19.")
            else:
                print("Error: Please enter a valid number.")
        
        # Create the character.
        self.character = Character(first_name, last_name, jersey)
    
    def select_preset(self):
        """
        Displays the available overall presets and allows the player to select one.
        Returns the selected preset name.
        """
        presets = [
            "First Time in Pads",
            "Madden Enthusiast",
            "Flag Football Starter",
            "Pop Warner Legend"
        ]
        
        print("\nSelect your starting overall preset:")
        for i, preset in enumerate(presets, start=1):
            print(f"  {i}. {preset}")
        
        while True:
            choice = input("Enter the number corresponding to your preset: ").strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(presets):
                    return presets[index]
            print("Invalid selection. Please try again.")
    
    def assign_attributes(self, preset_name: str):
        """
        Creates an Attributes instance from the preset and assigns it to the character.
        
        Args:
            preset_name (str): The name of the preset chosen by the player.
        """
        # Create Attributes from the preset.
        attributes = Attributes.from_preset(preset_name)
        # Attach the Attributes instance to the Character.
        self.character.set_attributes(attributes)
    
    def show_character_info(self):
        """
        Displays the full character details including cosmetic info and attributes.
        """
        print("\nCharacter Setup Complete!")
        print("-------------------------")
        print(self.character)
    
    def run(self):
        """
        Executes the game flow for the high school phase.
        """
        self.create_character()
        preset = self.select_preset()
        self.assign_attributes(preset)
        self.show_character_info()
        # Future expansion: insert further narrative or game logic here.

