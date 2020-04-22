import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')

import django
django.setup()


#FAKE pop JavaScript


from apptwo.models import User
from faker import Faker
fakegen = Faker()

def add_dummy_data(n=5):
    for entry in range(n):
        #create fake data for the entry
        fake_firstname = fakegen.first_name()
        print(fake_firstname)
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        #add user entry
        try:
            user = User.objects.get_or_create(Firstname=fake_firstname, Lastname=fake_lastname, Email= fake_email)[0]
            user.save()
        except Exception as e:
            raise e



if __name__ == '__main__':
    print('populating script!')
    add_dummy_data(5)
    print('populating complete!')
