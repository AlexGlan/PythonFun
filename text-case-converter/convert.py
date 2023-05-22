import re

def convert():
    text = input("Enter your message: ")
    user_choice = input("Specify the desired case style(camelCase, snake_case, kebab-case, PascalCase): ")
    case = re.sub( r"\s+|[^a-z0-9]", "", user_choice.lower() )

    if case not in { "camelcase", "snakecase", "kebabcase", "pascalcase" }:
        print("Type not recognized, please try again.")

    if case == "snakecase":
        return re.sub( r"\s", "_", text.lower())
    
    elif case == "kebabcase":
        return re.sub( r"\s", "-", text.lower())
    
    elif case == "camelcase":
        modified_str = re.sub( r"\b\w", lambda w: w.group().upper(), text.lower() )
        modified_str = re.sub( r"^[^\s]", lambda match: match.group().lower(), modified_str )
        modified_str = re.sub( r"\s", "", modified_str)
        return modified_str
    
    elif case == "pascalcase":
        modified_str = re.sub( r"\b\w", lambda w: w.group().upper(), text.lower() )
        modified_str = re.sub( r"\s", "", modified_str)
        return modified_str

print(convert())