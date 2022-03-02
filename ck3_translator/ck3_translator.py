import os
import time
from tqdm import tqdm
from googletrans import Translator

from ck3_translator.file_utils import load_yaml


def get_translation_model():
    model = dlt.TranslationModel()
    print("Model Loaded")
    return model


class Base:
    def __init__(self, source_lang: str = "english", sleep_timer=5):
        self.source_lang = source_lang
        self.translator = Translator()
        self.sleep_timer = sleep_timer

    def _translate_text(self, text, target_lang) -> str:
        if target_lang == 'simp_chinese':
            target_lang = "zh-cn"
        time.sleep(self.sleep_timer)
        trans = self.translator.translate(text, src=self.source_lang, dest=target_lang)
        return trans.text

    def _translate_yaml(self, to_translate: dict, target_lang: str) -> dict:
        source = to_translate[f"l_{self.source_lang}"]

        tmp_dict = {}
        for key, text in tqdm(source.items()):
            translation = self._translate_text(text, target_lang)
            tmp_dict[key] = translation

        return {f"l_{target_lang}": tmp_dict}

    @staticmethod
    def _save_as_utf8_bom(translated, output_file):
        lang, output = list(translated.items())[0]
        # Save to file
        with open(output_file, "w", encoding="UTF-8-sig") as f:
            f.write(f"{lang}:\n")
            for k, v in output.items():
                f.write(f'  {k}:0 "{v}"\n')


class TranslatorCK3(Base):
    def translate_document(self, file_path, target_lang) -> None:
        """Translate single yml file to target language"""
        output_file = file_path.replace(self.source_lang, target_lang)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        print(f"Translating {file_path} -> {output_file}")

        # Load yaml
        my_yaml = load_yaml(file_path)

        # translate
        translated = self._translate_yaml(my_yaml, target_lang)

        # Save
        self._save_as_utf8_bom(translated, output_file)

    def translate_folder(self, folder, target_lang) -> None:
        """Translate all files in a folder to the target language"""
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                self.translate_document(file_path, target_lang)
