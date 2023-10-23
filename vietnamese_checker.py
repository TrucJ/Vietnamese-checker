import re

# Tất cả nguyên âm
all_vowel = ['e', 'ê', 'o', 'ô', 'ơ', 'i', 'a', 'u', 'ư', 'y', 'ia', 'ua', 'ưa', 'oi', 'ai', 'ôi', 'ơi', 'ui', 'ưi', 'uôi', 'ươi', 'ay', 'ây', 'eo', 'ao', 'au', 'âu', 'iu', 'êu', 'iêu', 'yêu', 'ưu', 'ươu', 'on', 'an', 'ân', 'ăn', 'ôn', 'ơn', 'en', 'ên', 'in', 'un', 'iên', 'yên', 'uôn', 'ươn', 'ong', 'ông', 'ăng', 'âng', 'ung', 'ưng', 'eng', 'iêng', 'uông', 'ương', 'ang', 'anh', 'inh', 'ênh', 'om', 'am', 'ăm', 'âm', 'ôm', 'ơm', 'em', 'êm', 'im', 'um', 'iêm', 'yêm', 'uôm', 'ươm', 'ot', 'at', 'ăt', 'ât', 'ôt', 'ơt', 'et', 'êt', 'ut', 'ưt', 'it', 'iêt', 'uôt', 'ươt', 'oc', 'ac', 'ăc', 'âc', 'uc', 'ưc', 'ôc', 'uôc', 'iêc', 'ươc', 'ach', 'ich', 'êch', 'op', 'ap', 'ăp', 'âp', 'ôp', 'ơp', 'ep', 'êp', 'ip', 'up', 'iêp', 'ươp', 'oa', 'oe', 'oai', 'oay', 'oan', 'oăn', 'oang', 'oăng', 'oanh', 'oach', 'oat', 'oăt', 'uê', 'uy', 'uơ', 'uya', 'uân', 'uyên', 'uât', 'uyêt', 'uynh', 'uych', 'oong']
# Tất cả các phụ âm đầu
all_consonant = ['b', 'v', 'l', 'h', 'c', 'n', 'm', 'd', 'đ', 't', 'th', 'x', 'ch', 's', 'r', 'k', 'kh', 'ph', 'nh', 'g', 'gh', 'qu', 'gi', 'ng', 'ngh', 'tr']
single_consonant_list = ['b', 'v', 'l', 'h', 'c', 'n', 'm', 'd', 'đ', 't', 'x', 's', 'r', 'k', 'g']
double_consonant_list = ['th', 'ch', 'kh', 'ph', 'nh', 'gh', 'qu', 'gi', 'ng', 'tr']
triple_consonant_list = ['ngh']
link_SC_consonant_list = ['k', 'gh', 'ngh']
unlink_SC_consonant_list = ['c', 'g', 'ng']
SC_list = ['e', 'ê', 'i'] # Special char

patterns = {
    '[áàảãạ]': 'a',
    '[ắằẳẵặ]': 'ă',
    '[ấầẩẫậ]': 'ă',
    '[éèẻẽẹ]': 'e',
    '[ếềểễệ]': 'ê',
    '[óòỏõọ]': 'o',
    '[ốồổỗộ]': 'ô',
    '[ớờởỡợ]': 'ơ',
    '[íìỉĩị]': 'i',
    '[úùủũụ]': 'u',
    '[ứừửữự]': 'ư',
    '[ýỳỷỹỵ]': 'y',
}

def remove_accent(text:str):
    """
    Remove accents in Vietnamese while keeping special Vietnamese characters
    text: input string to be converted
    Return: string converted
    Ex: "Tiếng Việt" -> "Tiêng Viêt"
    """
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

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

def Vietnamese_checker(word:str) -> bool:
    ok, consonant, vowel = split_consonant_vowel(word)
    if not ok:
        return False
    if consonant in unlink_SC_consonant_list and vowel[0] in SC_list:
        return False
    if consonant in link_SC_consonant_list and vowel[0] not in SC_list:
        return False
        
    return True
    
    

