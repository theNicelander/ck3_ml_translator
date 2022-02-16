from ck3_translator.ck3_translator import TranslatorCK3

ck3_translator = TranslatorCK3(sleep_timer=2)

languages = ["french", "spanish", "german", "russian", "korean", "simp_chinese"]

for language in languages:
    ck3_translator.translate_folder("localization/english", language)

