import numpy as np


def hamster(infoHamster, S, C):
    arr = []

    for i in range(1, C):
        for j in range(C):
            j = j + 1
            progorluvi = infoHamster[C - j][0] + (infoHamster[C - j][1] * (C - i))
            arr.append(int(progorluvi))

    arr1 = (np.array_split(arr, len(arr) / C))
    print(arr1, "відсортовано по прожорливості від найбільшої кількості сусідів до найменшої")

    length = 0  # кількість хомяків які відкидаються
    sum = 0  # кількість пакетів які їдять хомяки разом
    success = False
    for i in arr1:
        i.sort()
        print(i)
        for j in range(len(i) - length):
            sum += i[j]
        print(sum)
        if sum <= S:
            success = True
            break
        else:
            length += 1
            sum = 0

    if success:
        return C - length
    else:
        return 1


S = 19  # Кількість пакетів у покупця
C = 4  # Кількість хомяків в магазині
infoHamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]  # [H-денна норма для хомяка G-жадібність за кожного сусіда]

if __name__ == '__main__':
    print(hamster(infoHamsters, S, C), "Hamster/s")