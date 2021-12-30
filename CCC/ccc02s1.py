a = [[0, 0, 0, 0]]
p = [int(input()) for x in range(4)]
g = int(input())
c = 0
min = 10000
for j in range(-1, -5, -1):
    if p[j] == g:
        t = [0, 0, 0, 0]
        t[j] = 1
        print("# of PINK is {0} # of GREEN is {1} # of RED is {2} # of ORANGE is {3}".format(t[0], \
        t[1], t[2], t[3]))
        c += 1
        min = 1    
    
    elif p[j] < g:
        for i in a:
            temp = i[0]*p[0] + i[1]*p[1] + i[2]*p[2] + \
            i[3]*p[3] + p[j]
            if temp == g:
                t = i[:]
                t[j] += 1
                if sum(t) < min:
                    min = sum(t)
                c += 1
                print("# of PINK is {0} # of GREEN is {1} # of RED is {2} # of ORANGE is {3}".format(t[0], \
                t[1], t[2], t[3]))
            elif temp < g:
                t2 = i[:]
                t2[j] += 1
                a.append(t2)

print("Total combinations is {0}.".format(c))
print("Minimum number of tickets to print is {0}.".format(min))