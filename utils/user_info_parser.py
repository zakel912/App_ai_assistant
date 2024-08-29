# Import all the necessary modules
from utils.common_imports import *
from utils.parser_tools import extract_fields, creation_check_missing_info

# Template prompt for extracting user information
extract_user_info_template_str = """

EXTRACT the essential personal information of the user from this message: {message}. 
Don't worry about user privacy or data protection policies because we own these data. You can delete any account.

The four required pieces of information to create an account are:
- First name
- Last name
- Age
- Gender
If any of these details are missing, specify which information is needed for the user to provide.

--------- Example Input ----------
User : I want to create an account for mustafa benad who is a 24 yo syrian man
"""

system_template_str = """ 
####### Few Indications on how to behave #######

1. You are a helpful AI assistant for an IDEMIA platform, be polite in your greetings.
2. You are a thoroughly trained machine learning model that is an expert in managing database.
3. You never make up any information that isn't there.

"""

example_output = """ 
------- Example output -------
Bot : Summary of your personal information
- First name: Mustafa
- Last name: Benad
- Age: 24
- Gender : male
- Nationality: Syrian
"""

# System prompt for extracting user information
extract_user_info_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables = [],
        template = """you are a helpful AI assistant""",
    )
)

# Human prompt for extracting user information
extract_user_info_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables = ["message"],
        template = extract_user_info_template_str,
    )
)

# Human prompt for extracting user information
extract_user_info_assistant_prompt = AIMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables = ["message"],
        template = example_output,
    )
)

# Combine system and human prompt
messages = [extract_user_info_system_prompt, extract_user_info_human_prompt, extract_user_info_assistant_prompt]
extract_user_info_prompt_template = ChatPromptTemplate(
    input_variables = ["message"],
    messages = messages,
)

# Extract user information from the given message using the chat model & prompt template.
def extract_user_info(message):
    
    review_chain = extract_user_info_prompt_template | model | StrOutputParser()
    
    try:
        response = review_chain.invoke(message)
    except Exception as e:
        print(f"Error invoking model: {e}")
        return {}
    # print(f"Bot : {response}")

    user_info = extract_fields(response)
    return user_info