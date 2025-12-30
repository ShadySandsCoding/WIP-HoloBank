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
            'characters': self.char,
            'vehicle': self.Vehicles,
            'cruiser': self.Cruisers
        }
        
        target_dict = mapping.get(category.lower())
        try:
            del target_dict[era][faction][name]
            print(f"Successfully purged {name} from the records.")
        except KeyError:
            print("Error: Could not find that entry to delete.")


    def search_records(self, category: str, name: str):
        
        mapping = {
            'char': self.char,
            'vehicle': self.Vehicles,
            'cruiser': self.Cruisers
        }
        
        target_dict = mapping.get(category.lower())
        if not target_dict:
            print("Invalid category. Use: char, vehicle, or cruiser.")
            return

       
        found = False
        for era in target_dict:
            for faction in target_dict[era]:
                if name in target_dict[era][faction]:
                    record = target_dict[era][faction][name]
                    print("\n" + "—"*20)
                    print(f"NAME:    {record['name']}")
                    print(f"ERA:     {record['era']}")
                    print(f"FACTION: {record['Faction']}")
                    print(f"DATA:    {record['data']}")
                    print("—"*20)
                    found = True
        
        if not found:
            print(f"\n[System] No record found for '{name}' in {category}.")        