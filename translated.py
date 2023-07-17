from googletrans import Translator

translator = Translator()
all_languages = {'af': 'afrikaans',
                 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
                 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque',
                 'be': 'belarusian',
                 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian',
                 'ca': 'catalan',
                 'ceb': 'cebuano', 'ny': 'chichewa',
                 'zh-cn': 'chinese (simplified)',
                 'zh-tw': 'chinese (traditional)', 'co': 'corsican',
                 'hr': 'croatian',
                 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
                 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino',
                 'fi': 'finnish',
                 'fr': 'french', 'fy': 'frisian',
                 'gl': 'galician', 'ka': 'georgian',
                 'de': 'german', 'el': 'greek',
                 'gu': 'gujarati', 'ht': 'haitian creole',
                 'ha': 'hausa', 'haw': 'hawaiian',
                 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
                 'hu': 'hungarian',
                 'is': 'icelandic',
                 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish',
                 'it': 'italian',
                 'ja': 'japanese',
                 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh',
                 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)',
                 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
                 'lt': 'lithuanian',
                 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy',
                 'ms': 'malay', 'ml': 'malayalam',
                 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
                 'mn': 'mongolian',
                 'my': 'myanmar (burmese)',
                 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto',
                 'fa': 'persian', 'pl': 'polish',
                 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
                 'ru': 'russian', 'sm': 'samoan',
                 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
                 'sn': 'shona', 'sd': 'sindhi',
                 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian',
                 'so': 'somali', 'es': 'spanish',
                 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish',
                 'tg': 'tajik', 'ta': 'tamil',
                 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
                 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek',
                 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
                 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu',
                 'fil': 'Filipino', 'he': 'Hebrew'}

def get_translation(slang, text_input, language_output):
    if slang == '':
        response = translator.translate(text=text_input, dest=language_output)
    else:
        response = translator.translate(text=text_input, src=slang, dest=language_output)
    return [response.text, all_languages[response.src].capitalize()]
    # return response
