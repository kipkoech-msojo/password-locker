
class User:
    """
    class to create new user
    """
    user_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password
        """
        defined an init method to initialize the user attributes
        """



    def save_user_details(self):
        User.user_list.append(self)
        """
        method to save user details in the list
        """

    def delete_user_details(self):
        '''
        method to delete user details
        '''
        User.user_list.remove(self)

    @classmethod
    def display_user_details(cls):
        return cls.user_list


class Credentials:
    """
    created credentials class
    """

    credentials_list = []

    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password
        """
        method to initialize user credential details
        """

    def save_credentials(self):
        """
        method to save user credentials to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        method to delete credentials from the credentials list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def show_credentials(cls):
        """
        method to display user credentials in the list
        """
        return cls.credentials_list

    @classmethod
    def find_credential(cls, account):
        """
        Method to find the user credentials
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential


    

    

    