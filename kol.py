with open("emp.csv","r") as file:
    for line in file:
        line=line.split(',')
        print(line[0])
