class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"

book1 = Book("Chasing the sun", "Jonaxx", 2016)
book2 = Book("Stay awake Agatha", "Agatha Christine", 1942)
book3 = Book("Hell university", "J.M Dorhower", 2016)

print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
