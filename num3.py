import numpy as np


def solve_linear_system():
    try:
        print("Решение системы линейных уравнений:")
        print("a11*x + a12*y = b1")
        print("a21*x + a22*y = b2")

        a11 = float(input("a11 = "))
        a12 = float(input("a12 = "))
        a21 = float(input("a21 = "))
        a22 = float(input("a22 = "))
        
        A = np.array([[a11, a12],
                      [a21, a22]])
        
        b1 = float(input("b1 = "))
        b2 = float(input("b2 = "))
        
        b = np.array([b1, b2])
        
        det_A = np.linalg.det(A)
        
        if abs(det_A) < 1e-10:
            print("Система не имеет единственного решения")
        else:
            solution = np.linalg.solve(A, b)
            x, y = solution
            
            print("Решение системы:")
            print(f"x = {x:.6f}")
            print(f"y = {y:.6f}")
    
    except ValueError:
        print("Ошибка: введите числовые значения!")
    except np.linalg.LinAlgError as e:
        print(f"Ошибка при решении системы: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    solve_linear_system()
