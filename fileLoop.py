from Holobank_engine import Holobank


if __name__ == '__main__':
    bank = Holobank()

    bank.load_from_file()

    while True:
        print("\n" + "="*30)
        print("  HOLONET ADMINISTRATION")
        print("="*30)
        print("1. Add Character")
        print("2. Add Vehicle")
        print("3. Add Cruiser")
        print("4. Delete Entry")
        print("5. Save and Exit")
        print("6. Search Records")
        
        choice = input("\nSelect Option: ")

        if choice == '1':
            era = input("Enter Era (e.g., Clone Wars): ")
            fact = input("Enter Faction: ")
            name = input("Enter Name: ")
            bio = input("Enter Data/Bio: ")
            bank.add_character(era, fact, name, bio)

        elif choice == '2':
            era = input("Enter Era: ")
            fact = input("Enter Faction: ")
            v_name = input("Enter Vehicle Name: ")
            v_data = input("Enter Vehicle Data: ")
            bank.add_vehicle(era, fact, v_name, v_data)
       
        
        elif choice == '3':
            era = input("Enter Era: ")
            fact = input("Enter Faction: ")
            c_name = input("Enter Cruiser Name: ")
            c_data = input("Enter Cruiser Bio/Specs: ")
            bank.add_cruiser(era, fact, c_name, c_data)

        elif choice == '4':
            print("\nCategories: char, vehicle, cruiser")
            cat = input("Enter category: ")
            era = input("Enter era: ")
            fact = input("Enter faction: ")
            name = input("Enter name to delete: ")
            bank.delete_entry(cat, era, fact, name)    

        elif choice == '5':
            bank.save_in_file() 
            print("\n[System] Archives secured. Shutting down...")
            break

        elif choice == '6':
            print("\nSearch Categories: char, vehicle, cruiser")
            cat = input("Enter category: ")
            target_name = input("Enter name to search for: ")
            bank.search_records(cat, target_name)
        
        else:
            print("Invalid transmission. Try again.")