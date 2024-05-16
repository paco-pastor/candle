from main import Candle

# TODO raise exception with personnalized logs, dont continue the program
# FIXME MaClasse() takes no arguments


def candle(func):
    def candle_func(*args, **kwargs):
        try:
            print("RETURN")
            return func(*args, **kwargs)
        except Exception as e:
            print("EXCEPTION")
            # raise # for debug
            Candle().error(f"Erreur dans {func.__name__}" + str(e))

    if isinstance(func, type):
        print("IS CLASS")
        class CandleClass(entity):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                print("\nCLASSE AVEC DECORATEUR\n")

            def __getattribute__(self, name):
                print(name)
                obj = super().__getattribute__(name)
                if callable(obj):
                    print("Méthode décorée appelée")
                    # obj = candle_func(obj)
                    # setattr(self, name, candle_func(obj))
                return candle_func(obj)
        
        return CandleClass
        
    else:
        return candle_func


# Exemple d'utilisation du décorateur avec une fonction
# @candle
# def ma_fonction():
#     a = []
#     print(a[1])
#     print("Ma fonction originale")

# ma_fonction()


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print("-------------------------")
        return func(*args, **kwargs)
    return wrapper

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__: # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

# Exemple d'utilisation du décorateur avec une classe
@for_all_methods(candle)
class MaClasse:

    def division(self, a, b):
        print("DIVISION")
        return a / b


instance = MaClasse()
print(type(instance))
a = instance.division(1,0)
print(a, "type : ", type(a))