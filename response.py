
def get_response(msg):
    
    ### Rule based response ###
    if "create" in msg:
        response = "Compte crée"
    elif "delete" in msg:
        response = "Compte supprimé"
    else:
        response = "Je n'ai pas compris"
    return (response)



def main():
    print("Bot: Hello! How can I assist you today?")
    
    while True:
        user_message = input("You: ").strip().lower()
        
        ### Rule based response ###
        if "create" in user_message:
            response = "Compte crée"
        elif "delete" in user_message:
            response = "Compte supprimé"
        else:
            response = "Je n'ai pas compris"
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
