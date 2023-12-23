#Global variables
import json
#Lessons learned here:
#Functions should be named in an intuitive way that another engineer can understand 
#Fuctions should only do precisely what they're labeled to do. For example if it had to "Update book quantity", it should JUST do that. Not print the quantity of the books or print a statement etc.
#This is called "Pure functions"
#Moving onto the next project for now, but remember this for next time!! I outlined this in the "TO DO" sections 

def load_books(): #Opens the JSON file with book data
   with open('data.json', 'r') as file:
       library = json.load(file)
       return library


def save_books(data): #Writes changes made in the open JSON file to the original JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_book(title): #Loads the data associated with an inputted title #EDIT TO MAKE IT LOAD TITLE AS WELL
    # TODO: Let's make these functions more reusable. handle printing in the main method, return data for your functions
    # TODO: Make sure this is JUST "getting" the books data. It should not do anything that is not conferred by the name. This makes the program more organized
    # TODO: "Pure functions": A function that minds its own business, does not change any objects or variables that existed before it was called, for the same inputs it will always have the same outputs
    # Printing to the console is a side effect here, has nothing to do with actually getting the books data
    # Engineers have to trust that a function does what it's supposed to do without any side effects
    # TODO: Work on making the functions all pure functions

    x = load_books()
    if book_exists(title) == True:
        print("    Title: " + str(title))
        print(json.dumps(x[title], indent=4))
    else:
        print("The title you entered is not in library")

def display_all_books(): #Displays the data of all the books in the JSON file #NOT DISPLAYING TITLE AT THE MOMENT
    x = load_books()
    for title in x.keys():
        book_info = get_book(title)
        modified_book_info = str(book_info).replace("None","")
        print(modified_book_info)

def book_exists(title): #Checks if an inputted title exists in the JSON file
    # TODO: Explain this line: Return title in load_books()
    # TODO: curreny implementation is fine, this is just a more pythonic way of doing it
    x = load_books()
    if title in x:
        return True
    else:
        return False

def update_quantity(): #Updates the quantity of an inputted title
    title = input("Enter the title of the book you wish to update the quantity for: ")
    quantity = input("Enter the updated quantity: ")
    x = load_books()
    if book_exists(title) == True:
        x[title]['quantity'] = quantity
        save_books(x)
        y = x[title]['quantity']
        print("You successfully updated the quantity of the book " + str(title) + ". There are now " + str(y) + " available copies.") #logging
    else:
        print("The title you entered is not in the library")

def update_book(): #This one has to be reworked, remember you don't want the user to put in the field and value if the title doesn't exist
    title = input("Enter the title of the books for which you'd like to edit details :")
    x = load_books()

    if book_exists(title) == True:
        print("The current information is below: ")
        get_book(title)

        field = input("What field would you like to update? :")
        if field not in list(x[title].keys()):
            print("You did not enter a valid field")
        else:
            value = input("What integer or string would you like to be in that field instead of what is currently there? :")
            if field.lower() != "title":
                x[title][field] = value
            else:
                book_data = x[title]
                del x[title]
                x[value] = book_data
            save_books(x)
            print("The updated book data is below: \n")
            if field.lower() != "title":
                y = str((get_book(title))).replace("None", "")
            else:
                y = str((get_book(value))).replace("None", "")
            print(y)
    else:
        print("The title you entered is not in library")

def remove_book():
    title = input("Enter the title of the book you would like to remove: ")
    if book_exists(title) == True:
        title= str(title)
        x = load_books()
        del x[title]
        save_books(x)
        print(title + " has been removed from the library")
    else:
        print("The title you entered is not in library")

def add_book():
    title = input("Enter the title of the new book you'd like to add to the library: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year the book was published: ")
    quantity = input("Enter the number of books you'll be adding to the library: ")
    genre = input("Enter the genre of the book: ")
    x = load_books()
    if title not in x:
        x[title] = {
            "author": author,
            "year": year,
            "quantity": quantity,
            "genre": genre
        }
        save_books(x)
        print("\nThe data of the book you added is below: \n")
        print(str((get_book(title))).replace("None",""))
    else:
        print("The title you entered is already in the library")

def available_copies(title):
    x = load_books()
    print("Available copies of " + str(title) + ": " + str(x[title]['quantity']))

def borrow_book():
    title = input("Enter the title of the book you would like to borrow: ")
    x = load_books()
    if book_exists(title) == True:
        borrow_amount = int(input("How many copies of " + str(title) + " would you like to borrow? "))
        if int(x[title]['quantity']) == 0:
            print("There are no more copies of " + str(title) + " available.")
        elif int(x[title]['quantity']) >= borrow_amount:
            available_copies(title)
            x[title]['quantity'] = int(x[title]['quantity']) - borrow_amount
            save_books(x)
            print("Copies borrowed: " + str(borrow_amount))
            available_copies(title)
        else:
            print("The number of copies you want to borrow is not avaiable. The number of available copies is below. Please rent this number or less of your selected title")
            available_copies(title)
    else:
        print("The title you entered is not available in the library")

