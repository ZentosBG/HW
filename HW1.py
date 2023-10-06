while True:
    text = input("Введіть ткст-")
    actin = input("Щоб розсортувати по буквам натисніть l щоб розсортувати по словам w-")
    text = str.lower(text)
    actin = str.lower(actin)

    if actin == "l":
        text_len = {}
        text_len_sorted = {}

        a = 0
        for i in text:
            tim = len(text)
            if text[a].isalpha() and not text[a] in text_len:
                son = text.count(text[a])
                text_len[text[a]] = son
            a += 1
        else:
            text_len_sorted = dict(sorted(text_len.items()))

        for key in text_len_sorted:
            print(key, "-", text_len_sorted[key])

        else:
            print("Кількісти букв -" , tim)
            decision = input("Якщо хочете почати спочатку ввеіть 0 - ")
            if decision == "0":
                continue
            else:
                print("Дозустрічі:)")
                break
    elif actin == "w":
        a = 0
        list = []
        list = text.split()
        list_word = []

        for i in list:
            if list[a].isalpha() and not list[a] in list_word:
                if len(list[a]) > 3:
                    list_word.append(list[a])

            a += 1
        else:
            list_word_sorted = sorted(list_word)

        abc = 0
        for i in list_word_sorted:
            print(list_word_sorted[abc])
            abc += 1
        else:
            decision = input("Якщо хочете почати спочатку ввеіть 0 - ")
        if decision == "0":
            continue
        else:
            print("Дозустрічі:)")
            break
    else:
        print("Дебіл тобі сказано введи l або w")
        decision = input("Якщо хочете почати спочатку ввеіть 0 - ")
        if decision == "0":
            continue
        else:
            print("Дозустрічі:/")
            break