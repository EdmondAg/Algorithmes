def char_to_binary(c):
    return "{0:07b}".format(ord(c))


def string_to_binary(s):
    result = ""
    for c in s:
        result += char_to_binary(c)
    return result


def code_01_00(c):
    message = string_to_binary(c)
    finalPrint = ""
    if int(message[0]) == 1:
        finalPrint += "0 "
    else:
        finalPrint += "00 "
    last = False
    for b in range(len(message)):
        if b == len(message) - 1:
            b -= 1
            last = True
        if message[b] == message[b + 1]:
            finalPrint += "0"
            if message[b] != message[b + 1]:
                if message[0] == 1:
                    finalPrint += " 0 "
                else:
                    finalPrint += " 00 "
        else:
            if not last:
                finalPrint += "0 "
                if int(message[b + 1]) == 1:
                    finalPrint += "0 "
                else:
                    finalPrint += "00 "
            else:
                finalPrint += "0"
    print(finalPrint)


code_01_00("!")
