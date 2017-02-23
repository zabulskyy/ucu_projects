class Building:
    def __init__(self, address):
        """
        :param address: str
        """
        self.address = address


class House(Building):
    def __init__(self, address, flat):
        """
        :param address: str
        :param flat: str
        """
        super().__init__(address)
