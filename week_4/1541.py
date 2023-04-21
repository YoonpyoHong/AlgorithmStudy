import sys

formula = list(sys.stdin.readline().strip())

checker = True
result =0
words = ''
for word in formula:
    if checker:
        if word == '-':
            result += int(words)
            words = ''
            checker = not checker
        elif word == '+':
            result += int(words)
            words = ''
        else:
            words += word
    else:
        if word == '-' or word == '+':
            result -= int(words)
            words = ''
        else:
            words += word
if checker:
    result += int(words)
else:
    result -= int(words)

print(result)