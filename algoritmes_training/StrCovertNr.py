def converter_str_int(s):
    neg = False
    answer = 0
    if s[0] == "-":
        s = s[1:]
        neg = True
    for e in s:
        answer += (((ord(e) + 12) % 50) - 10)
        answer *= 10
    if not neg:
        print(answer / 10)
    else:
        print(-answer / 10)

    return answer


string_number = "-432"
print(type(string_number))

integer_number = converter_str_int(string_number)
print(type(integer_number))
