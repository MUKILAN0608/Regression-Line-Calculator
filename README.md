# Regression-Line-Calculator
This repository contains an interactive Python program to calculate regression lines and perform related calculations. The program supports two input methods: statistical values (e.g., mean, standard deviation) and raw data points. It enables users to compute regression coefficients and regression equations, as well as make prediction
Features
Input Methods:

Statistical Data: Users can provide the correlation coefficient, means, and standard deviations of X and Y.
Data Points: Users can input raw X and Y values directly, and the program will compute the required statistics.
Regression Equations:

Calculates both regression lines:
𝑋
X on 
𝑌
Y: 
𝑋
=
𝐵
𝑋
𝑌
𝑌
+
𝑅
𝑋
𝐿
X=B 
XY
​
 Y+R 
XL
​
 
𝑌
Y on 
𝑋
X: 
𝑌
=
𝐵
𝑌
𝑋
𝑋
+
𝑅
𝑌
𝐿
Y=B 
YX
​
 X+R 
YL
​
 
Prediction Capabilities:

Predict 
𝑌
Y given 
𝑋
X using the 
𝑌
Y-on-
𝑋
X regression line.
Predict 
𝑋
X given 
𝑌
Y using the 
𝑋
X-on-
𝑌
Y regression line.
Detailed Outputs:

Displays regression equations with coefficients rounded to four decimal places.
Outputs prediction results with high precision.
Program Flow
User Input:

Choose input method: statistical values or data points.
Provide required inputs based on the chosen method.
Calculation:

If statistical values are provided, the program uses them directly.
If data points are provided, the program computes means, standard deviations, and the correlation coefficient.
Regression Lines:

Computes slopes (
𝐵
𝑋
𝑌
B 
XY
​
  and 
𝐵
𝑌
𝑋
B 
YX
​
 ) and intercepts (
𝑅
𝑋
𝐿
R 
XL
​
  and 
𝑅
𝑌
𝐿
R 
YL
​
 ).
Displays the regression equations.
Further Actions:

Predict 
𝑌
Y from 
𝑋
X.
Predict 
𝑋
X from 
𝑌
Y.
View regression equations.
Key Functions
calculate_regression(): Main function that handles user input and computes regression equations.
choose_option(): Allows users to choose actions such as prediction or displaying regression lines.
display_regression_lines(): Displays regression equations for 
𝑋
X on 
𝑌
Y and 
𝑌
Y on 
𝑋
X.
calculate_y(): Computes 
𝑌
Y from 
𝑋
X using the regression line 
𝑌
Y on 
𝑋
X.
calculate_x(): Computes 
𝑋
X from 
𝑌
Y using the regression line 
𝑋
X on 
𝑌
Y.
How to Run
Install Python (if not already installed).
Ensure NumPy is installed (pip install numpy).
Run the script:
bash
Copy code
python regression_calculator.py
Follow the on-screen prompts to input data and perform calculations.
Example
Input:
sql
Copy code
Choose input method:
1. Statistical values (SD, mean)
2. Data points (X and Y values)
Enter choice (1/2): 2
Enter X values separated by space: 1 2 3 4 5
Enter Y values separated by space: 2 4 6 8 10
Output:
csharp
Copy code
--- Regression Lines ---
X on Y: X = 0.5000Y + 0.0000
Y on X: Y = 2.0000X + 0.0000
Prediction:
arduino
Copy code
Enter your choice (1/2/3): 1
Enter the X value: 6
Result: Y = 12.0000
Contribution
Contributions are welcome! Feel free to submit issues or pull requests to enhance functionality or improve the codebase.
