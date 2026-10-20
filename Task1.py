print("Write sales records to the file:")

#sales list
sales=[1200, 450, 980, 1500, 3000]

#write each sale to the new line
with open("sales.txt","w") as f:
    for amount in sales:
        f.write(str(amount)+'\n')

#read and prind the content
with open("sales.txt","r") as f:
    print(f.read())



# --- Optional 2: Write sales in comma-separated format

with open("sales.txt","w") as f:
    f.write(",".join(str(amount) for amount in sales))

with open("sales.txt","r") as f:
    print(f.read())
    
     



      