import os
import sys
import importlib
import builtins

class Tkinit:
    @classmethod
    def init(cls):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        models_dir = os.path.join(root_dir, "src", "models")

        # Asegurarse de que src esté en sys.path
        if root_dir not in sys.path:
            sys.path.insert(0, root_dir)

        # Importar todas las clases de src.models y exponerlas en builtins
        for file in os.listdir(models_dir):
            if file.endswith(".py") and not file.startswith("__"):
                module_name = file[:-3]  # 'Label.py' → 'Label'
                module = importlib.import_module(f"src.models.{module_name}")
                for attr in dir(module):
                    obj = getattr(module, attr)
                    if isinstance(obj, type):
                        setattr(builtins, attr, obj)