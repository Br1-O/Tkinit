from abc import ABC, abstractmethod

class IWidget(ABC):
    """
        Interface for widgets in tkinter

        Methods:
            create(cls, **kwargs)
        Properties:
            instance(self):
    """
    
    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        pass

    @property
    @abstractmethod
    def instance(self):
        pass