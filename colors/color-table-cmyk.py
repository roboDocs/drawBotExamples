size(200, 200)

n, m = 10, 10
x, y = 24, 18
s = 13

colorstep_c = 1.0 / (n - 1)
colorstep_m = 1.0 / (m - 1)
Y = 0.5

for j in range(m):
    for i in range(n):

        M = j * colorstep_m
        C = i * colorstep_c
        cmykFill(C, M, Y, 0)
        cmykStroke(C, M, Y, 0)
        rect(x, y, s, s)
        translate(0, s)
    translate(s, -(s * n))
