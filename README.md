Goal: Transform a pinyin string, no matter the text format into the right bopomofo tokens.
Subgoal 1: Parse string of pinyin without proper spacing between syllables to individual syllables
Subgoal 2: Create bopomofo token from pinyin (via existing repo)

Approach used is based on the observation that most Mandarin pinyin syllable start with a consonant. 

Main caveat is when a second syllable starts with a vowel and could take the previous syllable's last letter and both syllables would be correct. 
In that case it does not work, and it is virtually impossible to do, without inferring meaning from the text first. 


Credits to [ttempe](https://github.com/ttempe) for the decimal_pinyin to zhuyin converter.



## New goal
- Transform any text in pinyin, including punctuation, into its bopomofo equivalent. 
#### Example 1:
Input: yīnwéi dàizhe kǒuzhào yīzhí jiǎng huà ， hěn bù shūfú ，hěn mèn。
Output: ㄧㄣ ㄨㄟˊ ㄉㄞˋ ㄓㄜ˙ ㄎㄡˇ ㄓㄠˋ ㄧ ㄓˊ ㄐㄧㄤˇ ㄏㄨㄚˋ，ㄏㄣˇ ㄅㄨˋ ㄕㄨ ㄈㄨˊ，ㄏㄣˇ ㄇㄣˋ。

#### Example 2
Input: Lingguo dàchīyìjīng!
Output: ㄌㄧㄥˊ ㄍㄨㄛ˙ ㄉㄚˋ ㄔ ㄧˋ ㄐㄧㄥ!


### TODOS
- Achieve new goal
- Set up input validation to ensure always valid output
- Set up unit tests