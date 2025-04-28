class Tile:
    def __init__(self, x: int, y: int, resource: str, dice_number: int, texture: str):
        self.x = x
        self.y = y
        self.resource = resource
        self.dice_number = dice_number
        self.texture = texture
        self.frequency = (
            5
            if dice_number == 6 or dice_number == 8
            else (
                4
                if dice_number == 5 or dice_number == 9
                else (
                    3
                    if dice_number == 4 or dice_number == 10
                    else (
                        2
                        if dice_number == 3 or dice_number == 11
                        else 1 if dice_number == 2 or dice_number == 12 else 0
                    )
                )
            )
        )

        self.contains_robber = False if resource != "desert" else True

    def __str__(self):
        # Override the string representation of the tile, for printing to the console
        return f"Tile({self.x}, {self.y}, {self.resource}, {self.dice_number})"
