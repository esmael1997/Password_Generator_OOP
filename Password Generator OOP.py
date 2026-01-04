from abc import ABC, abstractmethod

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass
        
class LettersPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pass
    
class DigitsPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        digits = "0123456789"
        pass
    
class SymbolsPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        

        Symbols = letters + digits
        pass
    