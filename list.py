import json

# Load the existing lists from files
try:
    with open('anime_list.json', 'r') as file:
        anime = json.load(file)
except FileNotFoundError:
    anime = []
except json.JSONDecodeError:
    print("Error reading anime_list.json. Starting with an empty list.")
    anime = []

try:
    with open('manhwa_list.json', 'r') as file:
        manhwa = json.load(file)
except FileNotFoundError:
    manhwa = []
except json.JSONDecodeError:
    print("Error reading manhwa_list.json. Starting with an empty list.")
    manhwa = []

print("-------------------- WELCOME TO MY ANIME AND MANHWA LIST --------------------")

while True:
    print()
    print("1. Anime")
    print("2. Manhwa")
    print("3. Exit")
    print()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print()
        choice2 = 0
        while choice2 != 5:
            print()
            print("1. Search for an anime: ")
            print("2. To show all the animes: ")
            print("3. Add a new anime: ")
            print("4. To go back to the main menu: ")
            print()
            try:
                choice2 = int(input("Enter your choice: "))
            except ValueError:
                print()
                print("Invalid input. Please enter a number.")
                print()
                continue
            print()
            
            try:   
                if choice2 == 1:
                    search_anime = input("Enter the name of the anime to search for: ").lower()
                    if search_anime in anime:
                        print()
                        print(f"{search_anime} is in the list.")
                        print()
                    else:
                        print()
                        print("Anime not found.")
                        print()
                
                elif choice2 == 2:
                    list_size = len(anime)
                    print()
                    print(f"Animes available: {list_size}")
                    print()
                    print("Anime list: ")
                    for i in range(len(anime)):
                        print(f"\t\t{i+1}. {anime[i]}")
                    print()
                    
                elif choice2 == 3:
                    new_anime = input("Enter the name of the new anime: ").lower()
                    anime.append(new_anime)
                    print()
                    print(f"{new_anime} has been added to the list.")
                    print()

                    # Save the updated anime list to the file
                    with open('anime_list.json', 'w') as file:
                        json.dump(anime, file)
                        
                elif choice2 == 4:
                    print()
                    print("Returning to the main menu...")
                    print()
                    break

                else:
                    print()
                    print("Invalid choice. Please try again.")
                    print()
                    continue

            except Exception as e:
                print(f"An error occurred: {e}")
                continue

    elif choice == 2:
        print()
        choice3 = 0
        while choice3 != 5:
            print("1. Search for a manhwa: ")
            print("2. To show all the manhwas: ")
            print("3. Add a new manhwa: ")
            print("4. To go back to the main menu: ")
            print()
            try:
                choice3 = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            print()
            
            try:
                if choice3 == 1:
                    search_manhwa = input("Enter the name of the manhwa to search for: ").lower()
                    if search_manhwa in manhwa:
                        print()
                        print(f"{search_manhwa} is in the list.")
                        print()
                    else:
                        print()
                        print(f"{search_manhwa} is not in the list.")
                
                elif choice3 == 2:
                    list_size = len(manhwa)
                    print(f"Manhwas available: {list_size}")
                    print()
                    print("Manhwa list: ")
                    for i in range(len(manhwa)):
                        print(f"\t\t{i+1}. {manhwa[i]}")
                    print()
                
                elif choice3 == 3:
                    new_manhwa = input("Enter the name of the new manhwa: ").lower()
                    manhwa.append(new_manhwa)
                    print()
                    print(f"{new_manhwa} has been added to the list.")
                    print()

                    # Save the updated manhwa list to the file
                    with open('manhwa_list.json', 'w') as file:
                        json.dump(manhwa, file)
                
                elif choice3 == 4:
                    print()
                    print("Returning to the main menu...")
                    print()
                    break

                else:
                    print("Invalid choice. Please try again.")
                    continue

            except Exception as e:
                print(f"An error occurred: {e}")
                continue

    elif choice == 3:
        exit_program = input("Do you want to exit the program? (yes/no): ").lower()
        if exit_program == "yes":
            print()
            print("Exiting the program...")
            print()
            break
    else:
        print()
        print("Invalid choice. Please try again.")
        print()
