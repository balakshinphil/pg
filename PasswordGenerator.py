from random import shuffle, randint

class PasswordGenerator:
    _letters: str = 'abcdefghijklmnopqrstuvwxyz'
    _letters_big: str = _letters.upper()
    _numbers: str = '0123456789'
    _symbols: str = '!@$%&*()-_=+{}[],./;:\'"\\/?'


    def __init__(self, digits_quantity, mode) -> None:
        self._set_alphabet(mode)
        self.generatePassword(digits_quantity)


    def _set_alphabet(self, mode) -> None:
        self._alphabet: str = []

        alphabet_str: str = ''
        if 'l' in mode: alphabet_str += self._letters
        if 'L' in mode: alphabet_str += self._letters_big
        if 'n' in mode: alphabet_str += self._numbers
        if 's' in mode: alphabet_str += self._symbols

        for ch in alphabet_str: self._alphabet.append(ch)
        
        shuffle(self._alphabet)
    

    def generatePassword(self, digits_quantity) -> None:
        self._password: str = ''
        for _ in range(digits_quantity):
            self._password += self._alphabet[randint(0, len(self._alphabet)-1)]
            shuffle(self._alphabet)

    
    def getPassword(self) -> str:
        return self._password
    