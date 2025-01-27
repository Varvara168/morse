MorseCode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.-', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}


def encode_to_morse(text):

    morse_code = ""
    text = text.upper()
    for char in text:
        if char != ' ':
            if char in MorseCode:
                morse_code += MorseCode[char] + " "
            else:
                return
        else:
            morse_code += "  "
    return morse_code.strip()




def main():
    while True:
        action = input().lower()
        if action == 'q':
            break
        elif action == 'e':
            text = input()
            encoded_text = encode_to_morse(text)
            print(encoded_text)
        elif action == 'd':
            morse_code = input()
            decoded_text = decode_from_morse(morse_code)
            print(decoded_text)

