print("Task 7: Mini Project - Export discounted prices")
# Create a dictionary:
# prices = {
#     "Mouse": 500,
#     "Keyboard": 800,
#     "Monitor": 7000,
#     "Pendrive": 400,
#     "Camera": 5000
# }

# Ask the user for a discount percentage.
# Write discounted prices into discount_report.txt using:
# Product | Original Price | Discounted Price

# After writing, read the file and print it to the terminal.

# Extra (optional): Write a summary at the bottom of the file:
# Total Items: X
# Average Discounted Price: Y

prices = {
     "Mouse": 500,
     "Keyboard": 800,
     "Monitor": 7000,
     "Pendrive": 400,
    "Camera": 5000
}


# Ask the user for the discount
discount_percentage= float(input("Please tell me the discount price in percentage: "))
discount_report = []

#calculate the dicouted price
for product,price in prices.items():
    reduced_price= price - (price* discount_percentage)
    discount_report.append((product, price, reduced_price))
   

# Write to file
with open("discount_report.txt","w") as f:
    f.write(f"{'Product':<12} | {'Price':<15} | {'discounted_Price':<15}\n")
    f.write(f"------------------------------------\n")
    for product, price, reduced_price in  discount_report:
        f.write(f"{product:<12}| {price:<15}| {reduced_price:<15.2f}\n")
  
    #summary
    total_items=len(discount_report)
    avg_discounted_price= sum( r for _,_,r in discount_report)/total_items
    f.write("\nSummary \n")
    f.write(f"Total items: {total_items}\n")
    f.write(f"Average disconted price: {avg_discounted_price:.2f}\n")





# Read and print
with open("discount_report.txt","r") as f:
    print(f.read())


# I have to submit after checking all the task. 
