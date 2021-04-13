runic_dict = {

    "nd": "\U000016EF",
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
    "j": "\U000016B3",  # не совсем верная руна, но самая близкая к нужной. Та же, что и "С"
    "k": "\U000016B4",
    "l": "\U000016C5",
    "m": "\U000016D2",
    "n": "\U000016d8",
    "o": "\U0000039b",
    "p": "\U000016b9",
    # "q": "?", ни в одном из толкиенских алфавитов нет буквы q,
    # чем бы заменить?
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

syllable_list = []
word = input("Введите слово или фразу на эреборском наречии Кхуздула: ")
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
print(f"{initial_word.title()} в написании Эреборскими рунами будет выглядеть так: \n{word}")
