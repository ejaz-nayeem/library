

library=[
    {
        "title":"Abcd",
        "author":["A","f","VV"],
        "ISBN":"1234567899876",
        "publishing_year":1235,
        "price":3.7,
        "quantity":3,
        "available_books":3

        },
    {
        "title":"d",
        "author":["vv","S","Vb"],
        "ISBN":"1222234545459",
        "publishing_year":1222,
        "price":4.0,
        "quantity":1,
        "available_books":1

        },
    {
        "title":"fgD",
        "author":["y"],
        "ISBN":"1222234545454",
        "publishing_year":5656,
        "price":6.6,
        "quantity":6,
        "available_books":6

        }
    ]




def add_books():
    title=input("Enter title name: ")
    i=int(input("enter how many authors:"))
    writer=[]
    j=1
    while j<=i:
        j+=1
        author=input("Enter author name: ")
        writer.append(author)
        
    
    print("Enter ISBN: ")
    ISBN=input()
    if ISBN.isdigit() and len(ISBN)==13:
        pass
           
    else:
        print("wrong ISBN")
    
    publishing_year=input("enter 4 digit publishing year: ")
    if publishing_year.isdigit() and len(publishing_year)==4:
        pass
    else:
        print("wrong input_year")
    price=input("enter price in float: ")
    try:
        
        price=float(price)
    
        pass
    except ValueError:
        print("wrong input_price")
        
    quantity=input("quantity: ")
    try:
        quantity=int(quantity)
        pass
    except ValueError:
        print("wrong input_quantity")
    book={
        "title":title,
        "author":writer,
        "ISBN":ISBN,
        "publishing_year":publishing_year,
        "price":price,
        "quantity":quantity,
        "available_books":quantity

        }
    library.append(book)
    
#add_books()
#print(library)
def view_library():
    for i in library:
        
        print(i["title"],
          i["title"],
          i["author"],
          i["ISBN"],
          i["publishing_year"],
          i["price"],
          i["quantity"],
          i["available_books"],
          sep=" | "
          )
#view_library()
def search_book():
    book=input("enter book name or ISBN number: ")
    for i in library:
        if book.lower() in i["title"].lower() or book.lower() in i["ISBN"]:
            print(f"Found: title is '{i['title']}',author is '{i['author']}'")
#search_book()
def search_by_author():
    author_name=input("enter author name: ")
    for i in library:
        
        for j in i["author"]:
            
            if author_name.lower()==j.lower():
                
                print(i["title"])
#search_by_author()

def remove():
    book_name=input("enter book name you want to remove: ")
    for i in library:
        
        if book_name==i["title"]:
            library.remove(i)
#remove()
#view_library()
lent_books=[]
def lend_or_return_book():
    print("enter the book-name: ")
    
    title=input()
    for i in library:
        if i["title"].lower()==title.lower():
            available_books=i["available_books"]
    
            print("you want to lend or return book?")
            x=input()
            if x.lower()=="lend":
                if available_books!=0:
                    print("enter your name below:")
                    name=input()
                    available_books=i["available_books"]-1
                    tuple=(i["title"],name)
                    lent_books.append(tuple)
                    print(available_books)
                    i["available_books"]=i["available_books"]-1
                else:
                    print("not available to lend")
            elif x.lower()=="return":
                if available_books!=i["quantity"]:
                    available_books=i["available_books"]+1
                    print(available_books)
                    i["available_books"]=i["available_books"]+1
                else:
                    print("this book is not from here")
            else:
                print("wrong input")
def view_lent_books():
    for i,j in lent_books:
        
        print("book name: ",i,"reder name: ",j)
        
def library_txt():
    with open("library.txt", "w") as f:
        
        for book in library:
            
            f.write("Title: " + book["title"] + "\n")
            f.write("Authors: " + ", ".join(book["author"]) + "\n")
            f.write("ISBN: " + book["ISBN"] + "\n")
            f.write("Publishing Year: " + str(book["publishing_year"]) + "\n")
            f.write("Price: $" + str(book["price"]) + "\n")
            f.write("Quantity: " + str(book["quantity"]) + "\n")
            f.write("Available Books: " + str(book["available_books"]) + "\n")
            f.write("\n" + "-"*40 + "\n\n")

    with open("library.txt", "r") as f:
        
        contents = f.read()
        print(contents)
        
def menu():
    while True:
        
        
        print("Welcome")
        menu="""
        1. View Library
        2. Add Book
        3. Romove Book
        4. Search Book by Name/ISBN
        5. Search Book by Author
        6. Lend or return Book
        7. View who and which book is lent
        8. View in txt file 
        9. Exit
        """
        print(menu)
        choice=input()
    #while choice!="8":
        
        if choice=="1":
            
            
            view_library()
        elif choice=="2":
        
            add_books()
        elif choice=="3":
        
            remove()
        elif choice=="4":
        
            search_book()
        elif choice=="5":
            search_by_author()
        elif choice=="6":
            lend_or_return_book()
        elif choice=="7":
            view_lent_books()
        elif choice=="8":
            library_txt()
        elif choice=="9":
            print("exiting")
            break
    
        else:
            print("wrong choice")
menu()
#library_txt()
    
    
    

    
