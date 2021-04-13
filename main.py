runic_dict = {

    "ch": "\U000016b3",
    "nd": "\U000016EF",
    "qu": "\U000016AA",
    "a": "\U000016A2",
    "â": "\U000016A2",
    "b": "\U000016B1",
    "c": "\U000016B3",
    "d": "\U000016A8",
    "e": "\U000016BA",
    "f": "\U000016E9",
    "g": "\U000016A0",
    "h": "\U000016CC",
    "i": "\U000016C1",
    "j": "\U000016B3",  # The exact rune inexistent in utf-8, using the most resembling one (same as "C")
    "k": "\U000016B4",
    "l": "\U000016C5",
    "m": "\U000016D2",
    "n": "\U000016d8",
    "o": "\U0000039b",
    "p": "\U000016b9",
    # "q": "?", none of Tolkien's alphabets uses q as a letter, any ideas how to work it around? 
    "q": "",
    "r": "\U000016CF",
    "s": "\U000003bb",
    "t": "\U000016DA",
    "u": "\U000016DF",
    "v": "\U000016C4",
    "w": "\U000016DC",
    "x": "\U000016EA",
    "y": "\U000016CB",
    "z": "\U000016DD",
    " ": " ",
}


word = input("Enter a word or a pharse in Erebor version of Khuzdul: ")
# can be used as a sample: 
# word = "baruk khazad khazad aimenu 
initial_word = word
i = 0
for length in range(i, len(word) - 1):
    syllable = word[i:i + 2]
    if syllable in runic_dict:
        replacer = runic_dict[syllable]
        word = word.replace(syllable, replacer)
    i += 1

for i in word:
    if i in runic_dict:
        word = word.replace(i, runic_dict[i])
print(f"{initial_word.title()} in runes of Erebor will be: \n{word}")
