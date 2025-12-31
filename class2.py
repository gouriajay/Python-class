heading = """BookStore Receipts"""

book1 = "Books:\t{}\tPrice:\t₹{}\n".format("Python Basics", 450)
book2 = "Books:\t{}\tPrice:\t₹{}\n".format("Data Science Intro", 600)

total = 450 + 600
message = "Thank you for shopping!"

receipt = ( heading + "\n\n" + book1 + book2 + "\nTotal:\t₹{}\n\n".format(total) + message)

print(receipt.upper())


