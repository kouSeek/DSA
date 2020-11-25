def spiralPrint(r, c):
    mat = [ [0 for i in range(c)] for j in range(r)]
    left, right, top, bottom = 0, c-1, 0, r-1

    num = 0
    while num < r*c:
        ## go left
        for i in range(left, right+1):
            mat[top][i] = num
            num += 1
        top += 1

        ## go down
        for i in range(top, bottom+1):
            mat[i][right] = num
            num += 1
        right -= 1

        ## go right
        for i in range(right, left-1, -1):
            mat[bottom][i] = num
            num +=1
        bottom -= 1

        ## go up
        for i in range(bottom, top-1, -1):
            mat[i][left] = num
            num += 1
        left += 1

    pprint(mat)



def pprint(mat):
    for i in mat:
        print(i)

if __name__ == "__main__":
    spiralPrint(5, 5)
