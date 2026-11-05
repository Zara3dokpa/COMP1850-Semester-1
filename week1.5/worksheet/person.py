# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
            Creates a Person, given values for name and birth.
            """
        if (not isinstance(name,str)) or (not isinstance(birth,date)):
            raise TypeError
        if name=="":
            raise ValueError
        self.name=name
        self.birth=birth

    def initials(self):
        """ Returns initials """
        return "".join(part[0].upper()for part in self.name.split())
        

    def is_birthday(self):
        """ Returns True if the person's birthday is today, otherwise returns False """
        today=date.today()
        return self.birth.month==today.month and self.birth.day==today.day
         
        
    



        
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
