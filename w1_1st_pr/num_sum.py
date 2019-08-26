import sys
digit_string = sys.argv[1]

def validate(num):
    try:
        int(num)
    except:
        print("Number format is invalid. Integer required:", num)
        exit(10)


def get_sum(num):
    if len(str(num)) == 1:
        return num
    return int(str(num)[0:1]) + int(get_sum(str(num)[1:]))


validate(digit_string)
print(get_sum(digit_string))
