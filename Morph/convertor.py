import re


def convert_tam_utf2wx(text):
    unicodeValue = {}
    unicodeValue_vowels = {"\u0B85": 'a', "\u0B86": 'A', "\u0B87": 'i', "\u0B88": 'I', "\u0B89": 'u', "\u0B8A": 'U',
                           "\u0B8B": 'q', "\u0B8C": 'lq', "\u0B8F": 'e', "\u0B90": 'E', "\u0B93": 'o', "\u0B94": 'O',
                           "\u0B8D": 'EY', "\u0B8E": 'eV', "\u0B91": 'OY', "\u0B92": 'oV'}

    unicodeValue["\u0BB3"] = 'lY'
    unicodeValue["\u0BC5"] = 'EY'
    unicodeValue["\u0BB4"] = 'lYY'
    unicodeValue["\u0BA9"] = 'nY'
    unicodeValue["\u0BB1"] = 'rY'
    unicodeValue["\u0BC6"] = 'eV'
    unicodeValue["\u0BC9"] = 'OY'
    unicodeValue["\u0BCA"] = 'oV'

    unicodeValue[";"] = ';'
    unicodeValue[":"] = ':'
    unicodeValue["34"] = '\"'
    unicodeValue["39"] = '\''
    unicodeValue["44"] = ','
    unicodeValue["46"] = '.'
    unicodeValue["47"] = '/'
    unicodeValue["63"] = '?'
    unicodeValue["<"] = '<'
    unicodeValue[">"] = '>'
    unicodeValue["91"] = '['
    unicodeValue["93"] = ']'
    unicodeValue["123"] = '{'
    unicodeValue["125"] = '}'
    unicodeValue["40"] = '('
    unicodeValue["41"] = ')'
    unicodeValue["64"] = '@'
    unicodeValue["35"] = '#'
    unicodeValue["^"] = '^'
    unicodeValue["42"] = '*'
    unicodeValue["\u0BCD"] = ''
    unicodeValue["61"] = '='
    unicodeValue["43"] = '+'
    unicodeValue["\u0BE4"] = '|'
    unicodeValue["~"] = '~'
    unicodeValue["`"] = '`'
    unicodeValue["\\"] = '\\'

    unicodeValue["\u0BE6"] = '0'
    unicodeValue["\u0BE7"] = '1'
    unicodeValue["\u0BE8"] = '2'
    unicodeValue["\u0BE9"] = '3'
    unicodeValue["\u0BEA"] = '4'
    unicodeValue["\u0BEB"] = '5'
    unicodeValue["\u0BEC"] = '6'
    unicodeValue["\u0BED"] = '7'
    unicodeValue["\u0BEE"] = '8'
    unicodeValue["\u0BEF"] = '9'

    unicodeValue["\u0B85"] = 'a'
    unicodeValue["\u0BAC"] = 'b'
    unicodeValue["\u0B9A"] = 'c'
    unicodeValue["\u0BA1"] = 'd'
    unicodeValue["\u0BC7"] = 'e'
    unicodeValue["\u0B99"] = 'f'
    unicodeValue["\u0B97"] = 'g'
    unicodeValue["\u0BB9"] = 'h'
    unicodeValue["\u0BBF"] = 'i'
    unicodeValue["\u0B9C"] = 'j'
    unicodeValue["\u0B95"] = 'k'
    unicodeValue["\u0BB2"] = 'l'
    unicodeValue["\u0BAE"] = 'm'
    unicodeValue["\u0BA8"] = 'n'
    unicodeValue["\u0BCB"] = 'o'
    unicodeValue["\u0BAA"] = 'p'
    unicodeValue["\u0BC3"] = 'q'
    unicodeValue["\u0BB0"] = 'r'
    unicodeValue["\u0BB8"] = 's'
    unicodeValue["\u0B9F"] = 't'
    unicodeValue["\u0BC1"] = 'u'
    unicodeValue["\u0BB5"] = 'v'
    unicodeValue["\u0BA4"] = 'w'
    unicodeValue["\u0BA6"] = 'x'
    unicodeValue["\u0BAF"] = 'y'
    unicodeValue["\u0B81"] = 'z'

    unicodeValue["\u0BBE"] = 'A'
    unicodeValue["\u0BAD"] = 'B'
    unicodeValue["\u0B9B"] = 'C'
    unicodeValue["\u0BA2"] = 'D'
    unicodeValue["\u0BC8"] = 'E'
    unicodeValue["\u0B9E"] = 'F'
    unicodeValue["\u0B98"] = 'G'
    unicodeValue["\u0B83"] = 'H'
    unicodeValue["\u0BC0"] = 'I'
    unicodeValue["\u0B9D"] = 'J'
    unicodeValue["\u0B96"] = 'K'
    unicodeValue["\u0B82"] = 'M'
    unicodeValue["\u0BA3"] = 'N'
    unicodeValue["\u0BCC"] = 'O'
    unicodeValue["\u0BAB"] = 'P'
    unicodeValue["\u0BC4"] = 'Q'
    unicodeValue["\u0BB7"] = 'R'
    unicodeValue["\u0BB6"] = 'S'
    unicodeValue["\u0BA0"] = 'T'
    unicodeValue["\u0BC2"] = 'U'
    unicodeValue["\u0BA5"] = 'W'
    unicodeValue["\u0BA7"] = 'X'
    unicodeValue["\u0BBD"] = 'Y'
    unicodeValue["\u0BBC"] = 'Z'

    r1 = re.compile(r"([\u0B95-\u0BB9])\u0BCD")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["\u0BCD"], text)

    r1 = re.compile(r"([\u0B95-\u0BB9])\u0BBC([\u0BBE-\u0BCC])([\u0B81-\u0B83])")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["\u0BBC"] + unicodeValue[match.group(2)] +
                                unicodeValue[match.group(3)], text)

    r1 = re.compile(r"([\u0B95-\u0BB9])\u0BBC([\u0BBE-\u0BCC])")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["\u0BBC"] + unicodeValue[match.group(2)],
                  text)

    r1 = re.compile(r"([\u0B95-\u0BB9])\u0BBC([\u0B81-\u0B83])")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["\u0BBC"] + unicodeValue[match.group(2)],
                  text)

    r1 = re.compile(r"([\u0B95-\u0BB9])\u0BBC")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["\u0BBC"] + 'a', text)

    r1 = re.compile(r"([\u0B95-\u0BB9])([\u0BBE-\u0BCC])([\u0B81-\u0B83])")
    text = r1.sub(
        lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[match.group(3)], text)

    r1 = re.compile(r"([\u0B95-\u0BB9])([\u0BBE-\u0BCC])")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)

    r1 = re.compile(r"([\u0B95-\u0BB9])([\u0B81-\u0B83])")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + 'a' + unicodeValue[match.group(2)], text)

    r1 = re.compile(r"([\u0B95-\u0BB9])")
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + 'a', text)

    r1 = re.compile(r"([\u0B86-\u0B94])([\u0B81-\u0B83])")
    text = r1.sub(lambda match: unicodeValue_vowels[match.group(1)] + unicodeValue[match.group(2)], text)

    r1 = re.compile(r"([\u0B85])([\u0B81-\u0B83])")
    text = r1.sub(lambda match: 'a' + unicodeValue[match.group(2)], text)

    r1 = re.compile(r"([\u0B86-\u0B94])")
    text = r1.sub(lambda match: unicodeValue_vowels[match.group(1)], text)

    text = re.sub(r"([\u0B80-\u0BFF])",
                  lambda a: unicodeValue_vowels[a.group()] if a.group() in unicodeValue_vowels else a.group(), text)
    text = re.sub(r"([\u0B80-\u0BFF])", lambda a: unicodeValue[a.group()] if a.group() in unicodeValue else a.group(),
                  text)
    return text


