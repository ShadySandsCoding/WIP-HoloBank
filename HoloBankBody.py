class Holobank:
    def __init__(self):
        self.char = {
            'Old Republic': {},
             'High Republic': {}, 
             "Clone Wars": {},
             "Galactic Empire": {} 
            }
        self.Vehicles = {"Clone Wars": {},
             "Galactic Empire": {} 
             }
        
        self.Cruisers = {"Clone Wars": {},
             "Galactic Empire": {} 
             }
        
        self.Factions = {'Old Republic': {},
             'High Republic': {}, 
             "Clone Wars": {},
             "Galactic Empire": {}
             }
        
    
    def add_character(self, era: str, faction: str, name: str, data: str):
        if era not in self.char:
            self.char[era] = {}
        if faction not in self.char[era]:
            self.char[era][faction] = {}     
        
        self.char[era] [faction] [name] = {
             "name": name,
             "era": era,
             "Faction": faction,
             'data': data
        }
        print(f"Added {name} In To The {era} HoloBank Records.. ")   

    def add_vehicle(self, era: str, faction: str, vehicle_name: str, data: str):
        if era not in self.Vehicles:
            self.Vehicles[era] = {}
        if faction not in self.Vehicles[era]:
            self.Vehicles[era][faction] = {}     
        
        self.Vehicles[era] [faction] [vehicle_name] = {
             "vehicle name": vehicle_name,
             "era": era,
             "Faction": faction,
             'data': data
        }  
        print(f"The Vehicle {vehicle_name} That Belongs To {faction} Has Been Added To The {era} In The HoloBank Records..")

    def add_cruiser(self, era: str, faction: str, cruiser_name: str, data: str): 
        if era not in self.Cruisers:
            self.Cruisers[era] = {}
        if faction not in self.Cruisers[era]:
            self.Cruisers[era][faction] = {}
             
        self.Cruisers[era] [faction] [cruiser_name] = {
             "vehicle name": cruiser_name,
             "era": era,
             "Faction": faction,
             'data': data
        }  
        print(f"The Vehicle {cruiser_name} That Belongs To {faction} Has Been Added To The {era} In The HoloBank Records..")  

    def add_faction(self, era: str, fact_name: str, data: str):
        if era not in self.Factions:
            self.Factions[era] = {}
        self.Factions[era] [fact_name] = {
            'faction name': fact_name,
            "era": era,
            "Information": data 
        }    
        print(f'The Faction {fact_name} Has Been Added To The HoloBank DataBase..')

if __name__ == "__main__":
    bank = Holobank()
    
    while True:
        print("\n" + "="*30)
        print("     HoloBank Data Entry   ")
        print("="*30)
      
        era = input("Era (or 'quit' to exit): ")
        if era.lower() == 'quit':
            break  

        category = input("Category (char/vehicle/cruiser/fact): ").lower().strip()

        if category == "char":
            faction = input("Faction: ")
            name = input("Character Name: ")
            data = input("Details: ")
            bank.add_character(era, faction, name, data)
        
        elif category == "vehicle":
            faction = input("Faction: ")
            name = input("Vehicle Name: ")
            data = input("Details: ")
            bank.add_vehicle(era, faction, name, data)

        elif category == "cruiser":
            faction = input("Faction: ")
            name = input("Cruiser Name: ")
            data = input("Details: ")
            bank.add_cruiser(era, faction, name, data)   

        elif category == "fact":
            name = input("Faction Name: ")
            data = input("Factions History: ")
            bank.add_faction(era,name, data)  

        else:
            print("Warning!!! Invalid Input! Try Another Input.")       




  
      
   