from models import *
from database import *

"""
# Create
new_user = User(name='John Doe', email='john.doe@example.com')
session.add(new_user)
session.commit()

# Read
user = session.query(User).filter_by(name='John Doe').first()
print(user.email)

# Update
user.email = 'new_email@example.com'
session.commit()

# Delete
session.delete(user)
session.commit()

# Once operations are complete, close the session.
session.close()

"""