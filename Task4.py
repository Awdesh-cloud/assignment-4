print(" Task 4: Generate summary report from the file")

# Using only file reading operations:
# 1. Read all sales values from sales_data.txt.
# 2. Convert them into integers.
# 3. Calculate and print:
#    ○ Total Sales
#    ○ Highest Sale
#    ○ Lowest Sale
#    ○ Average Sale

with open("sales.txt", "r") as f:
    file = f.read()

# Replace newlines with commas, then split
parts= file.replace("\n",",").split(",")

# Convert to integers safely
sales = [int(x.strip()) for x in parts if x.strip()]


# Step 3: Calculate the summary
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)


print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)

