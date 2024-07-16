import sys

def main():
    while True:
        print("""Welcome, please enter your desired action:
(1): Matrix Addition A+B
(2): Matrix Transpose
(3): Matrix Multiplication AB
(4): Matrix Determinant det(A)""")
        try:
            n = int(input("Enter:"))
            if n == 1:
                print("For matrix A:")
                matrixA = input_matrix()
                print("For matrix B:")
                matrixB = input_matrix()
                print_matrix(add_matrices(matrixA,matrixB),s="Matrix A+B is equal to:\n")
                break

            elif n==2:
                print("For the starting matrix A:")
                matrixA = input_matrix()
                print_matrix(transpose(matrixA),"The transpose of matrix A is equal to:\n")
                break

            elif n==3:
                print("For matrix A:")
                matrixA = input_matrix()
                print("For matrix B:")
                matrixB = input_matrix()
                print_matrix(multiply_matrices(matrixA,matrixB),s="Matrix AB is equal to:\n")
                break
            elif n==4:
                print("For matrix A:")
                matrixA= input_matrix()
                print("det(matrixA) =",determinant(matrixA))
                break

            else:
                print("Invalid input, try again")
        except ValueError:
            print("Invalid input, try again")
            continue
        except EOFError:
            sys.exit("\n")


def create_matrix(rows,cols):

    #create an empty matrix of dimensions rowsxcols
    default = 0
    return [[default] * cols for _ in range(rows)]



def input_matrix():
    while True:
        try:
            rows = int(input("Enter number of rows:"))
            cols = int(input("Enter number of columns:"))
            break
        except ValueError:
            print("Invalid input,try again")

    matrix = create_matrix(rows,cols)

    elements=[]
    print("Enter the rows of the matrix, one by one, seperating each element with a whitespace.")
    try:
        i=0
        while i<rows:
            temp = input(f"Row {i+1}:")
            arr = temp.strip().split(" ")
            if len(arr) != cols:
                print("Invalid input, try again")
                continue
            for element in arr:
                if not isinstance(float(element), (int, float)):
                    raise(ValueError)
            matrix[i] = arr
            i += 1

    except ValueError:
        sys.exit("Invalid input for matrix elements.")

    return matrix


def print_matrix(matrix,s=""): #s: output string
    print(s,end="")
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            print(f"{float(matrix[i][k])} ",end="")
        print("")


        #print("")
def rowscols(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    return(rows,cols)

def add_matrices(matrixA,matrixB):

    if rowscols(matrixA) == rowscols(matrixB):
        r = rowscols(matrixA)[0]
        c = rowscols(matrixB)[1]
        new_matrix = create_matrix(r,c)
        for i in range(r):
            for k in range(c):
                new_matrix[i][k] = float(matrixA[i][k]) + float(matrixB[i][k])
        return new_matrix
    else:
        raise ValueError("Matrix A and B cannot be added.")


def transpose(matrix):
    r,c = rowscols(matrix)
    new_matrix = create_matrix(c,r)
    for i in range(r):
        for k in range(c):
            new_matrix[k][i] = float(matrix[i][k])
    return new_matrix

def multiplyrows(row1,row2):#helper function, will be needed in matrix multiplication. returns a single element.
    sum = 0
    for i in range(len(row1)):
        sum += float(row1[i])*float(row2[i])
    return sum


def multiply_matrices(matrixA,matrixB):

    rA,cA = rowscols(matrixA)
    rB,cB = rowscols(matrixB)

    if cA == rB:
        new_matrix = create_matrix(rA,cB)
        transB = transpose(matrixB)
        for i in range(rA):
            for k in range(cB):
                new_matrix[i][k] = multiplyrows(matrixA[i],transB[k])
        return new_matrix
    else:
        raise ValueError("These matrices cannot be multiplied.")



def determinant(matrix):

    rows, cols = rowscols(matrix)
    if rows==cols:

        if rows==2:
            return (float(matrix[0][0])*float(matrix[1][1])-float(matrix[0][1])*float(matrix[1][0]))
        else:
            det = 0
            for i in range(len(matrix)):
                sgn = pow(-1,i)

                sub = [row[:i] + row[i+1:] for row in matrix[1:]]
                det += sgn * float(matrix[0][i]) *determinant(sub)
        return det
    else:
        raise ValueError("Not a square matrix.")




if __name__ == "__main__":
    main()
