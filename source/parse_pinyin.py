"""
Main caveat is when a second syllable starts with a vowel and could take the previous syllable's last letter and both syllables would be correct. 
In that case it does not work, and it is virtually impossible to do, without inferring meaning from the text first. 
"""

from source.mandarin_utils import (
    syllables_list,
    diacritics_to_base_letter,
    single_letter_consonant,
    vowel,
    diacritics_to_decimals_basic
)


class PinyinUtils:
    def __init__(self) -> None:
        pass
    
    def find_pinyin_syllable(self, text: str) -> list[str]:
        output_syl = []
        eval_str = ""

        for char in text.lower():
            eval_str += char

            if len(eval_str) > 3: # Logic breaks with "yìshí"
                temp_state = self.is_valid_pinyin_string(eval_str)
                temp_string = self.remove_pinyin_diacritics(eval_str)

                # Check if this is a valid pinyin string
                if (
                    self.is_valid_pinyin_string(self.remove_pinyin_diacritics(eval_str))
                    == False
                ):
                    if eval_str[-2] in single_letter_consonant:
                        if self.remove_pinyin_diacritics(eval_str)[-1] in vowel:
                            output_syl.append(eval_str[:-2])
                            eval_str = eval_str[-2:]
                        else:
                            output_syl.append(eval_str[:-1])
                            eval_str = eval_str[-1:]
                            continue
                    else:
                        output_syl.append(eval_str[:-1])
                        eval_str = eval_str[-1:]
                        continue
        
        output_syl.append(eval_str)
        return output_syl

    def tokenize_pinyin_text(self, text: str) -> list[str]:
        """
        Parses a text in pinyin and returns a list of its individual pinyin syllables

        Keyword arguments:
        text -- pinyin text
        """

        text = self.clean_pinyin_text(text)        
        output = text.split(" ")
        
        output = map(self.find_pinyin_syllable, output)
        output = [syllable for syllable_list in output for syllable in syllable_list]
        
        # Validate Output
        invalid_syllables = ([i for i in output
          if not self.is_valid_pinyin_string(self.remove_pinyin_diacritics(i)) ]
          )

        if any(invalid_syllables):
            raise InvalidSyllablesError(f"Found unrecognized syllables {invalid_syllables}") 

        return output

    def is_valid_pinyin_string(self, pinyin_str: str) -> bool:
        """
        Validates whether the provided string without diacritics or decimals is a valid syllable in Mandarin Chinese.

        Keyword arguments:
        pinyin_str -- string to evaluate without accents or decimals
        """

        allowed_syllables = syllables_list

        pinyin_str = pinyin_str.replace(" ", "")
        return pinyin_str.lower() in allowed_syllables

    def clean_pinyin_text(self, text: str) -> str:
        """
        #TODO move from cleaning text to giving option to return punctuations marks as separate individual list items.
        Eg: ['dǎ', 'gè', 'zhāo', 'hū', '?']

        """
        text = text.replace(".", " ")
        text = text.replace(",", " ")
        text = text.replace("?", " ")
        return text

    def remove_pinyin_diacritics(self, pinyin_str: str) -> str:
        """
        Removes the diacritics (accents) from the provided pinyin string

        Keyword arguments:
        pinyin_str -- pinyin string with diacritics
        """
        output_str = ""

        for char in pinyin_str.lower():
            if char in diacritics_to_base_letter:
                output_str += diacritics_to_base_letter[char]
            else:
                output_str += char
        return output_str

    def pinyin_diacritics_to_decimals(self, syllable: str) -> str:
        """
        It is assumed that there is only 1 accent per syllable.

        """
        extracted_accent = []
        extracted_accent = [char for char in syllable if char in diacritics_to_decimals_basic]
        syllable_no_diacritics = self.remove_pinyin_diacritics(syllable)
        
        if len(extracted_accent) == 0:
            output = syllable_no_diacritics + "5"

        elif len(extracted_accent) == 1:
            output = syllable_no_diacritics + str(
                diacritics_to_decimals_basic[extracted_accent[0]][1]
            )

        return output
    
class InvalidSyllablesError(Exception):
    pass
print(PinyinUtils().tokenize_pinyin_text("yǒu dì lìyòng wǒ de shíj wān"))