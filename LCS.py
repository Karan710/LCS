s1=input("Enter First String:")
s2=input("Enter Second String:")
def lcs(s1, s2):
    m = [["" for x in range(len(s1))] for x in range(len(s2))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    m[i][j] = s1[i]
                else:
                    m[i][j] = m[i-1][j-1] + s1[i]
            else:
                m[i][j] = max(m[i-1][j], m[i][j-1])

    cs = m[-1][-1]

    return len(cs), cs

print(lcs(s1,s2))  


