morse_to_text = {
    'a': '.-',            
    'b': '-...',            
    'c': '-.-.',            
    'd': '-..',            
    'e': '.',            
    'f': '..-.',            
    'g': '--.',            
    'h': '....',            
    'i': '..',            
    'j': '.---',            
    'k': '-.-',            
    'l': '.-..',            
    'm': '--',            
    'n': '-.',            
    'o': '---',            
    'p': '.--.',            
    'q': '--.-',            
    'r': '.-.',            
    's': '...',            
    't': '-',            
    'u': '..-',            
    'v': '...-',            
    'w': '.--',            
    'x': '-..-',            
    'y': '-.--',            
    'z': '--..',            
    '0': '-----',           ',': '--..--',
    '1': '.----',           '.': '.-.-.-',
    '2': '..---',           '?': '..--..',
    '3': '...--',           ';': '-.-.-.',
    '4': '....-',           ':': '---...',
    '5': '.....',           "'": '.----.',
    '6': '-....',           '-': '-....-',
    '7': '--...',           '/': '-..-.',
    '8': '---..',           '(': '-.--.-',
    '9': '----.',           ')': '-.--.-',
    ' ': '/',            	'_': '..--.-',
    # '\\n': '/'
}

def convertMorseToText(s):

    return (morse_to_text.get(s))


def convertTextToMorse(s):
    
    text_to_morse = {v: k for k, v in morse_to_text.items()}
    
    return (text_to_morse.get(s))