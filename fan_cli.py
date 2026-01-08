from superhero_api import SuperHeroAPIService

class FanPageCLI:
    def __init__(self):
        self.api = SuperHeroAPIService(
            token="0069654288f68ac1987d70aa116aa473"
        )

    def choose_universe(self):
        print("\nChoose Fan Universe")
        print("1. MARVEL")
        print("2. DC")

        choice = input("Enter choice: ")
        if choice == "1":
            return "Marvel Comics"
        elif choice == "2":
            return "DC Comics"
        else:
            print("Invalid choice.")
            return None

    def display_basic_info(self, hero):
        print("\nBASIC INFO")
        print(f"Name             : {hero['name']}")
        print(f"Full Name        : {hero['biography'].get('full-name', 'N/A')}")
        print(f"Publisher        : {hero['biography'].get('publisher', 'N/A')}")
        print(f"First Appearance : {hero['biography'].get('first-appearance', 'N/A')}")

    def display_power_stats(self, hero):
        print("\nPOWER STATS")
        powerstats = hero.get("powerstats", {})
        for stat, value in powerstats.items():
            print(f"{stat.capitalize():12}: {value}")
    
    def display_biography_info(self, hero):
        bio = hero.get("biography", {})
        print("\nBIOGRAPHY")
        print(f"Full Name     : {bio.get('full-name', 'N/A')}")
        print(f"Alter Egos    : {bio.get('alter-egos', 'N/A')}")
        print(f"Place of Birth: {bio.get('place-of-birth', 'N/A')}")
        print(f"Alignment     : {bio.get('alignment', 'N/A')}")
<<<<<<< HEAD
def display_power_class(self, hero):
    bio = hero.get("biography", {})
    name = hero.get("name", "").lower()
=======
    
    def display_threat_level(self, hero):
        stats = hero.get("powerstats", {})
        try:
            total = sum(int(v) for v in stats.values() if v.isdigit())
            print("\n[THREAT LEVEL]")
            if total > 400:
                print("Threat Level : EXTREME")
            elif total > 250:
                print("Threat Level : HIGH")
            else:
                print("Threat Level : MODERATE")
        except Exception:
            print("\n[THREAT LEVEL]\nThreat Level : UNKNOWN")
        
    def display_combat_profile(self, hero):
        stats = hero.get("powerstats", {})
        print("\n[COMBAT PROFILE]")
        print(f"Combat       : {stats.get('combat', 'N/A')}")
        print(f"Intelligence : {stats.get('intelligence', 'N/A')}")
        print(f"Strength     : {stats.get('strength', 'N/A')}")

>>>>>>> ee1e798eca7c8089ee64a6e0b094b4d05b056641

    print("\n[POWER CLASS]")
    if "alien" in bio.get("place-of-birth", "").lower():
        print("Class : Cosmic / Alien")
    elif "mutant" in bio.get("alter-egos", "").lower():
        print("Class : Mutant")
    elif "god" in name or "asgard" in bio.get("place-of-birth", "").lower():
        print("Class : Mystic / God")
    else:
        print("Class : Human / Tech-Based")
def run(self):
        universe = self.choose_universe()
        if not universe:
            return

        hero_name = input("\nEnter hero name: ")

        results = self.api.search(hero_name)
        filtered = self.api.filter_by_publisher(results, universe)

        if not filtered:
            print("\nNo matching hero found.")
            return

        hero = filtered[0]  # best match
        print(f"\n{hero['name']} — PROFILE")
        self.display_basic_info(hero)


if __name__ == "__main__":
    FanPageCLI().run()
