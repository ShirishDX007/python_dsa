def student_func(id, name):
    return {"id": id, "name": name}

function_dict = {"student_func_key" : student_func}
function_dict["student_func_key"](1, "Alice")
print(function_dict)