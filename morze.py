MORSE = {
    ".-": "a",    "-...": "b",    "-.-.": "c",
    "-..": "d",    ".": "e",    "..-.": "f",
    "--.": "g",    "....": "h",    "..": "i",
    ".---": "j",    "-.-": "k",    ".-..": "l",
    "--": "m",    "-.": "n",    "---": "o",
    ".--.": "p",    "--.-": "q",    ".-.": "r",
    "...": "s",    "-": "t",    "..-": "u",
    "...-": "v",    ".--": "w",    "-..-": "x",
    "-.--": "y",    "--..": "z" 
}

sozlar = input("Morse kodini yozing: ")
lst = sozlar.split(" ")
result = ""

for i in lst:
    if i in MORSE:
        result += MORSE[i]
    else:
        result += "?"

print("Natija:", result)