import json
import os

def save_in_file(self, archiveName= 'holodisk_HB.json'):
    #bundles dicts into a JSON object and saves it
    archive_data_disks = { 
      'Characters': self.char,
      'Vehicles': self.Vehicles,
      'Cruisers': self.Cruisers,
      'Factions': self.Factions
    }
    try:
        with open(archiveName, 'w') as f:
            
            
            json.dump(archive_data_disks, f, indent=4, sort_keys= True)
            print(f'\n[System] Data Has Been Uploaded To The {archiveName}..')
    except IOError as e:
        print(f'\n [Error] Could Not Access Holodisk!!: {e}')

def load_from_file(self, archiveName= 'holodisk_HB.json'):
    try:
        with open(archiveName, 'r') as f:
            holodiskData = json.load(f)
            #using the .get function so i can "grab" my data without thowing KeyError

            self.char = holodiskData.get('Characters', {})
            self.Vehicles = holodiskData.get('Vehicles', {})
            self.Cruisers = holodiskData.get('Cruisers', {})
            self.Factions = holodiskData.get('Factions', {})
        print(f'\n[SYstem] Archives Loaded.. {archiveName} Is Now Online..')
    except FileNotFoundError:
        print('\n[System] No Holodisks Found.. Initializing Empty Database..')
    except json.JSONDecodeError:
        print('\n[Error] Holodisk Data Has Been Corrupted!!')


if __name__ == '__main__':
    bank = Holobank()
    bank.load_from_file()

    while True:
        print('\n' + '-'*35)
        print('    HOLONET DATA ADMINISTRATION')
        print('-'*35)
        print(' 1. Add Entry')
        print(' 2. Update Entry')
        print(' 3. Delete Entry') 
        print(' 4. Search Records')  
        print(' 5. Quit And Save')

        choice = input('\nSelect A Choice (1-5): ').strip()

        if choice == '5':
            bank.save_in_file()
            print("\nThe Holodisk Data Has Been Saved, May The Force Be With You..")
            break
        print(f'\nAvailable Eras: {','.join(bank.era_list)}')
        era = input('Enter The Era: ').strip()

        if choice == '1':
            category =  input('Category (char/vehicle/cruiser/fact): ').lower().strip()
            faction = input('Faction: ').strip()
              
            if choice == 'char':
                name = input("Character Name: ")
                data = input("Bio Entry: ")
                bank.add_character(era, faction, name, data)   
            elif category== 'vehicle':
                name = input('Vehicle Name: ')
                data = input('Technical Specifications: ')
            elif category == 'cruisers':
                name = input('Cruiser Name/Class: ')
                data = input('Vessel History: ')
                bank.add_cruiser(era, faction, name, data)     
            elif category == 'fact':
                data = input('Faction Data/History: ')
                bank.add_faction(era, faction, data)
        
        elif choice == '2':
            category = input("Category to update (char/vehicle/cruiser): ").lower().strip()
            faction = input("Faction: ").strip()
            name = input("Name of entry to update: ").strip()
            new_data = input("Enter the new updated details: ")

            if category == "char":
                bank.update_char_details(era, faction, name, new_data)
            elif category == "vehicle":
                bank.update_Vehicles_details(era, faction, name, new_data)
            elif category == "cruiser":
                bank.update_Cruisers_details(era, faction, name, new_data)
        elif choice == '3':
            category = input("Category to delete (char/vehicle/cruiser): ").lower().strip()
            faction = input("Faction: ").strip()
            name = input("Name of entry to delete: ").strip()
            
            confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()
            if confirm == 'y':
                if category == "char":
                    bank.delete_char(era, faction, name)
                elif category == "vehicle":
                    bank.delete_vehicle(era, faction, name)
                elif category == "cruiser":
                    bank.delete_Cruisers(era, faction, name) 

        elif choice == '4':
            category = input("Search in (char/vehicle/cruiser): ").lower().strip()
            target_name = input("Enter Name to Search: ")

            source = {"char": bank.char, 'vehicle': bank.Vehicles, 'cruiser': bank.Cruisers}.get(category)

            found = False
            if source and era in source: 
                for faction, names in source[era].items():
                    if target_name in names:
                        print(f'\n[FOUND] {target_name}') 
                        print(f'faction: {faction}')
                        print(f'Data: {names[target_name]['data']}')
                        found = True
            if not found:
                print(f"\n[!] No Records Found For '{target_name}' In {era}")  

                        







