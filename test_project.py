from project import determinant,multiply_matrices,transpose,multiplyrows,add_matrices
import pytest



def test_determinant():

    matrix1 = [[2,2],[3,4]]
    assert determinant(matrix1) == 2

    matrix2 = [[2,2,3],[3,4,1],[1,5,6]]
    assert determinant(matrix2) == 37

    matrix3 = [[2,2,1],[3,4,2]]
    with pytest.raises(ValueError):
        assert determinant(matrix3) == "Not a square matrix."


def test_transpose():

    matrix1 = [[2,2],[3,4]]
    assert transpose(matrix1) == [[2,3],[2,4]]

    matrix2 = [[2,2,3],[3,4,1],[1,5,6]]
    assert transpose(matrix2) == [[2,3,1],[2,4,5],[3,1,6]]


def test_add_matrices():

    matrix1 = [[2,2],[3,4]]
    matrix2 = [[1,1],[2,2]]

    assert add_matrices(matrix1,matrix2) == [[3,3],[5,6]]

    matrix1 = [[2,2],[3,4],[1,4]]
    matrix2 = [[1,1],[2,2]]

    with pytest.raises(ValueError):
        assert add_matrices(matrix1,matrix2) == "These matrices cannot be added."

def test_multiplyrows():

    r1 = [1,2,3]
    r2 = [-1,0,4]

    assert multiplyrows(r1,r2) == 11

def test_multiply_matrices():
    matrix1 = [[1,1],[2,2]]
    matrix2 = [[3,4],[5,5]]

    assert multiply_matrices(matrix1,matrix2) == [[8,9],[16,18]]

    matrix1 = [[1,1,1],[2,2,1]]
    matrix2 = [[3,4],[5,5]]


    with pytest.raises(ValueError):
        assert multiply_matrices(matrix1,matrix2) == "These matrices cannot be multiplied."
