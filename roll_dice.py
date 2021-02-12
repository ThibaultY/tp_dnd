"""
Créateur : Yohan Thibault
Groupe :407
Ce prgramme est une commande de roll dice.
"""


class RollDice:
    def __init__(self, text_input):
        """
        This is going to roll dice with the amount of face and dice wanted.
        :param text_input: How many dice with x faces, xDy
        :return: The sum of all the dices
        """
        import random
        text_input = text_input.upper().split("D")
        # check for invalid entries
        if len(text_input) != 2:
            print("********UN SEUL D")
        elif not text_input[0].isdigit() or not text_input[1].isdigit():
            print("********Il faut que vos entrés soient des nombres.")

        dice_amount = int(text_input[0])
        face_amount = int(text_input[1])
        self.values = [random.randint(1, face_amount) for i in range(dice_amount)]

        if dice_amount == 1:  # If it's only one dice we want this result.
            return self.values[0]

    def sum(self):
        return sum(self.values)

    def keep_max(self, amount):
        """
        This will keep the highest numbers
        :param amount: the amount of numbers you want to keep
        :return: Return the list of the biggest numbers.
        """
        old_list = self.values
        new_list = []
        for i in range(amount):
            new_list.append(max(old_list))
            old_list.pop(old_list.index(max(old_list)))
        return sum(new_list)
