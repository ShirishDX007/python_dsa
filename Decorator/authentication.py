
class User:
    def __init__(self, authenticated = False):
        self.authenticated = authenticated

def require_authentication(func):

    def wrapper(User, *args, **kwargs):
        if User.authenticated:
            return func(*args, **kwargs)
        else:
            raise PermissionError("User is not authenticated.")
    return wrapper

class SecureResource():
    @require_authentication
    def user_logging(self, user):
        return "user Logged in secuerly."

user = User(authenticated=True)
resource = SecureResource()
print(resource.user_logging(user))
