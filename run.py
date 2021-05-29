from user import User,Credentials
def create_new_user(username,password):
    """
    function that creates a user using a password and username
    """
    new_user = User(username,password) 
    return new_user

def save_user(user):
    """
    function that saves a new user
    """
    user.save_user()

def display_user(user):
    """
    function that displays user
    """
    return User.display_user()

def login_user(password,username):
    """
    a function that checks if the users already exist 
    """
    checked_user = Credentials.verify_user(password,username)
    return checked_user

def create_new_credential(account,username,password):
    """
    function that create new credential details for a new user
    """
    new_credential = Credentials(account,username,password)
    return new_credential