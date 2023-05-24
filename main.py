from source.parse_pinyin import PinyinUtils
from source.pinyin_to_zhuyin import bopomofo
input_str = "Lingguo dàchīyìjīng!"

PinUti = PinyinUtils()

pinyin_tone_mark_list = PinUti.tokenize_pinyin_text(input_str)



pinyin_tone_number_list = [PinUti.pinyin_diacritics_to_decimals(item) for item in pinyin_tone_mark_list]
print(pinyin_tone_number_list)
bopomofo_list = [bopomofo(syllable) for syllable in pinyin_tone_number_list]
bopomofo_list
print(" ".join(bopomofo_list))