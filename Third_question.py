def snake_to_camel(text: str) -> str:
    words = text.split('_')
    camel_string = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_string

text = 'a_b_c_d'
print(snake_to_camel(text))
