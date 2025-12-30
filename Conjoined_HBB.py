import json 

class Holobank:
    def __init__(self):
        # Initializing the data structures
        self.char = {
            'Old Republic': {},
            'High Republic': {}, 
            'Clone Wars': {},
            'Galactic Empire': {} 
        }
        self.Vehicles = {"Clone Wars": {}, "Galactic Empire": {}}
        self.Cruisers = {"Clone Wars": {}, "Galactic Empire": {}}
        self.Factions = {
            'Old Republic': {}, 'High Republic': {}, 
            'Clone Wars': {}, 'Galactic Empire': {}
        }
        self.era_list = ['Old Republic', 'High Republic', 'Clone Wars', 'Galactic Empire']

    def save_in_file(self, archiveName='holodisk_HB.json'):
        archive_data_disks = { 
            'Characters': self.char,
            'Vehicles': self.Vehicles,
            'Cruisers': self.Cruisers,
            'Factions': self.Factions
        }
        try:
            with open(archiveName, 'w') as f:
                json.dump(archive_data_disks, f, indent=4, sort_keys=True)
                print(f'\n[System] Data Has Been Uploaded To The {archiveName}..')
        except IOError as e:
            print(f'\n[Error] Could Not Access Holodisk!!: {e}')

    def load_from_file(self, archiveName='holodisk_HB.json'):
        try:
            with open(archiveName, 'r') as f:
                holodiskData = json.load(f)
                self.char = holodiskData.get('Characters', {})
                self.Vehicles = holodiskData.get('Vehicles', {})
                self.Cruisers = holodiskData.get('Cruisers', {})
                self.Factions = holodiskData.get('Factions', {})
            print(f'\n[System] Archives Loaded.. {archiveName} Is Now Online..')
        except FileNotFoundError:
            print('\n[System] No Holodisks Found.. Initializing Empty Database..')
        except json.JSONDecodeError:
            print('\n[Error] Holodisk Data Has Been Corrupted!!')

    def add_character(self, era: str, faction: str, name: str, data: str):
        if era not in self.era_list:
            print(f"Error!! {era} Is Not Stored In The HoloBank!!")    
            return 

        if era not in self.char:
            self.char[era] = {}
        if faction not in self.char[era]:
            self.char[era][faction] = {}     
        
        self.char[era][faction][name] = {
             "name": name,
             "era": era,
             "Faction": faction,
             'data': data
        }
        print(f"Added {name} In To The {era} HoloBank Records.. ")

    def add_vehicle(self, era: str, faction: str, vehicle_name: str, data: str):
        if era not in self.era_list:
            print(f"Error!! {era} Is Not Stored In The HoloBank!!")    
            return
        if era not in self.Vehicles:
            self.Vehicles[era] = {}
        if faction not in self.Vehicles[era]:
            self.Vehicles[era][faction] = {}
            
        self.Vehicles[era][faction][vehicle_name] = {
            "name": vehicle_name,
            "era": era,
            "Faction": faction,
            "data": data
        }
        print(f"Vehicle {vehicle_name} logged in {era} archives.")


    def add_cruiser(self, era: str, faction: str, ship_name: str, data: str):
        if era not in self.era_list:
            print(f"Error!! {era} is not a valid Era.")
            return
        if era not in self.Cruisers:
            self.Cruisers[era] = {}
        if faction not in self.Cruisers[era]:
            self.Cruisers[era][faction] = {}
            
        self.Cruisers[era][faction][ship_name] = {
            "name": ship_name,
            "era": era,
            "Faction": faction,
            "data": data
        }
        print(f"Cruiser {ship_name} added to the {era} registry.")


    def delete_entry(self, category: str, era: str, faction: str, name: str):
        
        mapping = {
            'char': self.char,
            'vehicle': self.Vehicles,
            'cruiser': self.Cruisers
        }
        
        target_dict = mapping.get(category.lower())
        try:
            del target_dict[era][faction][name]
            print(f"Successfully purged {name} from the records.")
        except KeyError:
            print("Error: Could not find that entry to delete.")

              

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
        
        else:
            print("Invalid transmission. Try again.")