import secrets


# Apple class
class Apple:
    def __init__(self, name: str, weight: float, is_ripe: bool, size: float):
        self.name = name
        self.weight = weight
        self.is_ripe = is_ripe
        self.size = size
        self.barrel = None
        self.bottle = None

    def grind(self, bottle: "Bottle"):
        if bottle.add(self):
            self.bottle = bottle

    def harvest(self, barrel: "Barrel"):
        barrel.add(self)
        self.barrel = barrel


class Orange:
    def __init__(self, name: str, weight: float, is_ripe: bool, size: float):
        self.name = name
        self.weight = weight
        self.is_ripe = is_ripe
        self.size = size
        self.basket = None
        self.bottle = None

    def pick(self, basket: "Basket"):
        basket.add(self)
        self.basket = basket

    def squeeze(self, bottle: "Bottle"):
        if bottle.add(self):
            self.bottle = bottle


class Bottle:
    def __init__(self, price: float, size: float):
        self.price = price
        self.size = size
        self.id = secrets.token_urlsafe(5)
        self.content = []

    def add(self, juice: Orange | Apple):
        if len(self.content) < self.size:
            self.content.append(juice)
            return True
        else:
            return False


class Barrel:
    def __init__(self, price: float, size: float):
        self.price = price
        self.size = size
        self.id = secrets.token_urlsafe(5)
        self.apples = []

    def add(self, apple: Apple):
        if len(self.apples) < self.size:
            self.apples.append(apple)
            return True
        else:
            return False


class Basket:
    def __init__(self, price: float, size: float):
        self.price = price
        self.size = size
        self.id = secrets.token_urlsafe(5)
        self.oranges = []

    def add(self, orange: Orange):
        if len(self.oranges) < self.size:
            self.oranges.append(orange)
            return True
        else:
            return False


if __name__ == "__main__":
    # create containers
    basket = Basket(300, 100)
    barrel = Barrel(600, 50)

    bottle = Bottle(4, 20)

    # create oranges
    o1 = Orange("a", 4.5, True, 1)
    o2 = Orange("b", 2.3, True, 1)
    # create apples
    a1 = Apple("b", 5.2, True, 1)
    a2 = Apple("c", 7.34, True, 1)

    # pick oranges
    o1.pick(basket)
    o2.pick(basket)

    # harvest apples
    a1.harvest(barrel)
    a2.harvest(barrel)

    # squeeze oranges
    o1.squeeze(bottle)
    o1.squeeze(bottle)

    # grind apple
    a1.grind(bottle)
    a2.grind(bottle)
