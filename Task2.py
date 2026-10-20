print("Task 2 --> read the file from different ways+  '\n")
# using the same sales.txt 
    #1. read the entire file using the read() and print it
    # 2. Read the first line using the readline()
    # 3. Read all lines using the readlines() and convert them into the list of integers
    # Ensure Proper foratting and cleanup the new lines.
sales = [1200, 450, 980, 1500, 3000]

#First, write the sales in comma-separated format (optional setup)
with open("sales.txt","w") as f:
        f.write(",".join(str(amount) for amount in sales) )
       

with open("sales.txt","r") as f:
    print(f.read())

# all value in different line
with open("sales.txt",'w') as f:
      for amount in sales:
            f.write(str(amount)+ '\n')

#read and prints content
with open("sales.txt","r") as f:
      print("Using .read(): ")
      print(f.read())

with open("sales.txt","r") as f:
      print("Using .readline(): ")
      print(f.readline())

with open("sales.txt","r") as f:
      print("Using .readlines() to readlines and convert them into integer")
      lines=f.readlines()

# cleanup: remove \n and convert to integers
numbers= [int(line.strip()) for line in lines]
print(numbers)
print("*" * 80,"Question 2 end here")

#***********************************************************************************************
print("Task 3: Append new sales")
new_sales=[5000,2500,1700]
with open("sales.txt",'a') as f:
      f.write( ",".join(str(amount)for amount in new_sales))

#read the updated file
with open("sales.txt",'r') as f:
      print(f.read())