def return_book():
    title = input("Enter the title of the book you would like to return: ")
    x = load_books()
    if book_exists(title) == True:
        return_amount = int(input("How many copies of " + str(title) + " would you like to return? "))
        available_copies(title)
        x[title]['quantity'] = int(x[title]['quantity']) + return_amount
        save_books(x)
        print("Copies returned: " + str(return_amount))
        available_copies(title)
    else:
        print("The title you entered is not in our library records. You must have borrowed it from another library")

def add_attribute():
    title = input("Enter the title of the book you would like to add attributes for: ")
    attribute = input("What attribute would you like to add?")
    value = input("Enter the value you want to assign to this attribute: ")
    if book_exists(title) == True:
        x = load_books()
        x[title][attribute] = value
        save_books(x)
        print("\nThe book information is below: \n")
        get_book(title)
    else:
        print("The title you entered does not exist in the library")

def rate_book():
    title = input("Enter the title of the book you would like to rate: ")
    if book_exists(title) == True:
        new_rating = float(input("What is your rating of the book from 0-5,\n0 being the most negative rating and 5 being the most positive rating? "))
        if 0.0 <= new_rating <= 5.0:
            x = load_books()
            if "Number of Ratings" in x[title]:
                x[title]["Number of Ratings"] += 1
                x[title]["Sum of Ratings"] += new_rating
                save_books(x)
                x[title]["Average Rating"] = x[title]["Sum of Ratings"] / x[title]["Number of Ratings"]
            else:
                x[title]["Number of Ratings"] = 1
                x[title]["Sum of Ratings"] = new_rating
                save_books(x)
                x[title]["Average Rating"] = x[title]["Sum of Ratings"] / x[title]["Number of Ratings"]
            save_books(x)
            print("\nNumber of ratings: " + str(x[title]["Number of Ratings"]))
            print("Average Rating: " + str(x[title]["Average Rating"]))
        else:
            print("You entered an invalid rating. Please enter a rating in the range 0 to 5.")
    else:
        print("The title you entered does not exist in the library")

def rating():
    title = input("Enter the title of the book you would like to check the rating for: ")
    if book_exists(title) == True:
        x = load_books()
        if "Number of Ratings" in x[title]:
            print("\nNumber of ratings: " + str(x[title]["Number of Ratings"]))
            print("Average Rating: " + str(x[title]["Average Rating"]))
        else:
            print("There are no ratings for " + str(title) + " yet")
    else:
        print("The title you entered does not exist in the library")

def main():

    print("\nWelcome to Book Manager!\n")
    print("Use the actions below to access and edit the information in your JSON Library\n")
    print("1- Displays the data of all books in the library       8- Check the number of available copies of a title \n"
          "2- Displays the data of a specific title               9- Borrow books from the library\n"
          "3- Check if a certain title exists in the library      10- Return books to the library  \n"
          "4- Edit the quantity of a title                        11- Add a piece of data for a certain title \n"
          "5- Update any of the data for a certain title          12- Rate a book \n"
          "6- Remove a title from the library                     13- Check the rating of a book \n"
          "7- Add a title to the library                          14- Exit the program"
          )

    while True:

        action = int(input("\nEnter a number 1-14 to perform your desired function: "))

        if action == 14:
            break

        elif action == 1:
            display_all_books()

        elif action == 2:
            title = input("Type in the book's title to view its details: ")
            print('\n')
            get_book(title)

        elif action == 3:
            title = input("Enter a title to check if it exists in the library: ")
            print('\n')
            if book_exists(title) == True:
                print(str(title) + " DOES exist in the library")
            else:
                print(str(title) + " DOES NOT exist in the library")

        elif action == 4:
            update_quantity()

        elif action == 5:
            update_book()

        elif action == 6:
            remove_book()

        elif action == 7:
            add_book()

        elif action == 8:
            title = input("Enter the title of the book you would like to check the available copies for: ")
            available_copies(title)

        elif action == 9:
            borrow_book()

        elif action == 10:
            return_book()

        elif action == 11:
            add_attribute()

        elif action == 12:
            rate_book()

        elif action == 13:
            rating()

        else: #if not integer, if not 1-14
            print("You did not enter a valid command. Please refer to the action menu above and enter a number from 1-14.")

if __name__ == "__main__":
    main()
