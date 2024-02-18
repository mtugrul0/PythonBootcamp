class Library:
 
  def __init__(self):
    self.file = open("books.txt", 'a+')

  def list_book(self):
    self.file.seek(0)
    book_data = self.file.read().splitlines()
    for books in book_data:
      book_info = books.strip().split(",")
      print(f'{book_info[0]}, {book_info[1]}')

  def add_book(self):
    book_title = input('Book Name: ')
    author = input('Author Name: ')
    first_release_year = input('First Release Year: ')
    page_number = input('Page Number: ')
    self.file.write(f'Book Name: {book_title}, Author Name: {author}, First Release Year: {first_release_year}, Page Number: {page_number}\n')
    print("Book added successfully.")
  
  def remove_book(self):
    book_title = input("Enter the name of book you want to remove: ")
    with open("books.txt", "r") as file:
      lines = file.readlines()

    with open("books.txt", "w") as file:
      for line in lines:
        if book_title not in line:
          file.write(line)

    print("Book was removed successfully")
 
  def __del__(self):
    self.file.close()

lib = Library()

while True:
  print("""
  ***MENU***
1) List Books
2) Add Book
3) Remove Book
4) Exit
  """)

  choice = input('Chose a value: ')

  if choice == "1":
    lib.list_book()
  elif choice == "2":
    lib.add_book()
  elif choice == "3":
    lib.remove_book()
  elif choice == "4":
    print("Program was closed.")
    break
  else:
    print('Please chose a valid value.')