from utils.db_agent_manager import db_agent_executor, memory

def get_ai_response(user_message):
    # Retrieve the chat history from the memory buffer
    chat_history = memory.buffer_as_messages
        
    # Prepare the inputs for the AI model, including the user's message and chat history
    inputs = {
        "message": user_message,
        "chat_history" : chat_history,
    }
    
    try:
        # Invoke the AI model using the provided inputs
        response = db_agent_executor.invoke(inputs)
        return (f"{response['output']}")
    except Exception as e:
        return (f"Sorry, I encountered an error: {e}")
        

if __name__ == "__main__":
    main()
