import tabulate as tab
import googletrans


class Translator:
    def __init__(self):
        pass

    def get_data(self):
        self.text = input("enter the text here ")
        self.text_language = input("enter the text language here ")
        self.translated_language = input(
            "enter the translated language here ").lower()
        self.Reference_Table(self.translated_language)

    def Reference_Table(self, t_language):
        languages = googletrans.LANGUAGES
        lang_dict = {'Languages': [items for _, items in languages.items()], 'Abstract': [
            keys for keys in languages.keys()]}
        for (abstract, lang) in zip(lang_dict['Abstract'], lang_dict['Languages']):
            if lang == t_language.lower():
                self.abstract_code = abstract
                break
    def Translator(self):
        try:
            translator = googletrans.Translator()
            translated_text = translator.translate(
                self.text, dest=self.abstract_code)
            Trans_val = [[self.text_language.upper(), self.translated_language.upper()], [
                self.text, f"{translated_text.text}({translated_text.pronunciation})"]]
            print(tab.tabulate(Trans_val, headers="firstrow", tablefmt='presto'))
        except ValueError:
            print("Invalid Input!! .....\nTry again")

    def translate(self):
        prompt = False
        while not prompt:
            self.get_data()
            self.Translator()
            prompt = input("Do you want to try again?(Y/N): ")
            if prompt == 'N' or prompt == 'n':
                prompt = True
            elif prompt == 'Y' or prompt == 'y':
                prompt = False
            else:
                raise Exception("Invalid Input!! .... Try again")


if __name__ == '__main__':
    home = Translator()
    home.translate()