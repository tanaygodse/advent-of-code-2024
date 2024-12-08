with open("in") as f:
    lines = f.read().splitlines()

# print(lines)

result = []
equation = []
for l in lines:
    x = l.split(': ')
    result.append(int(x[0]))
    equation.append([int(n) for n in x[1].split(" ")])

# print(d)

res = 0
for i in range(len(result)):
    # print(k, v)
    temp = [equation[i][0]]
    for j in range(1, len(equation[i])):
        new_results = []
        for x in temp:
            new_results.append(x * equation[i][j])
            new_results.append(x + equation[i][j])
            new_results.append(int(str(x) + str(equation[i][j])))
        temp = new_results
        if all(t > result[i] for t in temp):
            break
    # print(temp)
    if result[i] in temp:
        res += result[i]


print(res)
