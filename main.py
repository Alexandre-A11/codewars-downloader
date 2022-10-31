from manipulate_csv import new_katas, clear
from rest_api import take_katas, LANGUAGES

clear()
# Dificuldade Katas
lvl_katas = input(
    "8) 8 kyu\n7) 7 kyu\n6) 6 kyu\n5) 5 kyu\n4) 4 kyu\n3) 3 kyu\n2) 2 kyu\n1) 1 kyu\nSelecione o nível de dificuldade desejado (default = 8): "
)
if lvl_katas not in "12345678" or int(lvl_katas) > 8:
    lvl_katas = 8
clear()


# Linguagem
for index, language in enumerate(LANGUAGES):
    if language == "cpp":
        language = "c++"
    print(f"{index+1}) {language}")

print("0) Todas as linguagens mostradas")

choice_languages = abs(int(input("Escolha a linguagem: ")))

for num in str(choice_languages):
    if int(num) > len(LANGUAGES):
        choice_languages = 0

if choice_languages != 0:
    languages = []
    for i in str(choice_languages):
        if LANGUAGES[int(i) - 1] not in languages:
            languages.append(LANGUAGES[int(i) - 1])
else:
    languages = LANGUAGES
clear()
print("Linguagem(s) escolhida(s):")
for lang in languages:
    print("c++" if lang == "cpp" else lang)

# Quantidade de Katas
qty_katas = int(input("Digite a quantidade de desafios que vocês deseja baixar (default = 1, max = 10): "))
if qty_katas < 1 or qty_katas > 10:
    qty_katas = 1

clear()
# Criar lista com novos katas
new_katas_list = new_katas(lvl_katas)

take_katas(new_katas_list, qty_katas, languages, lvl_katas)
