str_ = input("Напечатайте текст: ")
str_ = list(str_)

if str_.count('f') > 1:
    lastf = str_[::-1].index('f')
    firstf = str_.index('f')
    print(f"First in {firstf}, Last in {(len(str_)-lastf-1)}")
elif str_.count('f') == 1:

    print("Индекс буквы 'f' равен: ", str_.index('f'))