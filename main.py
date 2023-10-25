import unicodedata

# Tất cả nguyên âm
all_vowel = ['e', 'ê', 'o', 'ô', 'ơ', 'i', 'a', 'u', 'ư', 'y', 'ia', 'ua', 'ưa', 'oi', 'ai', 'ôi', 'ơi', 'ui', 'ưi', 'uôi', 'ươi', 'ay', 'ây', 'eo', 'ao', 'au', 'âu', 'iu', 'êu', 'iêu', 'yêu', 'ưu', 'ươu', 'on', 'an', 'ân', 'ăn', 'ôn', 'ơn', 'en', 'ên', 'in', 'un', 'iên', 'yên', 'uôn', 'ươn', 'ong', 'ông', 'ăng', 'âng', 'ung', 'ưng', 'eng', 'iêng', 'uông', 'ương', 'ang', 'anh', 'inh', 'ênh', 'om', 'am', 'ăm', 'âm', 'ôm', 'ơm', 'em', 'êm', 'im', 'um', 'iêm', 'yêm', 'uôm', 'ươm', 'ot', 'at', 'ăt', 'ât', 'ôt', 'ơt', 'et', 'êt', 'ut', 'ưt', 'it', 'iêt', 'uôt', 'ươt', 'oc', 'ac', 'ăc', 'âc', 'uc', 'ưc', 'ôc', 'uôc', 'iêc', 'ươc', 'ach', 'ich', 'êch', 'op', 'ap', 'ăp', 'âp', 'ôp', 'ơp', 'ep', 'êp', 'ip', 'up', 'iêp', 'ươp', 'oa', 'oe', 'oai', 'oay', 'oan', 'oăn', 'oang', 'oăng', 'oanh', 'oach', 'oat', 'oăt', 'uê', 'uy', 'uơ', 'uya', 'uân', 'uyên', 'uât', 'uyêt', 'uynh', 'uych', 'oong']
SC_list = ['e', 'ê', 'i'] # Special char
SAV_list = ['t', 'c', 'ch', 'p'] # Special accent vowel
# Tất cả các phụ âm đầu
all_consonant = ['b', 'v', 'l', 'h', 'c', 'n', 'm', 'd', 'đ', 't', 'th', 'x', 'ch', 's', 'r', 'k', 'kh', 'ph', 'nh', 'g', 'gh', 'qu', 'gi', 'ng', 'ngh', 'tr']
single_consonant_list = ['b', 'v', 'l', 'h', 'c', 'n', 'm', 'd', 'đ', 't', 'x', 's', 'r', 'k', 'g']
double_consonant_list = ['th', 'ch', 'kh', 'ph', 'nh', 'gh', 'qu', 'gi', 'ng', 'tr']
triple_consonant_list = ['ngh']
link_SC_consonant_list = ['k', 'gh', 'ngh']
unlink_SC_consonant_list = ['c', 'g', 'ng']
# Tất cả các thanh dấu
all_accent = [chr(769), chr(768), chr(777), chr(771), chr(803)]
SA_accent = [chr(769), chr(803)]
# Các case hợp lệ đặc biệt
special_verify_non_accent_list = ["gi"]

def split_accent(word:str) -> tuple[bool, str, str]:
    """
    Split accents in Vietnamese while keeping special Vietnamese characters
    text: input string to be splited
    Return: splited string
    Ex: "Trực" -> "Trưc", chr(803)
    """
    word = unicodedata.normalize("NFD", word)
    accent = ""
    for char in word:
        if char in all_accent:
            if accent == "":
                accent = char
            else:
                return False, "", ""
    if len(accent) > 0:
        word = word.replace(accent,"")
    word = unicodedata.normalize("NFC", word)
    return True, word, accent

def split_consonant_vowel(word:str) -> tuple[bool, str, str]:
    def get_consonant(word):
        if word[:3] in triple_consonant_list:
            return word[:3]
        if word[:2] in double_consonant_list:
            return word[:2]
        if word[:1] in single_consonant_list:
            return word[:1]
        return ""
    consonant = get_consonant(word)
    vowel = word[len(consonant):]
    if vowel in all_vowel:
        return True, consonant, vowel
    return False, "", ""

def Vietnamese_check(word:str) -> bool:
    lower_word = word.lower()
    ok, non_accent_word, accent = split_accent(lower_word)
    if not ok:
        return False
    if non_accent_word in special_verify_non_accent_list:
        return True
    ok, consonant, vowel = split_consonant_vowel(non_accent_word)
    if not ok:
        return False
    if consonant in unlink_SC_consonant_list and vowel[0] in SC_list:
        return False
    if consonant in link_SC_consonant_list and vowel[0] not in SC_list:
        return False
    if accent not in SA_accent:
        for end_vowel in SAV_list:
            if vowel.endswith(end_vowel):
                return False
    return True
