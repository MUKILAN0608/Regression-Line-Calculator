import numpy as np

def calculate_regression():
    print("---- Regression Line Calculator ----")
    regression_input = input("Choose input method:\n1. Statistical values (SD, mean)\n2. Data points (X and Y values)\nEnter choice (1/2): ")

    if regression_input == '1':
        print("\n--- Enter Statistical Data ---")
        rc = float(input("Regression Coefficient (Correlation Coefficient): "))
        meanX = float(input("Mean of X: "))
        meanY = float(input("Mean of Y: "))
        SDX = float(input("Standard Deviation of X: "))
        SDY = float(input("Standard Deviation of Y: "))

        BXY = rc * (SDX / SDY)
        BYX = rc * (SDY / SDX)
        RXL = meanX - (BXY * meanY)
        RYL = meanY - (BYX * meanX)

        choose_option(BXY, RXL, BYX, RYL)

    elif regression_input == '2':
        print("\n--- Enter Data Points ---")
        x_values = list(map(float, input("Enter X values separated by space: ").split()))
        y_values = list(map(float, input("Enter Y values separated by space: ").split()))

        if len(x_values) != len(y_values):
            print("Error: The number of X and Y values must match.")
            return

        meanX = np.mean(x_values)
        meanY = np.mean(y_values)
        SDX = np.std(x_values, ddof=1)
        SDY = np.std(y_values, ddof=1)
        rc = np.corrcoef(x_values, y_values)[0, 1]

        BXY = rc * (SDX / SDY)
        BYX = rc * (SDY / SDX)
        RXL = meanX - (BXY * meanY)
        RYL = meanY - (BYX * meanX)

        choose_option(BXY, RXL, BYX, RYL)

    else:
        print("Invalid choice! Please enter 1 or 2.")

def choose_option(BXY, RXL, BYX, RYL):
    print("\n--- Choose Next Action ---")
    print("1. Calculate Y value from X\n2. Calculate X value from Y\n3. Display Regression Equations")
    opt = input("Enter your choice (1/2/3): ")

    if opt == '1':
        calculate_y(BYX, RYL)
    elif opt == '2':
        calculate_x(BXY, RXL)
    elif opt == '3':
        display_regression_lines(BXY, RXL, BYX, RYL)
    else:
        print("Invalid option selected!")

def display_regression_lines(BXY, RXL, BYX, RYL):
    print("\n--- Regression Lines ---")
    x_on_y = f'X = {BXY:.4f}Y + {RXL:.4f}' if RXL >= 0 else f'X = {BXY:.4f}Y - {abs(RXL):.4f}'
    y_on_x = f'Y = {BYX:.4f}X + {RYL:.4f}' if RYL >= 0 else f'Y = {BYX:.4f}X - {abs(RYL):.4f}'
    
    print(f"X on Y: {x_on_y}")
    print(f"Y on X: {y_on_x}")

def calculate_y(BYX, RYL):
    x = float(input("Enter the X value: "))
    y_val = BYX * x + RYL
    print(f'Result: Y = {y_val:.4f}')

def calculate_x(BXY, RXL):
    y = float(input("Enter the Y value: "))
    x_val = BXY * y + RXL
    print(f'Result: X = {x_val:.4f}')


calculate_regression()
