class Name:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        return None

call_name = Name("Shirish", "Dande")
print(f"Hello {call_name.name} {call_name.last_name}")
