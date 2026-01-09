class Artist:
    def __init__(self, name, email, rights):
        self.name = name
        self.__email = email  # Private attribute
        self.__rights = rights  # Private attribute

    def get_email(self):
        return self.__email

    def get_rights(self):
        return self.__rights

    def update_rights(self, new_rights):
        self.__rights = new_rights

class Producer:
    def __init__(self, name, contact_info):
        self.name = name
        self.__contact_info = contact_info  # Private attribute

    def get_contact_info(self):
        return self.__contact_info

def protect_sensitive_info(artist, producer):
    return {
        "artist_name": artist.name,
        "producer_name": producer.name,
        "artist_rights": artist.get_rights(),
        "producer_contact": producer.get_contact_info()
    }

# Example usage
artist = Artist("John Doe", "john@example.com", ["Copyright", "Distribution"])
producer = Producer("Jane Smith", "jane@example.com")

sensitive_info = protect_sensitive_info(artist, producer)
print(sensitive_info)
