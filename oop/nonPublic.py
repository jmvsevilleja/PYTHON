class Person:
    def __init__(self, first_name, email, age):
        self.first_name = first_name
        # protected properties
        self._protected_email = email
        self.__private_age = age

    def public_get_email(self):
        return self._protected_email

    def _protected_get_email(self):
        return self._protected_email

    def public_get_age(self):
        return self.__private_age

    def __private_set_age(self, age):
        self.__private_age = age

    def __private_get_age(self):
        return self.__private_age


# However, this doesn’t fully perform the functionality of the protected modifier.
me = Person('Jess', 'old@mail.com', 20)
print(me._protected_email)  # old@mail.com
me._protected_email = 'new@mail.com'
print(me._protected_email)  # new@email.com

print('public_get_email() - ', me.public_get_email())  # new@email.com
print('_protected_get_email() - ', me._protected_get_email())  # new@email.com

# print(me.__private_age)  # no attribute
me.__private_age = 30  # ignored?
print(me.public_get_age())  # 20
# print(me.__private_get_age())  # no attribute
# me.__private_set_age(30) # no attribute
me._Person__private_age = 40  # mangling on private attributes
print(me.public_get_age())  # 40
