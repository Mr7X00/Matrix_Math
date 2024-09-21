# Matrix_Math
This Python program allows users to perform various matrix operations such as addition, subtraction, multiplication, finding the determinant, adjoint, and inverse of matrices. It takes input matrices from the user and provides an interactive menu to choose the desired operation.

Features
Addition of two matrices
Subtraction of two matrices
Multiplication of two matrices
Determinant of a square matrix
Adjoint of a square matrix
Inverse of a square matrix (if it exists)
Requirements
Python 3.x
NumPy library
You can install NumPy using pip:

bash
Copy code
pip install numpy
How to Run the Program
Clone this repository or download the program file matrix_operations.py.
Ensure that Python 3.x and NumPy are installed.
Open a terminal or command prompt and navigate to the directory containing matrix_operations.py.
Run the program:
bash
Copy code
python matrix_operations.py
The program will prompt you to enter the dimensions and elements of the matrices.

Follow the menu to choose an operation:

Addition (1): Add two matrices of the same dimension.
Subtraction (2): Subtract two matrices of the same dimension.
Multiplication (3): Multiply two matrices (the number of columns of the first matrix must equal the number of rows of the second matrix).
Determinant (4): Calculate the determinant of a square matrix.
Adjoint (5): Calculate the adjoint of a square matrix.
Inverse (6): Calculate the inverse of a square matrix (if the matrix is non-singular).
Exit (7): Exit the program.
Example Usage
bash
Copy code
Enter the number of rows for the first matrix: 3
Enter the number of columns for the first matrix: 3
Enter the elements of the matrix (3x3):
Row 1: 1 2 3
Row 2: 4 5 6
Row 3: 7 8 9

Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Determinant
5. Adjoint
6. Inverse
7. Exit
Enter your choice (1-7): 4

Determinant: 0.0
Notes
Square Matrices: The determinant, adjoint, and inverse can only be calculated for square matrices (i.e., matrices with the same number of rows and columns).
Matrix Inverse: If the determinant of a matrix is 0, the matrix is singular, and its inverse does not exist.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
