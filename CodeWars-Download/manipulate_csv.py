import csv, os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def new_katas(level_katas):
    """Acessa CSV e cria lista com ID's"""
    with open(f"./csv_files/{level_katas}kyu.csv", "r") as file:
        reader_csv = csv.reader(file)
        new_katas_list = [row for row in reader_csv][0]
        return new_katas_list


def generate_csv(kyu, list):
    """Cria arquivo CSV"""
    with open(f"./csv_files/{kyu}kyu.csv", "w", encoding="UTF8") as file:
        # create the csv writer
        writer = csv.writer(file)

        # write a row to the csv file
        writer.writerow(list)
        print(f"{len(list)} katas adicionados ao {kyu}kyu.csv")


def compare_csv(kyu, kyu_available):
    """Verifica se existe o arquivo CSV do nível kyu escolhido e compara a quantidade de katas disponíveis no site e os extraídos"""
    csv_file = f"{kyu}kyu.csv"
    if os.path.isfile(f"./csv_files/{csv_file}"):
        # Open the csv file object
        with open(f"./csv_files/{csv_file}", "r") as file:
            # Construct the csv reader object from the file object
            reader = csv.reader(file)
            for row in reader:
                if len(row) == kyu_available:
                    print(
                        "Quantidade de katas disponíves é a mesma quantidade de katas extraídos, encerrando operação."
                    )
                    return 0


def edit_readme(description, path_readme):
    with open(path_readme, "w") as file:
        file.write(description)
    return 