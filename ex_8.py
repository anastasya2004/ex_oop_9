class MorseMsg:
    """
    MorseMsg class represents a Morse code message decoder capable of decoding both English and Russian languages.

    Attributes:
    eng_morse (dict): A dictionary mapping English letters to their Morse code representations.
    eng_vowels (dict): A dictionary mapping English vowels to their Morse code representations.
    eng_consonants (dict): A dictionary mapping English consonants to their Morse code representations.
    ru_morse (dict): A dictionary mapping Russian letters to their Morse code representations.
    ru_vowels (dict): A dictionary mapping Russian vowels to their Morse code representations.
    ru_consonants (dict): A dictionary mapping Russian consonants to their Morse code representations.
    coded (str): The Morse code message to be decoded.

    Methods:
    __init__(coded): Initializes the MorseMsg object with a coded message.
    eng_decode(): Decodes the Morse code message to English letters.
    ru_decode(): Decodes the Morse code message to Russian letters.
    get_vowels(lang): Gets the vowels from the Morse code message based on the specified language.
    get_consonants(lang): Gets the consonants from the Morse code message based on the specified language.
    __str__(): Returns the Morse code message stored in the object as a string.
    """

    eng_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..'}

    eng_vowels = {'A': '.-', 'E': '.', 'I': '..', 'O': '---', 'U': '..-', 'Y': '-.--'}

    eng_consonants = {'B': '-...', 'C': '-.-.', 'D': '-..', 'F': '..-.', 'G': '--.',
                      'H': '....', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
                      'N': '-.', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
                      'T': '-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Z': '--..'}

    ru_morse = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
                'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..',
                'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.',
                'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-',
                'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
                'Ш': '----', 'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-',
                'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'}

    ru_vowels = {'А': '.-', 'Е': '.', 'Ё': '.', 'И': '..',
                 'О': '---', 'У': '..-', 'Ы': '-.--', 'Э': '..-..',
                 'Ю': '..--', 'Я': '.-.-'}

    ru_consonants = {'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
                     'Ж': '...-', 'З': '--..', 'К': '-.-', 'Л': '.-..', 'М': '--',
                     'Н': '-.', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-',
                     'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
                     'Щ': '--.-', 'Ъ': '.--.-.', 'Ь': '-..-', 'Й': '.---'}

    def __init__(self, coded):
        """
        Initializes a MorseMsg object with a given coded message.

        Parameters:
        coded (str): The Morse code message to be decoded.
        """
        self.coded = coded

    def eng_decode(self):
        """
        Decodes the Morse code message to English letters.

        Returns:
        str: Decoded English message.
        """
        decoded = ''
        morse_list = self.coded.split()
        for char in morse_list:
            for key, value in MorseMsg.eng_morse.items():
                if char == value:
                    decoded += key
                    break
        return decoded

    def ru_decode(self):
        """
        Decodes the Morse code message to Russian letters.

        Returns:
        str: Decoded Russian message.
        """
        decoded = ''
        morse_list = self.coded.split()
        for char in morse_list:
            for key, value in MorseMsg.ru_morse.items():
                if char == value:
                    decoded += key
                    break
        return decoded

    def get_vowels(self, lang):
        """
        Gets the vowels from the Morse code message based on the specified language.

        Parameters:
        lang (str): The language of the Morse code message ('eng' for English, 'ru' for Russian).

        Returns:
        list: List of decoded vowels.
        """
        decoded = []
        morse_list = self.coded.split()
        if lang == 'eng':
            decoder_dict = MorseMsg.eng_vowels.items()
        if lang == 'ru':
            decoder_dict = MorseMsg.ru_vowels.items()
        for char in morse_list:
            for key, value in decoder_dict:
                if char == value:
                    decoded.append(key)
                    break
        return decoded

    def get_consonants(self, lang):
        """
        Gets the consonants from the Morse code message based on the specified language.

        Parameters:
        lang (str): The language of the Morse code message ('eng' for English, 'ru' for Russian).

        Returns:
        list: List of decoded consonants.
        """
        decoded = []
        morse_list = self.coded.split()
        if lang == 'eng':
            decoder_dict = MorseMsg.eng_consonants.items()
        if lang == 'ru':
            decoder_dict = MorseMsg.ru_consonants.items()
        for char in morse_list:
            for key, value in decoder_dict:
                if char == value:
                    decoded.append(key)
                    break
        return decoded

    def __str__(self):
        """
        Returns the Morse code message stored in the object as a string.

        Returns:
        str: The Morse code message.
        """
        return self.coded    

a = '..-. ..- -. -. -.-- . -..- . .-. ... -.-. .. ... . ...'
a_decode = MorseMsg(a)
print(a_decode)
print(a_decode.eng_decode())
print(a_decode.get_vowels('eng'))
print(a_decode.get_consonants('eng'))
b = '--- ... --- -... . -. -. --- .--. --- ... .-.. . -.. -. .. . - .-. ..'
b_decode = MorseMsg(b)
print(b_decode)
print(b_decode.ru_decode())
print(b_decode.get_vowels('ru'))
print(b_decode.get_consonants('ru'))