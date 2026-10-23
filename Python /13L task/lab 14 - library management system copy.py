# Library Book Management System

# Initial collections
books = [
    ("Python Basics", "John", 2023, "Programming"),
    ("Cloud Computing", "Aman", 2024, "Cloud")
]

library_categories = {"Programming", "Cloud", "AI"}
student_wishlist = {"AI", "Cybersecurity"}

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. View Books")
    print("2. Add Book")
    print("3. View Categories")
    print("4. Add Wishlist")
    print("5. Gap Analysis")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1. View Books
    if choice == "1": 
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in books:
                title, author, year, category = book
                print("Title:", title)
                print("Author:", author)
                print("Year:", year)
                print("Category:", category)
                print("------------------")

            print("Total books:", len(books))

    # 2. Add Book
    elif choice == "2":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category: ").strip()

        if title and author and year and category:
            if year.isdigit():
                new_book = (title, author, int(year), category)
                books.append(new_book)
                library_categories.add(category)
                print("SUCCESS: Book added!")
            else:
                print("ERROR: Year must be a number.")
        else:
            print("ERROR: All fields are mandatory.")

    # 3. View Categories
    elif choice == "3":
        print("\nLibrary Categories:")
        for category in sorted(library_categories):
            print(category)

        print("Total categories:", len(library_categories))

    # 4. Add Wishlist
    elif choice == "4":
        category = input("Enter requested category: ").strip()

        if category:
            student_wishlist.add(category)
            print("SUCCESS: Added to wishlist!")
        else:
            print("ERROR: Category cannot be empty.")

    # 5. Gap Analysis
    elif choice == "5":
        already_in_stock = library_categories & student_wishlist
        purchase_needed = student_wishlist - library_categories
        full_coverage = library_categories | student_wishlist

        print("\n===== GAP ANALYSIS =====")
        print("Already in Stock:", already_in_stock)
        print("Purchase Needed:", purchase_needed)
        print("Full Combined Coverage:", full_coverage)

    # 6. Exit
    elif choice == "6":
        print("Thank you! Goodbye!")
        break

    # Invalid choice
    else:
        print("INVALID: Enter a number from 1 to 6.")