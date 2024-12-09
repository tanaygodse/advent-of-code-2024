with open("in") as f:
    lines = f.read().splitlines()

list_a = []
for i in lines:
    list_a.append(i.split(' '))

list_a = [[int(i) for i in l] for l in list_a]


def is_safe(l):
    if len(l) < 2:
        return False

    if l == sorted(l):
        for i in range(1, len(l)):
            diff = l[i] - l[i-1]
            if diff < 1 or diff > 3:
                return False
        return True
    elif l == sorted(l, reverse=True):
        for i in range(1, len(l)):
            diff = l[i-1] - l[i]
            if diff < 1 or diff > 3:
                return False
        return True
    else:
        return False


res = 0
for l in list_a:
    if is_safe(l):
        res += 1
    else:
        for i in range(len(l)):
            new_l = l[:i] + l[i+1:]
            if is_safe(new_l):
                res += 1
                break
print(res)
