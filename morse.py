class MorseCode:
    def __init__(self, text):
        self.text = text
        self.morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
        }

    def encrypt(self):
        result = []
        for char in self.text.upper():
            if char in self.morse_code:
                result.append(self.morse_code[char])
        return ' '.join(result)

    def decrypt(self):
        result = []
        for code in self.text.split():
            for char, morse_code in self.morse_code.items():
                if code == morse_code:
                    result.append(char)
                    break
            else:
                raise ValueError("Invalid Morse code")
        return ''.join(result)
