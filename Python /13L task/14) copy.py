books = [
    ("Python Basics", "John Doe", "2021", "Programming"),
    ("Machine Learning", "Jane Smith", "2022", "AI")
]
library_categories = {"Programming", "AI"}
student_wishlist = {"AI", "Cloud"}

while True:
    print("\n1. View Books\n2. Add Book\n3. View Categories\n4. Add Wishlist\n5. Gap Analysis\n6. Exit")
    choice = input("Prompt: Input choice (1-6): ").strip()

    if choice == '1':
        for title, author, year, category in books:
            print(f"{title}, {author}, {year}, {category}")
        print(f"Total count: {len(books)}")

    elif choice == '2':
        title = input("Prompt: title: ").strip()
        author = input("author: ").strip()
        year = input("year: ").strip()
        category = input("category: ").strip()

        if title and author and year and category:
            books.append((title, author, year, category))
            library_categories.add(category)
            print("[SUCCESS] Book added")
        else:
            print("[ERROR] All fields mandatory")

    elif choice == '3':
        for cat in sorted(library_categories):
            print(cat)
        print(f"Total genres count: {len(library_categories)}")

    elif choice == '4':
        req_cat = input("Prompt: requested category: ").strip()
        if req_cat:
            student_wishlist.add(req_cat)
            print("[SUCCESS] Added to wishlist")
        else:
            print("[ERROR] Category cannot be empty")

    elif choice == '5':
        in_stock = library_categories & student_wishlist        
        to_order = student_wishlist - library_categories
        full_coverage = library_categories | student_wishlist

        print("Category Gap Analysis:")
        print(f"1. Already in Stock: {in_stock}")
        print(f"2. Purchase Order Needed: {to_order}")
        print(f"3. Full Combined Coverage: {full_coverage}")

    elif choice == '6':
        print("Thank you. Goodbye!")
        break

    else:
        print("[INVALID] Enter number 1-6")
