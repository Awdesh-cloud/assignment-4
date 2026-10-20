print("Task 5: Create Product Info File (User Input)")

# 1. Ask the user for 3 product names & their prices.
# 2. Write them into a new file products.txt in this format:
# 3. ProductName | Price
# 4. Read the file and print each line with proper formatting.

# ask the user to enter 3 product names and prices
products=[]
for i in range(3):
    product= input("Please enter the productname: ")
    price= input("Please enter the price of the prouct: ")
    products.append((product,price))

#write them into products.txt
with open("products.txt","w") as f:
    for name,price in products:
        f.write(f"{name}  | {price} \n")

#Read the file
with open("products.txt","r") as file:
    print(f"{'Product':<15} {'Price':>10}")
    print("-"*27)
    for line in file:
        #print("Product info:",line.strip())
        if "|" in line: # only split if separator exists
            name,price=line.split("|")
            print(f"{name.strip():<15} | {price.strip():>10}")



    
