import unittest

from source.parse_pinyin import PinyinUtils

class TestPinyinutils(unittest.TestCase):
    def test_find_pinyin_syllable(self):
        data = "dă yigè hāqian"

        assert PinyinUtils().find_pinyin_syllable(data) == ['dă ', 'yi', 'gè ', 'hā', 'qian']

print(PinyinUtils().find_pinyin_syllable("dă yigè hāqian"))

if __name__ == '__main__':
    unittest.main()

