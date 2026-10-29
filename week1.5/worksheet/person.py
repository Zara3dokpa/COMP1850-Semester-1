# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        if (not isinstance(name,str)) or (not isinstance(birth,date)):
            raise TypeError
        if name=="":
            raise ValueError
        self.name=name
        self.birth=birth

    def initials(self):
        return "".join(part[0].upper()for part in self.name.split())
        """ Returns intitials """

    def is_birthday(self):
        if self.birth==date.today():
            return True
        else:
            return False
        """ Returns True if the person's birthday is today, otherwise returns False """
    



        
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
