import numpy as np

def matrix_input(rows, cols):
    """Takes matrix input from the user"""
    print(f"Enter the elements of the matrix ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Error: Enter exactly {cols} numbers!")
            return None
        matrix.append(row)
    return np.array(matrix)

def print_menu():
    """Prints the operations menu"""
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Determinant (Square matrix only)")
    print("5. Adjoint (Square matrix only)")
    print("6. Inverse (Square matrix only)")
    print("7. Exit")

def perform_operation(matrix1, matrix2, operation):
    """Performs the specified matrix operation"""
    if operation == 1:  # Addition
        if matrix1.shape == matrix2.shape:
            return matrix1 + matrix2
        else:
            print("Error: For addition, matrices must have the same dimensions.")
            return None
    elif operation == 2:  # Subtraction
        if matrix1.shape == matrix2.shape:
            return matrix1 - matrix2
        else:
            print("Error: For subtraction, matrices must have the same dimensions.")
            return None
    elif operation == 3:  # Multiplication
        if matrix1.shape[1] == matrix2.shape[0]:
            return np.dot(matrix1, matrix2)
        else:
            print("Error: For multiplication, the number of columns in the first matrix must equal the number of rows in the second matrix.")
            return None
    else:
        return None

def determinant(matrix):
    """Finds the determinant of a square matrix"""
    return np.linalg.det(matrix)

def adjoint(matrix):
    """Finds the adjoint of a square matrix"""
    cofactor_matrix = np.linalg.inv(matrix).T * np.linalg.det(matrix)
    return cofactor_matrix.T

def inverse(matrix):
    """Finds the inverse of a square matrix"""
    if np.linalg.det(matrix) == 0:
        return None
    return np.linalg.inv(matrix)

def main():
    """Main function to handle matrix operations"""
    
    # Welcome note in bold style
    print("\033[1m" + "Welcome to the Matrix Operations Program!" + "\033[0m")
    print("\033[1m" + "You can perform addition, subtraction, multiplication, determinant, adjoint, and inverse of matrices." + "\033[0m")
    
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))
    
    matrix1 = matrix_input(rows1, cols1)
    if matrix1 is None:
        return

    while True:
        print_menu()
        choice = int(input("Enter your choice (1-7): "))

        if choice == 7:
            print("Exiting program.")
            break

        if choice in [1, 2, 3]:
            # Matrix addition, subtraction, or multiplication requires a second matrix
            rows2 = int(input("Enter the number of rows for the second matrix: "))
            cols2 = int(input("Enter the number of columns for the second matrix: "))
            matrix2 = matrix_input(rows2, cols2)
            if matrix2 is None:
                return

            result = perform_operation(matrix1, matrix2, choice)
            if result is not None:
                print("\nResultant Matrix:")
                print(result)

        elif choice == 4:  # Determinant
            if rows1 != cols1:
                print("Error: Determinant is only defined for square matrices.")
            else:
                det = determinant(matrix1)
                print(f"\nDeterminant: {det}")

        elif choice == 5:  # Adjoint
            if rows1 != cols1:
                print("Error: Adjoint is only defined for square matrices.")
            else:
                adj = adjoint(matrix1)
                print("\nAdjoint Matrix:")
                print(adj)

        elif choice == 6:  # Inverse
            if rows1 != cols1:
                print("Error: Inverse is only defined for square matrices.")
            else:
                inv = inverse(matrix1)
                if inv is None:
                    print("Matrix is singular, inverse does not exist.")
                else:
                    print("\nInverse Matrix:")
                    print(inv)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
