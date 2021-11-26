import sys
import os
output = open(sys.argv[4], "w")
try:
    n = sys.argv[1]
    if n != "enc" and n != "dec":
        raise ModuleNotFoundError
    key = open(sys.argv[2], "r")
    if n == "enc":
        plain = open(sys.argv[3], "r")
        plain_list = [line.upper() for line in plain.readline()]
        if (plain_list == []):
            raise ZeroDivisionError
        if sys.argv[3].endswith(".txt") is False:
            raise NameError
        for control1 in plain_list:
            if control1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']:
                raise ArithmeticError
    elif n == "dec":
        cipher = open(sys.argv[3], "r")
        cipher_list = list(eval(cipher.readline()))
        if not sys.argv[3].endswith(".txt"):
             raise NameError
    if not sys.argv[2].endswith(".txt"):
        raise LookupError
    key_list = [line.strip("\n").split(",") for line in key.readlines()]
    key.close()
    keycontrol = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "\n"]
    if key_list == []:
        raise RecursionError
    for error in key_list:
        for err in error:
            if err not in keycontrol:
                raise OverflowError
    key_list_int = []
    key_list_int1 = []
    if len(sys.argv) != 5:
        raise IndexError
except IndexError:
     print("Parameter number error")
except FileNotFoundError:
    if not (os.path.exists(sys.argv[3]) ):
        print("Input file not found error")
    elif not os.path.exists(sys.argv[2]):
        print("Key file not found error")
except NameError:
    print("The input file could not be read error")
except ZeroDivisionError:
    print("Input file is empty error")
except LookupError:
    print("Key file could not be read error")
except RecursionError:
    print("Key file is empty error")
except OverflowError:
    print("Invalid character in key file error")
except ArithmeticError:
    print("Invalid character in input file error")
except ModuleNotFoundError:
    print("Undefined Parameter Error")
else:
    for keys in key_list:
        for k in keys:
            key_list_int1.append(int(k))    #string --> integer
        key_list_int.append(key_list_int1)
        key_list_int1 = []
    if n == "enc":
        enc_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, " ": 27}
        empty = []
        for letter in plain_list:
            if letter == []: # create a list to multiplication
                empty.append(" ")
            for pl in letter:
                PL = pl.upper()
                empty.append(PL)
        pass_mul_list = []
        for em in empty:        #From this it starts to multiply
            pass_mul_list.append(enc_dict.get(em))
        a, b, c, list = len(key_list_int), 0, 1, []
        while a * c <= len(pass_mul_list):
            if len(pass_mul_list) % len(key_list_int) == 0:
                list.append(pass_mul_list[a * b:a * c])
                b, c = b + 1, c + 1
            else:
                while len(pass_mul_list) % len(key_list_int) != 0:
                    pass_mul_list.append(27)
        f = 0
        result = 0
        result_list = []
        for first in list:
            for ky in key_list_int:
                for k in ky:
                    a = k * first[f]
                    f += 1
                    result += a
                result_list.append(result)
                f = 0
                result = 0
        print(*result_list, sep=",", file = output)# end of encoding
    elif n == "dec":
    #decoding
        unit_matris = []
        unit_matris1 = []
        unittest = 0
        for keyy in key_list_int:
            for i in range(0, len(keyy)):
                unit_matris1.append(0)
            unit_matris1[unittest] = 1
            unit_matris.append(unit_matris1)
            unit_matris1 = []
            unittest += 1
        just_now = []
        for unit_matris2 in unit_matris[0]:
            strange = unit_matris2 / key_list_int[0][0] # this is for unit matrix
            just_now.append(strange)
        unit_matris[0] = just_now
        just_now = []
        for keyy in key_list_int[0]:
            first = keyy / key_list_int[0][0] # this is key matrix
            just_now.append(first)
        key_list_int[0] = just_now
        just_now = []
        ct = 1
        firstdevelop = 0
        for unit in unit_matris[1:]:
            for i in unit_matris[0]:
                down = unit_matris[ct][firstdevelop] - (key_list_int[ct][0] * unit_matris[0][firstdevelop])
                firstdevelop += 1
                just_now.append(down)
            unit_matris[ct] = just_now
            ct += 1
            firstdevelop = 0
            just_now = []
        ct = 1
        for keyy in key_list_int[1:]:
            for i in key_list_int[0]:
                calm = key_list_int[ct][firstdevelop] - (key_list_int[ct][0] * key_list_int[0][firstdevelop])
                firstdevelop += 1
                just_now.append(calm)
            key_list_int[ct] = just_now
            ct += 1
            firstdevelop = 0
            just_now = []
        ct = 1
        firstdevelop = 1
        c1 = 1
        b1 = 1
        a1 = 1
        a = 1
        basic_math = 0
        for keyy in key_list_int[1:]:
            for uni in unit_matris[ct]:
                makeone1 = uni / key_list_int[ct][firstdevelop]
                just_now.append(round(makeone1, 3))
            unit_matris[ct] = just_now
            just_now = []
            for divi in key_list_int[ct]:
                make_one = divi/key_list_int[ct][firstdevelop]
                just_now.append(round(make_one, 3))
            key_list_int[ct] = just_now
            just_now = []
            b = b1
            c = c1
            for zub in unit_matris:
                if zub == unit_matris[ct]:
                    basic_math += 1
                    continue
                else:
                    index = 0
                    b = 0
                    c = 0
                    for z in zub:
                        if index == None:
                            continue
                        else:
                            basic1 = key_list_int[basic_math][a]
                            if basic1 is not zub[-1]:
                                down = z - (unit_matris[ct][b] * basic1)
                            else:
                                down = basic1 - (unit_matris[ct][b] * basic1)
                            just_now.append(round(down, 3))
                        if index == len(zub) - 1:
                            break
                        else:
                            b += 1
                        index += 1
                    zub[c:] = just_now
                    just_now = []
                b = 0
                index = 0
                basic_math += 1
            a += 1
            b = b1 - 1
            c = c1
            basic_math = 0
            for i in key_list_int:
                if i == key_list_int[ct]:
                    continue
                else:
                    indexx = 0
                    for k in i:
                        if indexx == 0:
                            b += 1
                            indexx += 1
                            continue
                        else:
                            basic = i[a1]
                            if basic is not i[-1]:
                                calm = k - key_list_int[ct][b] * basic
                            else:
                                calm = basic - (key_list_int[ct][b] * basic)
                            just_now.append(round(calm, 3))
                        if i.index(basic) == len(i) - 1 or b == len(i) - 1:
                            break
                        else:
                            b += 1
                        indexx += 1
                    indexx = 0
                    i[c:] = just_now
                    just_now = []
                b = b1 - 1
            c1 += 1
            b1 += 1
            ct += 1
            a1 += 1
            firstdevelop += 1
        decode_list = []
        decode_list1 = []
        for cipherr in cipher_list:
            decode_list1.append(cipherr)
            if len(decode_list1) == len(key_list_int[0]):
                decode_list.append(decode_list1)
                decode_list1 = []
        gfirst = 0
        final_result = 0
        final_list = []
        for dec in decode_list:
            for start in unit_matris:
                for final in start:
                    find = final * dec[gfirst]
                    final_result += find
                    gfirst += 1
                final_list.append(final_result)
                final_result = 0
                gfirst = 0
        dec_dict = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M", 14:"N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z", 27: " "}
        for i in final_list:
            print(dec_dict.get(i), end="", file = output)