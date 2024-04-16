class Art:
    def __init__(self, art_id, painter, style, price, address, email, phone, name=None, size=None, material=None):
        self.art_id = art_id
        self.painter = painter
        self.style = style
        self.price = price
        self.address = address
        self.email = email
        self.phone = phone
        self.name = name
        self.size = size
        self.material = material

    def display_info(self):
        print(
            f"Art ID: {self.art_id}, Painter: {self.painter}, Style: {self.style}, Price: {self.price}, Address: {self.address}, Email: {self.email}, Phone Number: {self.phone}")
        if self.name:
            print(f"Name: {self.name}")
        if self.size:
            print(f"Size: {self.size}")
        if self.material:
            print(f"Material: {self.material}")


class Exhibition(Art):
    def __init__(self, art_id, painter, style, price, address, email, phone, name, date, title, curator, description):
        super().__init__(art_id, painter, style, price, address, email, phone, curator, description)
        self.size = None
        self.paintings_name = name
        self.exhibition_date = date
        self.exhibition_title = title
        self.curator = curator
        self.description = description

    def display_info(self):
        super().display_info()
        print(f"Paintings Name: {self.paintings_name}")
        print(f"Exhibition Date: {self.exhibition_date}")
        print(f"Exhibition Title: {self.exhibition_title}")
        print(f"Curator: {self.curator}")
        print(f"Description: {self.description}")


class Payment:
    @staticmethod
    def process_payment(amount, payment_method):
        # Placeholder function to simulate payment processing
        if payment_method == "credit_card":
            # Simulate credit card payment processing
            print(f"Processing credit_card payment for ${amount}")
            return True
        elif payment_method == "paypal":
            # Simulate PayPal payment processing
            print(f"Processing payPal payment for ${amount}")
            return True
        else:
            print("Invalid payment method")
            return False


class Customer:
    def __init__(self, id_number, first_name, last_name, age, address, phone, email, payments=None):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.payments = payments if payments is not None else []


    def display_info(self):
        print(f"ID Number: {self.id_number}, First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}, Address: {self.address}, Phone Number: {self.phone}, Email: {self.email}")
        if self.payments:
            print("Payment History:")
            for payment in self.payments:
                print(f"Art Id:{payment['art_id']}, Amount: {payment['amount']}, Payment Method: {payment['method']}, Payment Date: {payment['date']}")

    def make_payment(self, amount, payment_method, payment_date, art_id):
        payment_processor = Payment()
        if payment_processor.process_payment(amount, payment_method):
            self.payments.append({'art_id': art_id, 'amount': amount, 'method': payment_method, 'date': payment_date})
            print("Payment successful!")
        else:
            print("Payment failed. Please try again.")


class ArtCollection:
    def __init__(self):
        self.artworks = []
        self.customers = []
        self.exhibitions = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def remove_artwork(self, art_id):
        for artwork in self.artworks:
            if artwork.art_id == art_id:
                self.artworks.remove(artwork)
                print(f"Artwork with ID {art_id} removed successfully.")
                return
        print(f"Artwork with ID {art_id} not found.")

    def search_artwork_by_id(self, art_id):
        for artwork in self.artworks:
            if artwork.art_id == art_id:
                artwork.display_info()
                return
        print(f"Artwork with ID {art_id} not found.")

    def print_all_artworks(self):
        print("All Artworks:")
        for artwork in self.artworks:
            artwork.display_info()
            print()  # Add an empty line between artworks

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, id_number):
        for customer in self.customers:
            if customer.id_number == id_number:
                self.customers.remove(customer)
                print(f"Customer with ID Number {id_number} removed successfully.")
                return
        print(f"Customer with ID Number {id_number} not found.")

    def search_customer_by_first_name(self, first_name):
        first_name = first_name.capitalize()  # Normalize input to match stored format
        found_customers = [customer for customer in self.customers if customer.first_name == first_name]
        if found_customers:
            print(f"Customers with First Name {first_name}:")
            for customer in found_customers:
                customer.display_info()
        else:
            print(f"No customers found with First Name {first_name}.")

    def search_customer_by_last_name(self, last_name):
        last_name = last_name.capitalize()  # Normalize input to match stored format
        found_customers = [customer for customer in self.customers if customer.last_name == last_name]
        if found_customers:
            print(f"Customers with Last Name {last_name}:")
            for customer in found_customers:
                customer.display_info()
        else:
            print(f"No customers found with Last Name {last_name}.")

    def print_all_customers(self):
        print("All Customers:")
        for customer in self.customers:
            customer.display_info()
            print()  # Add an empty line between customers

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def remove_exhibition_by_id(self, exhibition_id):
        self.exhibitions = [exhibition for exhibition in self.exhibitions if exhibition.art_id != exhibition_id]

    def search_exhibition_by_id(self, exhibition_id):
        return [exhibition for exhibition in self.exhibitions if exhibition.art_id == exhibition_id]

    def print_all_exhibitions(self):
        print("All Exhibitions:")
        for exhibition in self.exhibitions:
            exhibition.display_info()
            print()


