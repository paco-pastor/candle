from main import Candle

# TODO raise exception with personnalized logs, dont continue the program
# FIXME MaClasse() takes no arguments

def candle(entity):
    def candle_func(*args, **kwargs):
            try:
                return entity(*args, **kwargs)
            except Exception as e:
                raise # for debug
                Candle().error(f"Erreur dans {entity.__name__}"+str(e))

    if isinstance(entity, type):
        class CandleClass(entity):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                print("\nCLASSE AVEC DECORATEUR\n")
            
            def __getattribute__(self, name):
                print(name)
                obj = super().__getattribute__(name)
                if callable(obj):
                    print("Méthode décorée appelée")
                    setattr(self, name, candle_func(obj))
                return obj
        
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

# Exemple d'utilisation du décorateur avec une classe
@candle
class MaClasse:

    def division(self, a, b):
        return a / b



instance = MaClasse()

instance.division(1, 0)
