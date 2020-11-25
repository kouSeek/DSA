def mat_rotate(mat, num):
    def rotate(mat):
        r = len(mat)
        c = len(mat[0])

        temp = [ [0 for i in range(c)] for j in range(r)]
        top, left, right, bottom = 0, 0, c-1, r-1
        while left<right and top<bottom:
            ## top
            for i in range(left, right):
                temp[top][i] = mat[top][i+1]
            ## right
            for i in range(top, bottom):
                temp[i][right] = mat[i+1][right]
            ##bottom
            for i in range(right, left, -1):
                temp[bottom][i] = mat[bottom][i-1]
            ## left
            for i in range(bottom, top, -1):
                temp[i][left] = mat[i-1][left]
            
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return temp


    for i in range(num):
        mat = rotate(mat)

    return mat



def pprint(mat):
    for i in mat:
        print(i)





mat = [
[1,2,3,4],
[12,1,2,5],
[11,4,3,6],
[10,9,8,7],
]

pprint(mat)
print("------------------")
pprint(mat_rotate(mat, 2))