# Generate a response based on simple keyword matching rules.
def get_response(msg):
    
    if "create" in msg:
        response = "Compte crée"
    elif "delete" in msg:
        response = "Compte supprimé"
    else:
        response = "Je n'ai pas compris"
    return (response)
