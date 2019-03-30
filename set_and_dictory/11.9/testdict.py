# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/26 15:30
# @Author  : Despicable Me
# @Email   : 
# @File    : testdict.py
# @Software: PyCharm
# @Explain :

from hashdict import HashDict

def main(capacity = 10):
    d = HashDict()
    print("\nThe dictionary: ", list(d.items()))
    for key in range(1, capacity + 1):
        d[key] = "Value" + str(key)
    print("\nLength: ", len(d))
    print("\nThe dictionary: ", d)
    print("\nThe keys: ", list(d.keys()))
    print("\nThe values: ", list(d.values()))
    print("\nThe items: ", list(map(str, d.items())))

    for i in range(1, capacity + 1):
        print(d)


    print("\nKey Value (using []): ", end = " ")
    for key in d:
        print(key, d[key], end= ", ")
    print("\nReplace Value1 with Valuez: ")
    d[1] = "Valuez"
    print(d)
    print("\n Delete all keys: ")
    for key in range(1, capacity + 1):
        print(d.pop(key), end="->")
    print("\nLength: ", len(d))

if __name__ == "__main__":
    main()