def convert_tam_wx2utf(text):
    unicodeValue = {}
    unicodeValue_vowels = {"a": '\u0B85', "A": '\u0B86', "i": '\u0B87', "I": '\u0B88', "u": '\u0B89', "U": '\u0B8A',
                           "q": '\u0B8B', "lq": '\u0B8C', "e": '\u0B8F', "E": '\u0B90', "o": '\u0B93', "O": '\u0B94',
                           "aA": '\u0B86', "ai": '\u0B87', "aI": '\u0B88', "au": '\u0B89', "aU": '\u0B8A',
                           "aq": '\u0B8B', "alq": '\u0B8C', "ae": '\u0B8F', "eE": '\u0B90', "ao": '\u0B93',
                           "aO": '\u0B94', "EY": '\u0B8D', "eV": '\u0B8E', "OY": '\u0B91', "oV": '\u0B92',
                           "aEY": '\u0B8D', "aeV": '\u0B8E', "aOY": '\u0B91', "aoV": '\u0B92'}

    unicodeValue["lY"] = '\u0BB3'
    unicodeValue["lYY"] = '\u0BB4'
    unicodeValue["nY"] = '\u0BA9'
    unicodeValue["rY"] = '\u0BB1'
    unicodeValue["EY"] = '\u0BC5'
    unicodeValue["eV"] = '\u0BC6'
    unicodeValue["aeV"] = '\u0BC6'
    unicodeValue["OY"] = '\u0BC9'
    unicodeValue["oV"] = '\u0BCA'
    unicodeValue["aoV"] = '\u0BCA'

    unicodeValue[";"] = ';'
    unicodeValue[":"] = ':'
    unicodeValue["\""] = '34'
    unicodeValue["'"] = '39'
    unicodeValue[","] = '44'
    unicodeValue["."] = '46'
    unicodeValue["/"] = '47'
    unicodeValue["?"] = '63'
    unicodeValue["<"] = '<'
    unicodeValue[">"] = '>'
    unicodeValue["["] = '91'
    unicodeValue["]"] = '93'
    unicodeValue["{"] = '123'
    unicodeValue["}"] = '125'
    unicodeValue["("] = '40'
    unicodeValue[")"] = '41'
    unicodeValue["@"] = '64'
    unicodeValue["#"] = '35'
    unicodeValue["^"] = '^'
    unicodeValue["*"] = '42'
    unicodeValue["_"] = '\u0BCD'
    unicodeValue["="] = '61'
    unicodeValue["+"] = '43'
    unicodeValue["|"] = '\u0BE4'
    unicodeValue["~"] = '~'
    unicodeValue["`"] = '`'
    unicodeValue["\\"] = '\\'

    unicodeValue["0"] = '\u0BE6'
    unicodeValue["1"] = '\u0BE7'
    unicodeValue["2"] = '\u0BE8'
    unicodeValue["3"] = '\u0BE9'
    unicodeValue["4"] = '\u0BEA'
    unicodeValue["5"] = '\u0BEB'
    unicodeValue["6"] = '\u0BEC'
    unicodeValue["7"] = '\u0BED'
    unicodeValue["8"] = '\u0BEE'
    unicodeValue["9"] = '\u0BEF'

    unicodeValue["a"] = '\u0B85'
    unicodeValue["b"] = '\u0BAC'
    unicodeValue["c"] = '\u0B9A'
    unicodeValue["d"] = '\u0BA1'
    unicodeValue["e"] = '\u0BC7'
    unicodeValue["f"] = '\u0B99'
    unicodeValue["g"] = '\u0B97'
    unicodeValue["h"] = '\u0BB9'
    unicodeValue["i"] = '\u0BBF'
    unicodeValue["j"] = '\u0B9C'
    unicodeValue["k"] = '\u0B95'
    unicodeValue["l"] = '\u0BB2'
    unicodeValue["m"] = '\u0BAE'
    unicodeValue["n"] = '\u0BA8'
    unicodeValue["o"] = '\u0BCB'
    unicodeValue["p"] = '\u0BAA'
    unicodeValue["q"] = '\u0BC3'
    unicodeValue["r"] = '\u0BB0'
    unicodeValue["s"] = '\u0BB8'
    unicodeValue["t"] = '\u0B9F'
    unicodeValue["u"] = '\u0BC1'
    unicodeValue["v"] = '\u0BB5'
    unicodeValue["w"] = '\u0BA4'
    unicodeValue["x"] = '\u0BA6'
    unicodeValue["y"] = '\u0BAF'
    unicodeValue["z"] = '\u0B81'

    unicodeValue["A"] = '\u0BBE'
    unicodeValue["B"] = '\u0BAD'
    unicodeValue["C"] = '\u0B9B'
    unicodeValue["D"] = '\u0BA2'
    unicodeValue["E"] = '\u0BC8'
    unicodeValue["F"] = '\u0B9E'
    unicodeValue["G"] = '\u0B98'
    unicodeValue["H"] = '\u0B83'
    unicodeValue["I"] = '\u0BC0'
    unicodeValue["J"] = '\u0B9D'
    unicodeValue["K"] = '\u0B96'
    unicodeValue["M"] = '\u0B82'
    unicodeValue["N"] = '\u0BA3'
    unicodeValue["O"] = '\u0BCC'
    unicodeValue["P"] = '\u0BAB'
    unicodeValue["Q"] = '\u0BC4'
    unicodeValue["R"] = '\u0BB7'
    unicodeValue["S"] = '\u0BB6'
    unicodeValue["T"] = '\u0BA0'
    unicodeValue["U"] = '\u0BC2'
    unicodeValue["W"] = '\u0BA5'
    unicodeValue["X"] = '\u0BA7'
    unicodeValue["Y"] = '\u0BBD'
    unicodeValue["Z"] = '\u0BBC'

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])eV([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aeV"] +
                                unicodeValue[match.group(4)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])eV')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aeV"], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])EY([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aEY"] +
                                unicodeValue[match.group(4)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])EY')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aEY"], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oV([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aoV"] +
                                unicodeValue[match.group(4)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oV')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aoV"], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])OY([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aOY"] +
                                unicodeValue[match.group(4)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oY')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["aoV"], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([AiIuUeEoO])([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue[match.group(4)] +
                                unicodeValue[match.group(5)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([AiIuUeEoO])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue[match.group(4)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])a([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue[match.group(4)],
                  text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])a')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)], text)

    r1 = re.compile(
        r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["_"] + unicodeValue[match.group(3)] + unicodeValue["_"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])eV([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["eV"] + unicodeValue[match.group(3)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])eV')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["eV"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])EY([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["EY"] + unicodeValue[match.group(3)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])EY')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["EY"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oV([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["oV"] + unicodeValue[match.group(3)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oV')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["oV"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])OY([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["OY"] + unicodeValue[match.group(3)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])OY')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue["OY"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([AiIuUeEoO])([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue[match.group(3)] + unicodeValue[match.group(4)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([AiIuUeEoO])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue[match.group(3)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])a([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)] +
                                unicodeValue[match.group(3)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])a')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"] + unicodeValue[match.group(2)],
                  text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])eV([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"] + unicodeValue[match.group(2)],
                  text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])eV')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])EY([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"] + unicodeValue[match.group(2)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])EY')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oV([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"] + unicodeValue[match.group(2)],
                  text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])oV')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])OY([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"] + unicodeValue[match.group(2)],
                  text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])OY')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])Z([AiIuUeEoO])([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["Z"] + unicodeValue[match.group(2)] +
                                unicodeValue[match.group(3)], text)

    text = re.sub(r'(lYY)EY', lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"], text)

    text = re.sub(r'(lYY)oV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lYY)oV', lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"], text)

    text = re.sub(r'(lYY)OY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lYY)OY', lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"], text)

    text = re.sub(r'(lYY)([AiIuUeEoO])([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[
                      match.group(3)], text)
    text = re.sub(r'(lYY)([AiIuUeEoO])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)],
                  text)

    text = re.sub(r'(lYY)a([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)
    text = re.sub(r'(lYY)a', lambda match: unicodeValue[match.group(1)], text)
    text = re.sub(r'(lYY)', lambda match: unicodeValue[match.group(1)] + unicodeValue["_"], text)

    text = re.sub(r'(lYY)eV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lYY)eV', lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"], text)

    text = re.sub(r'(lYY)EY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lYY)EY', lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"], text)

    text = re.sub(r'(lYY)oV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lYY)oV', lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"], text)

    text = re.sub(r'(lYY)OY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lYY)OY', lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"], text)

    text = re.sub(r'(lYY)([AiIuUeEoO])([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[
                      match.group(3)], text)
    text = re.sub(r'(lYY)([AiIuUeEoO])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)],
                  text)

    text = re.sub(r'(lYY)a([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)

    text = re.sub(r'(lYY)a', lambda match: unicodeValue[match.group(1)], text)
    text = re.sub(r'(lYY)', lambda match: unicodeValue[match.group(1)] + unicodeValue["_"], text)

    # lY cases
    text = re.sub(r'(lY)eV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lY)eV', lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"], text)

    text = re.sub(r'(lY)EY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lY)EY', lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"], text)

    text = re.sub(r'(lY)oV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lY)oV', lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"], text)

    text = re.sub(r'(lY)OY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(lY)OY', lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"], text)

    text = re.sub(r'(lY)([AiIuUeEoO])([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[
                      match.group(3)], text)
    text = re.sub(r'(lY)([AiIuUeEoO])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)],
                  text)

    text = re.sub(r'(lY)a([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)

    text = re.sub(r'(lY)a', lambda match: unicodeValue[match.group(1)], text)
    text = re.sub(r'(lY)', lambda match: unicodeValue[match.group(1)] + unicodeValue["_"], text)

    text = re.sub(r'(nY)eV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(nY)eV', lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"], text)

    text = re.sub(r'(nY)EY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(nY)EY', lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"], text)

    text = re.sub(r'(nY)oV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"] + unicodeValue[match.group(2)],
                  text)

    text = re.sub(r'(nY)oV', lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"], text)
    text = re.sub(r'(nY)OY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(nY)OY', lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"], text)
    text = re.sub(r'(nY)([AiIuUeEoO])([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[
                      match.group(3)], text)
    text = re.sub(r'(nY)([AiIuUeEoO])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(nY)a([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)
    text = re.sub(r'(nY)a', lambda match: unicodeValue[match.group(1)], text)

    text = re.sub(r'(nY)', lambda match: unicodeValue[match.group(1)] + unicodeValue["_"], text)

    text = re.sub(r'(rY)eV([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"] + unicodeValue[match.group(2)],
                  text)
    text = re.sub(r'(rY)eV', lambda match: unicodeValue[match.group(1)] + unicodeValue["eV"], text)

    text = re.sub(r'(rY)EY([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"] + match.group(2),
                  text)
    text = re.sub(r'(rY)EY', lambda match: unicodeValue[match.group(1)] + unicodeValue["EY"], text)

    text = re.sub(r'(rY)oV([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"] + match.group(2),
                  text)
    text = re.sub(r'(rY)oV', lambda match: unicodeValue[match.group(1)] + unicodeValue["oV"], text)

    text = re.sub(r'(rY)OY([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"] + unicodeValue[match.group(2)],
                  text)

    text = re.sub(r'(rY)OY', lambda match: unicodeValue[match.group(1)] + unicodeValue["OY"], text)

    text = re.sub(r'(rY)([AiIuUeEoO])([MHz])',
                  lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[
                      match.group(3)], text)
    text = re.sub(r'(rY)([AiIuUeEoO])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)],
                  text)

    text = re.sub(r'(rY)a([MHz])', lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)
    text = re.sub(r'(rY)a', lambda match: unicodeValue[match.group(1)], text)

    text = re.sub(r'(rY)', lambda match: unicodeValue[match.group(1)] + unicodeValue["_"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([AiIuUeEoO])([MHz])')
    text = r1.sub(
        lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)] + unicodeValue[match.group(3)],
        text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])([AiIuUeEoO])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])a([MHz])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue[match.group(2)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])a')
    text = r1.sub(lambda match: unicodeValue[match.group(1)], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])q')  # New rule
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["q"], text)

    r1 = re.compile(r'([kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh])')
    text = r1.sub(lambda match: unicodeValue[match.group(1)] + unicodeValue["_"], text)

    r1 = re.compile(r'(aq)([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels[match.group(1)] + unicodeValue[match.group(2)], text)

    r1 = re.compile(r'aq')
    text = r1.sub(lambda match: unicodeValue_vowels["aq"], text)

    r1 = re.compile(r'q')
    text = r1.sub(lambda match: unicodeValue_vowels["q"], text)

    r1 = re.compile(r'aeV([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["aeV"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'aeV')
    text = r1.sub(lambda match: unicodeValue_vowels["aeV"], text)

    r1 = re.compile(r'eV([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["eV"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'eV')
    text = r1.sub(lambda match: unicodeValue_vowels["eV"], text)

    r1 = re.compile(r'aeY([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["aeY"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'aeY')
    text = r1.sub(lambda match: unicodeValue_vowels["aeY"], text)

    r1 = re.compile(r'eY([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["eY"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'eY')
    text = r1.sub(lambda match: unicodeValue_vowels["eY"], text)

    r1 = re.compile(r'aoV([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["aoV"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'aoV')
    text = r1.sub(lambda match: unicodeValue_vowels["aoV"], text)

    r1 = re.compile(r'oV([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["oV"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'oV')
    text = r1.sub(lambda match: unicodeValue_vowels["oV"], text)

    r1 = re.compile(r'aoY([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["aoY"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'aoY')
    text = r1.sub(lambda match: unicodeValue_vowels["aoY"], text)

    r1 = re.compile(r'oY([MHz])')
    text = r1.sub(lambda match: unicodeValue_vowels["oY"] + unicodeValue[match.group(1)], text)

    r1 = re.compile(r'oY')
    text = r1.sub(lambda match: unicodeValue_vowels["oY"], text)

    r1 = re.compile(r'aA')
    text = r1.sub(lambda match: unicodeValue_vowels["aA"], text)

    r1 = re.compile(r'ai', re.IGNORECASE)
    text = r1.sub(lambda _: unicodeValue_vowels["ai"], text)

    r1 = re.compile(r'au', re.IGNORECASE)
    text = r1.sub(lambda _: unicodeValue_vowels["au"], text)

    r1 = re.compile(r'ae', re.IGNORECASE)
    text = r1.sub(lambda _: unicodeValue_vowels["ae"], text)

    r1 = re.compile(r'ao', re.IGNORECASE)
    text = r1.sub(lambda _: unicodeValue_vowels["ao"], text)

    text = re.sub(r'([A-Za-z])',
                  lambda a: unicodeValue_vowels[a.group()] if a.group() in unicodeValue_vowels else a.group(), text)

    text = re.sub(r'([A-Za-z])+', lambda a: unicodeValue[a.group()] if a.group() in unicodeValue else a.group(), text)
    
    return text
