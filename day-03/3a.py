res = 0


def intTillComma(arr, idx):
    temp = ""
    for i in range(len(arr[idx:])):
        if arr[idx+i].isdigit():
            temp += arr[idx+i]
        elif arr[idx+i] == ',':
            return (idx+i, temp)
        else:
            return (-1, "")


def intTillClose(arr, idx):
    temp = ""
    for i in range(len(arr[idx:])):
        if arr[idx+i].isdigit():
            temp += arr[idx+i]
        elif arr[idx+i] == ')':
            return (idx+i, temp)
        else:
            return (-1, "")


with open("in") as f:
    lines = f.read()


temp = ""
for i in range(len(lines)):
    temp += lines[i]
    if lines[i-3:i+1] == 'mul(':
        aidx, a = intTillComma(lines, i+1)
        bidx, b = intTillClose(lines, aidx+1)
        if aidx != -1 and bidx != -1:
            res += int(a)*int(b)
        else:
            continue
print(res)
