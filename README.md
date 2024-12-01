# Rent-Calculator

This is a simple Python-based Rent Calculator program that helps to split the expenses of a hostel or flat among the residents. It calculates the total expenditure per person by considering the rent, food cost, and electricity charges. The program then divides the total expenses by the number of persons living in the accommodation to determine how much each person needs to pay.

## Features

- Takes input for:
  - Hostel/flat rent
  - Amount spent on food
  - Total electricity expenditure
  - Charge per unit of electricity
  - Number of persons living in the flat or hostel
- Calculates the total electricity bill based on the consumption and charge per unit.
- Splits the total rent, food, and electricity expenditure among all the persons.
- Outputs the amount each person needs to pay.

## Requirements

- Python 3.x (recommended version: 3.6+)

## How to Use

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the folder where the `rent_calculator.py` file is located.
4. Run the Python script using the command:
   ```
   python rent_calculator.py
   ```
5. Enter the following inputs when prompted:
   - Hostel/flat rent
   - Amount of food ordered
   - Total electricity expenditure
   - Charge per unit of electricity
   - Number of persons living in the flat or hostel
6. The program will calculate and display how much each person needs to pay based on the total expenses.


## Code Explanation

1. **Input values**: The user is prompted to input the rent, food cost, electricity spend, charge per unit of electricity, and the number of persons living in the flat/hostel.
   
2. **Electricity bill calculation**: The total electricity bill is calculated by multiplying the electricity spend by the charge per unit.

3. **Total expenditure calculation**: The total expenditure is calculated by adding the rent, food cost, and total electricity bill.

4. **Split the cost**: The total expenditure is then divided by the number of persons to calculate how much each person should pay.

5. **Output**: The amount each person needs to pay is displayed.



