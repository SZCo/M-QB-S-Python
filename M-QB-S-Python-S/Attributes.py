class Attributes:
    """
    Represents the 10 attribute categories for a quarterback.
    
    Attributes (each is an integer between 0 and 5):
        Speed, Agility, Pass Accuracy Short, Pass Accuracy Medium, 
        Pass Accuracy Deep, Pass Power, Pass with Pressure, 
        Pass on the Run, Awareness, Durability.
    """
    
    # Define the attribute categories in a fixed order
    CATEGORIES = [
        "Speed",
        "Agility",
        "Pass Accuracy Short",
        "Pass Accuracy Medium",
        "Pass Accuracy Deep",
        "Pass Power",
        "Pass with Pressure",
        "Pass on the Run",
        "Awareness",
        "Durability"
    ]
    
    def __init__(self, distribution: dict):
        """
        Initialize with a dictionary mapping category names to their values.
        """
        self.distribution = distribution

    def __str__(self):
        lines = []
        for category in self.CATEGORIES:
            value = self.distribution.get(category, 0)
            lines.append(f"{category}: {value}")
        return "\n".join(lines)

    @classmethod
    def from_preset(cls, preset_name: str):
        """
        Create an Attributes instance from a given preset.
        
        Presets:
            - "First Time in Pads": overall = 10, evenly distributed.
            - "Madden Enthusiast": overall = 15, focus on non-physical 
              attributes (Pass Accuracy Short, Pass Accuracy Medium, 
              Pass Accuracy Deep, Awareness).
            - "Flag Football Starter": overall = 25, evenly distributed.
            - "Pop Warner Legend": overall = 40, evenly spread with focus on 
              physical attributes (Speed, Agility, Pass Power, Durability).
              
        Returns:
            An instance of Attributes with the distributed values.
            
        Raises:
            ValueError if the preset name is not recognized.
        """
        preset_name = preset_name.strip().lower()
        distribution = {cat: 0 for cat in cls.CATEGORIES}

        if preset_name == "first time in pads":
            overall = 10
            # Even distribution: each category gets overall//10 points
            base = overall // 10  # 1 point each
            for cat in cls.CATEGORIES:
                distribution[cat] = base
            # No remainder in this case.
            
        elif preset_name == "madden enthusiast":
            overall = 15
            base = overall // 10  # 1 point each (since 15//10 is 1)
            remainder = overall - (base * 10)  # 15 - 10 = 5 extra points
            
            # First, assign the baseline to all categories.
            for cat in cls.CATEGORIES:
                distribution[cat] = base

            # Focus on non-physical attributes.
            focus = ["Pass Accuracy Short", "Pass Accuracy Medium", "Pass Accuracy Deep", "Awareness"]
            
            # First, allocate bonus point to each focus category (if possible) from the remainder.
            for cat in focus:
                if remainder > 0 and distribution[cat] < 5:
                    distribution[cat] += 1
                    remainder -= 1
                    
            # Distribute any remaining points sequentially over all categories (without exceeding 5).
            for cat in cls.CATEGORIES:
                if remainder <= 0:
                    break
                if distribution[cat] < 5:
                    distribution[cat] += 1
                    remainder -= 1
                    
        elif preset_name == "flag football starter":
            overall = 25
            base = overall // 10  # 2 points each (since 25//10 = 2)
            remainder = overall - (base * 10)  # 25 - 20 = 5
            
            for cat in cls.CATEGORIES:
                distribution[cat] = base
            # Distribute remaining points sequentially over categories, ensuring max is 5.
            for cat in cls.CATEGORIES:
                if remainder <= 0:
                    break
                if distribution[cat] < 5:
                    distribution[cat] += 1
                    remainder -= 1
                    
        elif preset_name == "pop warner legend":
            overall = 40
            # For this preset, we want a physical focus on: Speed, Agility, Pass Power, Durability.
            focus = ["Speed", "Agility", "Pass Power", "Durability"]
            
            # We'll assign focus categories the max (5) and then determine the remaining for non-focus.
            for cat in cls.CATEGORIES:
                if cat in focus:
                    distribution[cat] = 5
                else:
                    distribution[cat] = 0
            
            # Total allocated so far: 5*4 = 20.
            remaining = overall - (5 * len(focus))  # 40 - 20 = 20.
            # Non-focus categories count = 6.
            # We need to distribute 20 points among these 6 categories.
            # The even baseline for non-focus: 20 // 6 = 3, remainder = 20 - (3*6) = 2.
            non_focus = [cat for cat in cls.CATEGORIES if cat not in focus]
            base = remaining // len(non_focus)  # 3
            rem = remaining - (base * len(non_focus))  # 2
            
            for cat in non_focus:
                distribution[cat] = base
            # Distribute the remaining extra points sequentially in non-focus order.
            for cat in non_focus:
                if rem <= 0:
                    break
                # Ensure that even non-focus does not exceed 5.
                if distribution[cat] < 5:
                    distribution[cat] += 1
                    rem -= 1

        else:
            raise ValueError(f"Unrecognized preset: {preset_name}")
            
        return cls(distribution)
