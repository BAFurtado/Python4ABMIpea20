

class Posto:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def definir_preco(self):
        pass

    def __repr__(self):
        return f'Posto no Quadra {self.x}, {self.y}'