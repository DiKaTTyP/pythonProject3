def GenerationSimple(start, end):
    Spisok = []
    for i in range(start, end + 1):  # Формируется число
        k = 0
        num = i

        for n in range(1, end + 1):  # Формируется делитель

            if num % n == 0:  # Считается количество делителей
                k += 1

        if k == 2:  # Формируется список простых чисел
            Spisok.append(num)
            yield Spisok

