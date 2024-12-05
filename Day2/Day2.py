
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
            continue
    curr = list(tem)
    curr2 = list (tem)
    curr.sort()
    curr2.sort(reverse=True)
    if curr == tem or curr2 == tem:
        count += 1   
        
print(count)
        





