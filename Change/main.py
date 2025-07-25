# main.py: Convert the change given in quarters, dimes, nickels, and pennies into dollars and cents
# By: Husnain Masood
# Modified: 2/24/2025

# 1. Get amount of quarters 
quarter = int(input("Enter the number of quarters: "))

# 2. Get amount of dimes
dime = int(input("Enter the number of dimes: "))
 
# 3. Get amount of nickels
nickel = int(input("Enter the number of nickels: "))

# 4. Get amount of pennies
penny = int(input("Enter the number of pennies: "))

# 5. Calculate the total value in cents
cents_total = quarter * 25 + dime * 10 + nickel * 5 + penny

# 6. Convert the total value into dollars and cents
dollar = cents_total // 100
cent = cents_total % 100 

# 7. Output the result
print(f"Total change adds up to {dollar} dollars and {cent} cents ({quarter}Q + {dime}D + {nickel}N + {penny}P = ${dollar}.{cent:02d}).")
