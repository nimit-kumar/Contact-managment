class contact:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

    def display(self):
        print(f"Name:{self.name}")
        print(f"Phone:{self.phone}")
        print(f"email:{self.email}")
        print(f"address:{self.address}")
        
class contact_manager:
    def __init__(self):
        self.contact=[]
    def add_contact(self,contact):
        self.contact.append(contact)
        print("your contact added sucessfully")
    def view_contacts(self):
        if not self.contact:
            print("no contact available")
        else:
            for contact in self.contact:
                contact.display()
    def search_contact(self,search_term):
        found=False
        for contact in self.contact:
            if contact.name==search_term or contact.phone==search_term:
                contact.display()
                found = True
        if not found:
            print("contact not found")
    
    def update_contact(self,search_term):
        for contact in self.contact:
            if contact.name==search_term or contact.phone==search_term:
                print("enter new details")
                contact.name=input("New Name:")
                contact.phone=input("New phone:")
                contact.email=input("New Email:")
                contact.address=input("New Adress:")
                print("Contact is Updated")
                return
        print("contact not found")
    
    def delete_contact(self,search_term):
         for contact in self.contact:
          if contact.name==search_term or contact.phone==search_term:
             self.contact.remove(contact)
             print("contact deleted")
             return
         print("contact not found")
             

def main():
    manager = contact_manager()

    while True:
        print("\n==== Contact Management System ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = contact(name, phone, email, address)
            manager.add_contact(new_contact)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search = input("Enter Name or Phone to Search: ")
            manager.search_contact(search)

        elif choice == '4':
            search = input("Enter Name or Phone to Update: ")
            manager.update_contact(search)

        elif choice == '5':
            search = input("Enter Name or Phone to Delete: ")
            manager.delete_contact(search)

        elif choice == '6':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid Choice! Try again.")


          


