paragraph = """Python is a powerful programming language.
This Python course is designed for beginners to learn Python easily and effectively."""

print("length of paragaph:",len(paragraph))

print("First character of paragraph:",paragraph[0])

print("Second character of paragraph:",paragraph[-1])

print("Slicing:",paragraph[:50])

print("Replace:",paragraph.replace("Python","PYTHON"))

print("lowercase:",paragraph.lower())

print("Remove whitespace:",paragraph.strip())

print("Split:",paragraph.split())

print("Checking:","course"in paragraph)

print("The course description is {} characters long and has {} words."
      
.format(len(paragraph.strip()),len(paragraph.split()))
)
