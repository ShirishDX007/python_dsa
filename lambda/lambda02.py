#lambda parameters: expression
#lambda take one or more arguments but only on expression

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

formatter = lambda first_name, last_name: f"{first_name} {last_name}"
full_name = get_full_name(
        'Shirish',
        'Dande',
        formatter        
)
print(full_name)

