def boatsToSavePeople(people, limit):
    people.sort()
    l = 0
    r = len(people) - 1
    boats = 0
    while l <= r:
        sum2 = people[l] + people[r]
        if sum2 <= limit:
            l+=1
        r-=1
        boats += 1
    print(boats)
    return boats 

people = [3,2,2,1]
limit = 3

boatsToSavePeople(people, limit)