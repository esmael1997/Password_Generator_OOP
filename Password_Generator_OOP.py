from abc import ABC, abstractmethod
import random
class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass
        
class LettersPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = ''.join(random.choice(letters) for _ in range(20))
        return password
    
class DigitsPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        digits = "0123456789"
        password = ''.join(random.choice(digits) for _ in range(20))
        return password
    
class AlphaNumericPasswordGenerator(PasswordGenerator):
    
    def generate(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        

        Chars = letters + digits
        password = ''.join(random.choice(Chars) for _ in range(20))
        return password
    
def generate_all_passwords(generators):
    for gen in generators:
        print(f"{gen.__class__.__name__}: {gen.generate()}")
        
        
generators = [LettersPasswordGenerator(), DigitsPasswordGenerator(), AlphaNumericPasswordGenerator()]
generate_all_passwords(generators)
            
alphanum_gen = AlphaNumericPasswordGenerator()
print(alphanum_gen.generate())    
