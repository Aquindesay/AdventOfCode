
data = open("Day2/PuzzelInputDay2.txt", "r").readlines()

distance = 0
liste = []
count = 0

for item in data:
    liste.append(list(map(int,item.strip("\n").split())))

for tem in liste:
    for i in range(0, len(tem)-1):
        distance = abs(tem[i] - tem[i+1])
        if distance > 3:
            break
    curr = list(tem)
    tem.sort()
    if curr == tem:
        count += 1
    tem.sort(reverse = True)
    if curr == tem:
        count += 1     
        
print(count)
        





