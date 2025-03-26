class Character:
    """
    Represents a player character in Masters Quarterback Simulation.
    
    Attributes:
        first_name (str): The player's first name.
        last_name (str): The player's last name.
        jersey (int): The player's jersey number.
        attributes (Attributes): The player's attribute set (to be assigned later).
    """
    
    def __init__(self, first_name: str, last_name: str, jersey: int):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.jersey = jersey
        # Placeholder for attributes; will be assigned later.
        self.attributes = None

    def set_attributes(self, attributes_object):
        """
        Assign an Attributes object to the character.
        
        Args:
            attributes_object: An instance of the Attributes class containing the 10 attribute values.
        """
        self.attributes = attributes_object

    def __str__(self):
        base_info = f"{self.first_name} {self.last_name} (Jersey #{self.jersey})"
        if self.attributes:
            return f"{base_info}\nAttributes:\n{self.attributes}"
        else:
            return base_info
