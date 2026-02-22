if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
    scores = sorted(set([record[1] for record in record]))
    second_lowest = scores[1]
    names = [record[0] for record in record if record[1] == second_lowest]
    for name in sorted(names):
        print(name)
