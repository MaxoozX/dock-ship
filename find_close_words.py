import main

if __name__ == "__main__":
    while True:
        user_input = input("Enter the word of which you want related words : ")
        print("\n")
        if user_input in main.adjancency_list.keys():
            print("The word has been found, here are the close words :")
            print(*main.adjancency_list[user_input], sep=", ")
        else:
            print(f"Couldn't find the word {user_input} in the words list.")
        
        print("\n\n")