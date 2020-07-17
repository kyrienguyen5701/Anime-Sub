from translate import Translator

translator = Translator(to_lang='vi')
translation = translator.translate(input("Nhập vào câu bạn cần dịch: "))
print(translation)