# Tất cả các nguyên âm và phụ âm theo SGK tiếng Việt (162 âm)
# e, b, ê, v, l, h, o, c, ô, ơ, 
# i, a, n, m, d, đ, t, th, 
# u, ư, x, ch, s, r, k, kh, 
# p-ph, nh, g, gh, q-qu, gi, ng, ngh, y, tr, 
# ia, ua, ưa, 
# oi, ai, ôi, ơi, ui, ưi, uôi, ươi, ay, â-ây, 
# eo, ao, au, âu, iu, êu, iêu, yêu, ưu, ươu, 
# on, an, ân, ă-ăn, ôn, ơn, en, ên, in, un, iên, yên, uôn, ươn, 
# ong, ông, ăng, âng, ung, ưng, eng, iêng, uông, ương, ang, anh, inh, ênh, 
# om, am, ăm, âm, ôm, ơm, em, êm, im, um, iêm, yêm, uôm, ươm, 
# ot, at, ăt, ât, ôt, ơt, et, êt, ut, ưt, it, iêt, uôt, ươt, 
# oc, ac, ăc, âc, uc, ưc, ôc, uôc, iêc, ươc, ach, ich, êch, 
# op, ap, ăp, âp, ôp, ơp, ep, êp, ip, up, 
# iêp, ươp, oa, oe, oai, oay, oan, oăn, 
# oang, oăng, oanh, oach, oat, oăt, uê, uy, 
# uơ, uya, uân, uyên, uât, uyêt, uynh, uych

# Nguyên âm thêm (không nằm trong SGK, tuy nhiên lại được sử dụng rộng rãi)
# oong


# Tất cả các nguyên âm (137 âm)
# e, ê, o, ô, ơ, i, a, u, ư, y, ia, ua, ưa, oi, ai, ôi, ơi, ui, ưi, uôi, ươi, ay, ây, eo, ao, au, âu, iu, êu, iêu, yêu, ưu, ươu, on, an, ân, ăn, ôn, ơn, en, ên, in, un, iên, yên, uôn, ươn, ong, ông, ăng, âng, ung, ưng, eng, iêng, uông, ương, ang, anh, inh, ênh, om, am, ăm, âm, ôm, ơm, em, êm, im, um, iêm, yêm, uôm, ươm, ot, at, ăt, ât, ôt, ơt, et, êt, ut, ưt, it, iêt, uôt, ươt, oc, ac, ăc, âc, uc, ưc, ôc, uôc, iêc, ươc, ach, ich, êch, op, ap, ăp, âp, ôp, ơp, ep, êp, ip, up, iêp, ươp, oa, oe, oai, oay, oan, oăn, oang, oăng, oanh, oach, oat, oăt, uê, uy, uơ, uya, uân, uyên, uât, uyêt, uynh, uych, oong

# Tất cả các phụ âm đầu (26 phụ âm)
# b, v, l, h, c, n, m, d, đ, t, th, x, ch, s, r, k, kh, ph, nh, g, gh, qu, gi, ng, ngh, tr



# Các trường hợp đặc biệt
## Các nguyên âm có phần cuối là
## t, c, ch, p
## phải được dùng kèm với thanh sắc hoặc thanh nặng

## Luật sử dụng phụ âm g/gh, ng/ngh, c/k
## Các phụ âm đầu g, ng, c bắt buộc không sử dụng với nguyên âm bắt đầu với từ 'i', 'e', 'ê'
## Các phụ âm đầu gh, ngh, k bắt buộc phải sử dụng với nguyên âm bắt đầu với từ 'i', 'e', 'ê'

## Luật đọc khi dùng phụ âm đầu 'qu'
## Luật đọc khi dùng phụ âm đầu 'gi'