def main():
    global art_id
    collection = ArtCollection()

    while True:
        print("Commands:")
        print("0 - Exit")
        print("1 - Add painting info")
        print("2 - Search painting info by ID")
        print("3 - Remove painting info by ID")
        print("4 - Print all painting info")
        print("5 - Add customer info")
        print("6 - Remove customer info by ID")
        print("7 - Search customer info by First Name")
        print("8 - Search customer info by Last Name")
        print("9 - Print all customer info")
        print("10 - Add exhibition info")
        print("11 - Remove exhibition info by ID")
        print("12 - Search exhibition info by ID")
        print("13 - Print all exhibition info")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            while True:
                art_id = input("Enter painting ID: ")
                if art_id.isnumeric():
                    break
                else:
                    print("Invalid input. Please enter only numeric characters.")

            while True:
                painter = input("Enter painter's full name: ")
                if painter.isalpha() or " " in painter:
                    break
                else:
                    print("Invalid input. Please enter only alphabetic characters.")

            while True:
                style = input("Enter painter style: ")
                if style.isalpha():
                    break
                else:
                    print("Invalid input. Please enter only alphabetic characters.")

            while True:
                price = input("Enter painting price: ")
                if ' $' in price or ' €' in price:
                    break
                else:
                    print("Invalid input. Please include either '$' or '€' in the price.")

            while True:
                size = input("Enter painting's size: ")
                if 'cm' in size or 'm' in size:
                    break
                else:
                    print("Invalid input. Please include either 'cm' or 'm' in the size.")

            address = input("Enter painting address: ")
            phone = input("Enter painter's Phone Number: ")  # Accept input as string
            try:
                phone = int(phone)  # Convert input to integer
            except ValueError:
                print("Invalid phone number format. Please enter a valid integer.")
                continue  # Skip adding artwork if phone number format is invalid
            while True:
                email = input("Enter painter's Email Address: ")
                if "@" in email:
                    break
                else:
                    print("Invalid email format. Please include the '@' symbol.")
            name = input("Enter painting name: ")
            material = input("enter maretial of painting used:")
            artwork = Art(art_id, painter, style, price, address, email, phone, name, size, material)
            collection.add_artwork(artwork)
            print("Painting info added successfully.")
        elif choice == "2":
            art_id = input("Enter painting ID to search: ")
            collection.search_artwork_by_id(art_id)
        elif choice == "3":
            art_id = input("Enter painting ID to remove: ")
            collection.remove_artwork(art_id)
        elif choice == "4":
            collection.print_all_artworks()
        elif choice == "5":
            while True:
                id_number = input("Enter customer ID Number (format: number-letter): ")
                if id_number[:-2].isnumeric() and id_number[-1].isalpha() and len(id_number) > 1:
                    break
                else:
                    print("Invalid input. Please enter the ID Number in the format 'number-letter'.")

            while True:
                first_name = input("Enter customer's First Name: ")
                if first_name.isalpha():
                    first_name.capitalize()
                    break
                else:
                    print("Invalid input. Please enter only alphabetic characters with first capital letter.")

            while True:
                last_name = input("Enter customer's Last Name: ")
                if last_name.isalpha():
                    last_name.capitalize()
                    break
                else:
                    print("Invalid input. Please enter only alphabetic characters with first capital letter.")

            while True:
                age = input("Enter customer's Age: ")
                if age.isnumeric():
                    break
                else:
                    print("Invalid input. Please enter only numeric characters.")

            address = input("Enter customer's Address: ")
            while True:
                phone = input("Enter customer's Phone Number: ")
                if phone.startswith('+') or phone.startswith('00'):
                    if phone[1:].isdigit():  # Check if the rest of the string is composed of digits
                        break
                    else:
                        print("Invalid input. Phone number should contain only digits the country code and after it.")
                else:
                    print("Invalid input. Phone number should start with '+' or '00' for international format.")

            # Validate gallery email address (email format)
            while True:
                email = input("Enter Gallery's Email Address: ")
                if '@' in email and '.' in email:
                    break
                else:
                    print("Invalid email format. Please include the '@' symbol and a '.'.")

            customer = Customer(id_number, first_name, last_name, age, address, phone, email)
            collection.add_customer(customer)
            # Prompt for payment
            if customer:
                while True:
                    amount = input("Enter the payment amount: ")
                    if ' $' in amount or ' €' in amount:
                        break
                    else:
                        print("Invalid input. Please include either '$' or '€' in the amount.")


                while True:
                    payment_method = input("Select payment method (credit_card/Paypal): ")
                    if payment_method == "credit_card" or payment_method == "paypal":
                        break
                    else:
                        print("Invalid payment method. Please enter 'Credit Card' or 'Paypal' with the first letters capitalized.")


                while True:
                    payment_date = input("Enter the payment date (DD.MM.YYYY): ")
                    date_parts = payment_date.split('.')
                    if len(date_parts) == 3 and all(part.isdigit() for part in date_parts):
                        day, month, year = map(int, date_parts)
                        if 1 <= day <= 31 and 1 <= month <= 12:
                            break
                        else:
                            print("Invalid date format. Please enter a valid date.")
                    else:
                        print("Invalid date format. Please enter the date in the format DD.MM.YYYY.")

                while True:
                    art_id = input("Enter painting ID: ")
                    if art_id.isnumeric():
                        break
                    else:
                        print("Invalid input. Please enter only numeric characters.")

                customer.make_payment(amount, payment_method, payment_date, art_id)
            else:
                print("Please add customer info before making a payment.")
            print("Customer info added successfully.")


        elif choice == "6":
            id_number = input("Enter customer ID Number to remove: ")
            collection.remove_customer(id_number)
        elif choice == "7":
            first_name = input("Enter customer's First Name to search: ")
            collection.search_customer_by_first_name(first_name)
        elif choice == "8":
            last_name = input("Enter customer's Last Name to search: ")
            collection.search_customer_by_last_name(last_name)
        elif choice == "9":
            collection.print_all_customers()

        elif choice == "10":
            # Validate exhibition ID (starts with 'EX' followed by numbers)
            while True:
                art_id = input("Enter exhibition ID: ")
                if art_id.startswith('EX') and art_id[2:].isdigit():
                    break
                else:
                    print("Invalid exhibition ID format. Please start with 'EX' followed by numeric characters.")

            # Validate exhibition title (alphabetic)
            while True:
                title = input("Enter exhibition title: ")
                if title and title[0].isalpha() and title[0].isupper():
                    break
                else:
                    print("Invalid title. Please enter a title starting with a capital letter.")


            while True:
                painter = input("Enter painter's full name: ")
                if ' ' in painter:
                    first_name, last_name = painter.split(' ', 1)
                    if first_name.isalpha() and last_name.isalpha() and first_name[0].isupper() and last_name[
                        0].isupper():
                        break
                    else:
                        print(
                            "Invalid painter's name format. Enter first name & last name, each starting with a capital.")
                else:
                    print(
                        "Invalid painter's name format. Enter both first name and last name separated by a space.")

            # Validate painting styles (alphabetic)
            while True:
                style = input("Enter painting styles: ")
                if style.isalpha() or ' ' in style:
                    break
                else:
                    print("Invalid painting style. Please enter only alphabetic characters.")

            while True:
                price = input("Enter painting prices: ")
                if any(char.isdigit() or char in ['$', '€'] for char in price):
                    break
                else:
                    print("Invalid price format. Please include numeric characters with symbols ($, €).")

            # Validate gallery address (alphanumeric with symbols)
            while True:
                address = input("Enter Gallery address: ")
                if address.isalnum() or any(char in [' ', ',', '.', '-'] for char in address):
                    break
                else:
                    print("Invalid address format. Please enter alphanumeric characters with symbols.")

            # Validate gallery phone number (starts with '+' or '00' and numeric)
            while True:
                phone = input("Enter Gallery's Phone Number: ")
                if phone.startswith(('+', '00')) and phone[1:].isdigit():
                    break
                else:
                    print("Invalid phone number format. Please start with '+' or '00' followed by numeric characters.")

            # Validate gallery email address (email format)
            while True:
                email = input("Enter Gallery's Email Address: ")
                if '@' in email and '.' in email:
                    break
                else:
                    print("Invalid email format. Please include the '@' symbol and a '.'.")


            # Validate painting names (optional, alphabetic)
            name = input("Enter painting names (optional): ")
            if name and not name.isalpha() or ', ' in name:
                print("Invalid painting name. Please enter only alphabetic characters.")

            # Validate exhibition date (duration format dd.mm.yyyy - dd.mm.yyyy)
            while True:
                date = input("Enter exhibition date (dd.mm.yyyy - dd.mm.yyyy): ")
                date_parts = date.split(' - ')

                if len(date_parts) == 2:
                    start_date, end_date = date_parts
                    start_parts = start_date.split('.')
                    end_parts = end_date.split('.')

                    if (len(start_parts) == 3 and len(end_parts) == 3 and
                            all(part.isdigit() for part in start_parts) and all(part.isdigit() for part in end_parts)):

                        start_day, start_month, start_year = map(int, start_parts)
                        end_day, end_month, end_year = map(int, end_parts)

                        if (1 <= start_day <= 31 and 1 <= start_month <= 12 and
                                1 <= end_day <= 31 and 1 <= end_month <= 12 and
                                start_year <= end_year and
                                (start_year < end_year or (start_year == end_year and (start_month < end_month or (
                                        start_month == end_month and start_day <= end_day))))):
                            break
                        else:
                            print(
                                "Invalid date format or range. Please enter a valid date range in the format dd.mm.yyyy - dd.mm.yyyy.")
                    else:
                        print(
                            "Invalid date format or range. Please enter a valid date range in the format dd.mm.yyyy - dd.mm.yyyy.")
                else:
                    print(
                        "Invalid date format or range. Please enter a valid date range in the format dd.mm.yyyy - dd.mm.yyyy.")


            # Validate exhibition curator name (alphabetic)
            while True:
                curator = input("Enter exhibition Curator Name: ")
                if curator.isalpha() or ' ' in curator:
                    break
                else:
                    print("Invalid curator name. Please enter only alphabetic characters.")

            description = input("Enter exhibition description: ")

            exhibition = Exhibition(art_id, painter, style, price, address, email, phone, name, date, title, curator,
                                    description)

            collection.add_exhibition(exhibition)
            print("Exhibition info added successfully.")


        elif choice == "11":
            exhibition_id = input("Enter exhibition ID to remove: ")
            collection.remove_exhibition_by_id(exhibition_id)
            print(f'the Exhibition with ID {exhibition_id} successfully removed')

        elif choice == "12":
            exhibition_id = input("Enter exhibition ID to search: ")
            found_exhibitions = collection.search_exhibition_by_id(exhibition_id)
            if found_exhibitions:
                print("Exhibition(s) found:")
                for exhibition in found_exhibitions:
                    exhibition.display_info()
            else:
                print(f"No exhibition found with ID {exhibition_id}.")
        elif choice == "13":
            collection.print_all_exhibitions()
        else:
            print("Invalid choice. Please enter a valid command.")


if __name__ == "__main__":
    main()
