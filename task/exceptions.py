class WrongCityNameError(Exception):
    """Raised when input value is not valid"""
    def __init__(self, message):
        self.message = message
