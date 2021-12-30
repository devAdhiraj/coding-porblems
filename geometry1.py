for i in range(int(input())):
    a = input().split()
    a = list(map(int, a))

    d1 = ((a[2] - a[0])**2 + (a[3] - a[1])**2)**0.5
    d2 = ((a[4] - a[2])**2 + (a[5] - a[3])**2)**0.5
    d3 = ((a[4] - a[0])**2 + (a[5] - a[1])**2)**0.5
    s = (d1 + d2 + d3) / 2
    a = (s*(s - d1)*(s - d2)*(s - d3))**0.5
    print('{0:.2f}'.format(round(a, 2)), '{0:.2f}'.format((round(2*s, 2))), )