 # THE MATRIX PLAYGROUND
    #### Description:
        This is a simple program which performs linear algebra operations on matrices, such as addition, tranposation,
    multiplication aswell as finding the determinant, without using the NumPy library. As an electrical and computer engineering student who likes
    mathematics and coding, this was a fun project which could combine my two interests into something useful and productive.
        The program starts by showing a menu of all the possible aforementioned operations, prompting the user to choose one
    by entering the corresponding integer into the console.
        For every possible operation, the user has to input matrices in order for the program to work. At first, I thought that the
    user should input the elements of the matrix one by one, however I noticed that this was very time consuming. Instead, the user is
    prompted to enter the matrices row by row, seperated by whitespace, so that the whole process is faster and less annoying for the user.

        Let's explore each of the functions in the program one by one:

        -> create_matrix(rows,cols):
            This function is called as soon as the user inputs the number of rows and columns of his desired matrix.
            A matrix of dimensions rows x cols is returned with each element having a default starting value of 0.
            This way, we can safely start managing and performing operations on matrices.

        -> input_matrix():
            This function is responsible for excracting the user's input and turning it into a 2d matrix.
            It prompts the user to enter the matrix elements row by row, after asking for the dimensions of the matrix.
            Incase of a misinput, which consists of anything that is not a float, an error message is printed and the user
            can try entering elements in the correct format again.
            A matrix which consists of the elements inserted by the user is returned.

        -> rowscols(matrix):
            A simple function which takes a matrix as a parameter and returns its number of
            rows and columns in a tuple.
            This will make the following functions easier and faster to implement.

        -> add_matrices(matrixA,matrixB)
            This function takes as input two matrices, A and B.
            If the two matrices have the same dimensions, then the matrix A+B is computed by adding each
            corresponding element of the two matrices and the function returns it.
            If the two matrices don't have the same dimensions, then there's no point in talking about addition between them,
            so a ValueError is raised.

        -> transpose(matrix)
            The point of this function is to compute the transpose of the inserted matrix and return it.
            We recall that we can find the transpose of a matrix by swapping the rows and the columns of the starting matrix,
            or, in other words, taking each element at position (i,k) in the starting matrix and putting it at position (k,i) in the transpose.

        ->multiplyrows(row1,row2):
            A helper function, used later in matrix multiplication. We define row multiplication as the number which emerges by multiplying
            corresponding elements which are in the same position in the two rows, and adding them all up. for example:
            multiplyrows([1,2,3],[2,3,4]) = 1*2 +2*3 +3*4 = 2+6+12 = 20

        -> multiply_matrices(matrixA,matrixB):

            This function takes as input two matrices, matrixA and matrixB, and performs the multiplication AB.
            Let's not forget that in linear algebra generally AB != BA, and that's why its specified in the input of this function.
            Now, to make things more simple, since we have already implemented the transpose() function, I decided to take an approach
            which is different than the traditional in the classic matrix multiplication algorithm.
            In the original matrix multiplication, we start with the first row and we multiply each corresponding element with the first column of matrixB, and
            the result is the first element of matrix AB.
            In this approach, we transpose the right matrix B and we start by multiplying the first row of matrix A with the first row of matrix transpose(B)
            for the first element. Then we multiply the first row of A with the second row of transpose(B) to get the element at (1,2) etc.
            I found this technique easier to implement, since we have all the above helper functions available to us.
            If AB cannot be defined, which means that A's columns are not equal to B's rows, a ValueError is raised.

        ->determinant(matrix)

            As our final function, determinant(matrix) returns the determinant of the inserted matrix, as long as it's a square matrix, which means
            that the number of rows and columns of the matrix must be equal.
            If the matrix is 2x2, then the determinant is easily calculated with the known mathematic formula.
            If it's not, then recursion is used to calculate the determinants of all the sub-matrixes which are formed by the known linear algebra algorithm,
            until all that's left are 2x2 matrices.
            If a non square matrix is inserted, then the function raises a ValueError.

        ->main():
            main() is responsible for printing the menu of all possible operations to the user and then calling the appropriate functions,
            according to the user's input.

    Most of the functions are then tested using pytest in the test_project.py file, so that we can assure than the algorithms are working as expected.




