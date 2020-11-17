import json
import keyword


class FromJson:
    """
    Turns json-format into dict
    """
    def __init__(self, dic):
        for key, value in dic.items():
            if keyword.iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = FromJson(value)
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return str(self.__dict__)


class ColorizeMixin:
    """
    Prints colored output
    """
    def __init__(self):
        self.repr_color_code = 33

    def __str__(self):
        return f"\033[1;{self.repr_color_code};40m {self.__repr__()} \033[m\n"


class Advert(ColorizeMixin):
    """
    Stores advertisement with attributes
    """
    def __init__(self, dic):
        super().__init__()
        attrs = FromJson(dic).__dict__
        if "price" in attrs:
            self.price = attrs["price"]
        self.__dict__.update(attrs)

    @property
    def price(self):
        if "price" not in self.__dict__:
            return 0
        else:
            return self.__dict__["price"]

    @price.setter
    def price(self, price_new):
        if price_new < 0:
            raise ValueError("price must be >= 0")
        self._price = price_new

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
    lesson_str = """{
        "title": "python",
        "class": "programming",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.price)
    print(lesson_ad.class_)
    print(lesson_ad)
