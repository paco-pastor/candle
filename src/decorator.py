from main import Candle

# TODO LIST
# [ ] Raise exception with personnalized logs, dont continue the program
# [ ] File with minimal logs, file with complete logs
# [ ] Log files separation into folders depending on code location
# [ ] .candle or .yml config file instead of manual config


def candle(entity):
    if isinstance(entity, type):
        
        def wrapper(entity):
            for attr in entity.__dict__:
                if callable(getattr(entity, attr)):
                    setattr(entity, attr, candle(getattr(entity, attr)))
            return entity
        return wrapper(entity)
    
    if not isinstance(entity, type):
        def wrapper(*args, **kwargs):
            try:
                return entity(*args, **kwargs)
            except Exception as e:
                # raise # for debug
                Candle().error(f"Erreur dans {entity.__name__}" + str(e))
        return wrapper



# Exemple d'utilisation du décorateur avec une fonction
@candle
def ma_fonction():
    a = []
    print(a[1])

@candle
class MaClasse:

    def division(self, a, b):
        return a / b


ma_fonction()
instance = MaClasse()
a = instance.division(1,0)