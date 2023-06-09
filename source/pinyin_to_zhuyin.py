# Copyright © 2012 Thomas TEMPÉ, <thomas.tempe@alysse.org>
# Copyright © 2014 Alex Griffin, <alex@alexjgriffin.com>

replacements = [
    (u"yu",   u"u:"),   (u"ü",    u"u:"),   (u"v", u"u:"),
    (u"yi",   u"i"),    (u"you",  u"ㄧㄡ"), (u"y", u"i"),
    (u"wu",   u"u"),    (u"wong", u"ㄨㄥ"), (u"w", u"u"),
]



table = [
    # special cases
    (u"ju",   u"ㄐㄩ"), (u"qu",   u"ㄑㄩ"), (u"xu",  u"ㄒㄩ"),
    (u"zhi",  u"ㄓ"),   (u"chi",  u"ㄔ"),   (u"shi", u"ㄕ"),   (u"ri",   u"ㄖ"),
    (u"zi",   u"ㄗ"),   (u"ci",   u"ㄘ"),   (u"si",  u"ㄙ"),
    (u"r5",   u"ㄦ"),

    # initials
    (u"b",    u"ㄅ"),   (u"p",    u"ㄆ"),   (u"m",   u"ㄇ"),   (u"f",    u"ㄈ"),
    (u"d",    u"ㄉ"),   (u"t",    u"ㄊ"),   (u"n",   u"ㄋ"),   (u"l",    u"ㄌ"),
    (u"g",    u"ㄍ"),   (u"k",    u"ㄎ"),   (u"h",   u"ㄏ"),
    (u"j",    u"ㄐ"),   (u"q",    u"ㄑ"),   (u"x",   u"ㄒ"),
    (u"zh",   u"ㄓ"),   (u"ch",   u"ㄔ"),   (u"sh",  u"ㄕ"),   (u"r",    u"ㄖ"),
    (u"z",    u"ㄗ"),   (u"c",    u"ㄘ"),   (u"s",   u"ㄙ"),

    # finals
    (u"i",    u"ㄧ"),   (u"u",    u"ㄨ"),   (u"u:",  u"ㄩ"),
    (u"a",    u"ㄚ"),   (u"o",    u"ㄛ"),   (u"e",   u"ㄜ"),   (u"ê",    u"ㄝ"),
    (u"ai",   u"ㄞ"),   (u"ei",   u"ㄟ"),   (u"ao",  u"ㄠ"),   (u"ou",   u"ㄡ"),
    (u"an",   u"ㄢ"),   (u"en",   u"ㄣ"),   (u"ang", u"ㄤ"),   (u"eng",  u"ㄥ"),
    (u"er",   u"ㄦ"),
    (u"ia",   u"ㄧㄚ"), (u"io",   u"ㄧㄛ"), (u"ie",  u"ㄧㄝ"), (u"iai",  u"ㄧㄞ"),
    (u"iao",  u"ㄧㄠ"), (u"iu",   u"ㄧㄡ"), (u"ian", u"ㄧㄢ"),
    (u"in",   u"ㄧㄣ"), (u"iang", u"ㄧㄤ"), (u"ing", u"ㄧㄥ"),
    (u"ua",   u"ㄨㄚ"), (u"uo",   u"ㄨㄛ"), (u"uai", u"ㄨㄞ"),
    (u"ui",   u"ㄨㄟ"), (u"uan",  u"ㄨㄢ"), (u"un",  u"ㄨㄣ"),
    (u"uang", u"ㄨㄤ"), (u"ong",  u"ㄨㄥ"),
    (u"u:e",  u"ㄩㄝ"), (u"u:an", u"ㄩㄢ"), (u"u:n", u"ㄩㄣ"), (u"iong", u"ㄩㄥ"),

    # tones
    (u"1",    u""),     (u"2",    u"ˊ"),
    (u"3",    u"ˇ"),    (u"4",    u"ˋ"),
    (u"5",    u"˙"),
]

table.sort(key=lambda pair: len(pair[0]), reverse=True)
replacements.extend(table)


def bopomofo(pinyin):
    '''Convert a pinyin string to Bopomofo
    The optional tone info must be given as a number suffix, eg: 'ni3'
    '''

    pinyin = pinyin.lower()
    for pair in replacements:
        pinyin = pinyin.replace(pair[0], pair[1])

    return pinyin

