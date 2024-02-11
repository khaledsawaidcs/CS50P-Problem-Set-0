def convert(input_string: str) -> str:
    smile = ":)"
    sad = ":("
    string_with_emoji = input_string
    if smile in input_string:
        string_with_emoji = string_with_emoji.replace(smile, "\U0001F600")
    if sad in input_string:
        string_with_emoji = string_with_emoji.replace(sad, "\U0001F614")
    return string_with_emoji
