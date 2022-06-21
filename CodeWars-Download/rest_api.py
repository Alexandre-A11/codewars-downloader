from manipulate_csv import edit_readme
import requests, random, os, platform

USER = "Alexandre-A11"
USER_URL = f"https://www.codewars.com/api/v1/users/{USER}"
USER_CHALLENGES = "/code-challenges/completed?page={page}"
CHALLENGES = "https://www.codewars.com/api/v1/code-challenges/"
LANGUAGES = ["python", "javascript", "cpp", "php"]
PATH_DIRECTORY = (
    "/mnt/Disco-Local/Cloud/Code/Desafios/CodeWars/"
    if platform.system() == "Linux"
    else f"Y:\\OneDrive\\Code\\Git\\Desafios\\CodeWars\\"
)


user_challenges = requests.get(f"{USER_URL}{USER_CHALLENGES}")


def create_files(path, suste):
    open(f"{path}/Readme.md", "w+")


def take_data_languages(kata, data):
    """Acessa RestApi e retorna linguagens do kata."""
    challenge = requests.get(f"{CHALLENGES}{kata}")
    return challenge.json()[data]


def take_katas(list_katas, qty, my_languages, lvl_katas):
    """Gera katas aleatórios a partir de arquivo CSV, Compara Katas completados com katas aleatórios, substitui katas aleatórios caso já tenham sido resolvidos. Retorna lista com novos katas"""
    challenge_complete = [key["id"] for key in user_challenges.json()["data"]]

    def compare_languages(kata):
        """Compara Listas de katas, confirmando se novo kata está disponível para determinada linguagem"""
        kata_languages = take_data_languages(kata, "languages")
        return all(item in kata_languages for item in my_languages)

    new_kata = random.sample(list_katas, qty)
    for index, kata in enumerate(new_kata):
        check_languages = compare_languages(kata)

        while kata in challenge_complete or not check_languages:
            # old_kata = kata
            kata = random.choice(list_katas)
            new_kata[index] = kata
            # take_data_languages(kata, "languages")

            check_languages = compare_languages(kata)
            # print(f"{my_languages} | {take_data_languages(kata)} == {check_languages}")
            # print(f"Kata alterado: {old_kata} para {kata}")
            print(f"{index+1}/{len(new_kata)} Concluído", end="\r")
    start_kata(new_kata, lvl_katas, my_languages)


def start_kata(kata_id_list, lvl_katas, my_languages):
    # for kata in kata_id_list:
    #     print(f"{kata} : {take_data_languages(kata)}")
    for kata in kata_id_list:
        kata_languages = take_data_languages(kata, "languages")
        folder = take_data_languages(kata, "slug")

        # define the name of the directory to be created
        path = (
            f"{PATH_DIRECTORY}{lvl_katas}kyu/{folder}/"
            if platform.system() == "Linux"
            else f"{PATH_DIRECTORY}{lvl_katas}kyu\\{folder}\\"
        )
        try:
            os.makedirs(path)
            os.mknod(f"{path}/Readme.md") if platform.system() == "Linux" else open(f"{path}/Readme.md", "w+")
            readme_data(kata, f"{path}Readme.md", lvl_katas)

            if platform.system() == "Linux":
                os.mknod(f"{path}/main.py") if "python" in kata_languages and "python" in my_languages else None
                os.mknod(f"{path}/main.js") if "javascript" in kata_languages and "javascript" in my_languages else None
                os.mknod(f"{path}/main.go") if "go" in kata_languages and "go" in my_languages else None
                os.mknod(f"{path}/main.rs") if "rust" in kata_languages and "rust" in my_languages else None
                os.mknod(f"{path}/main.php") if "php" in kata_languages and "php" in my_languages else None
                os.mknod(f"{path}/main.ts") if "typescript" in kata_languages and "typescript" in my_languages else None
                os.mknod(f"{path}/main.swift") if "swift" in kata_languages and "swift" in my_languages else None
                os.mknod(f"{path}/main.rb") if "ruby" in kata_languages and "ruby" in my_languages else None
                os.mknod(f"{path}/main.java") if "java" in kata_languages and "java" in my_languages else None
                os.mknod(f"{path}/main.cpp") if "cpp" in kata_languages and "cpp" in my_languages else None
                os.mknod(f"{path}/main.c") if "c" in kata_languages and "c" in my_languages else None
                os.mknod(f"{path}/main.cs") if "csharp" in kata_languages and "csharp" in my_languages else None
                os.mknod(f"{path}/main.sql") if "sql" in kata_languages and "sql" in my_languages else None
            else:
                open(f"{path}\\main.py", "w+") if "python" in kata_languages and "python" in my_languages else None
                open(
                    f"{path}\\main.js", "w+"
                ) if "javascript" in kata_languages and "javascript" in my_languages else None
                open(f"{path}\\main.go", "w+") if "go" in kata_languages and "go" in my_languages else None
                open(f"{path}\\main.rs", "w+") if "rust" in kata_languages and "rust" in my_languages else None
                open(f"{path}\\main.php", "w+") if "php" in kata_languages and "php" in my_languages else None
                open(
                    f"{path}\\main.ts", "w+"
                ) if "typescript" in kata_languages and "typescript" in my_languages else None
                open(f"{path}\\main.swift", "w+") if "swift" in kata_languages and "swift" in my_languages else None
                open(f"{path}\\main.rb", "w+") if "ruby" in kata_languages and "ruby" in my_languages else None
                open(f"{path}\\main.java", "w+") if "java" in kata_languages and "java" in my_languages else None
                open(f"{path}\\main.cpp", "w+") if "cpp" in kata_languages and "cpp" in my_languages else None
                open(f"{path}\\main.c", "w+") if "c" in kata_languages and "c" in my_languages else None
                open(f"{path}\\main.cs", "w+") if "csharp" in kata_languages and "csharp" in my_languages else None
                open(f"{path}\\main.sql", "w+") if "sql" in kata_languages and "sql" in my_languages else None

        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)


def readme_data(kata, path_readme, lvl_katas):
    """Adiciona descrição do Kata ao arquivo Readme.md"""
    description = f"[See on Website]({take_data_languages(kata, 'url')})\n\n{take_data_languages(kata, 'description')}"
    edit_readme(description, path_readme)
    open_folder(lvl_katas)


def open_folder(lvl_katas):
    """Abre pasta dos katas no nível selecionado."""
    path = f"{PATH_DIRECTORY}{lvl_katas}kyu"
    os.system(f"xdg-open {path}") if platform.system() == "Linux" else os.startfile(path)
