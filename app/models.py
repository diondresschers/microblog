from app import db
from datetime import datetime # This is for a time stamp

# If you want to reflect the changes in the database scheme run `(vv) $ flask db init` # this will create a new `migrations`-folder
# With `(v) $ flask db` you will see all the options for the `flask db`, so also the `flask db init`-command
# so, `flask db init`, 'flask db migrate`, flask db upgrade` # The `upgrade is a method in the versions-file in the `app/migrations/versions` directory.
# Het kan handig zijn om  de database te bekijken met de SQLite Browser [Downloads - DB Browser for SQLite](https://sqlitebrowser.org/dl/)
# SQLite users 'Snake Case" naming convention for databases, so the name `AddressAndPhone` will be used in the Model Class and the table name would be `address_and_phone`. If you want to change this you can add the attribute `__tablename__` to the model class.
# Instead of `flask db migrate`, you can also give an addional comment by using `flask db migrate -m "added posts"`




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic') # `Post` is the post database table. # P.44, this is actually not a field, but called "The one within", if you refert to this user as u, than `u.posts` will show all the posts of this user. # P.45 The `lazy` argument defineshow the database query for the relationship will be issued. # The `backref` argument defines the name of a field that will be added to the objects of the “many” class that points back at the “one” object

    def __repr__(self):
        return'<User {}>'.format(self.username) # return f.'User {self.username}>' # Using an f-string in stead of # return 'return'<User {}>'.format(self.username)"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) # This will be indexed. # `datetime.utcnow`, will Pass the function itself and not the result of this, otherwise this would be `datetime.utcnow()`. # P.44 This `db.relationship`, reflects one-to-many.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # This is a foreign key, form the table `user`, and the database fieldname is `id`. 
    
    def __repr__(self):
        return f"<Post {self.body}"

# If you want to communicate with the database via the Python command:

# >>> from app import db
# >>> from app.models import User, Post
# >>> u = User(username='Dion', email='dion@example.com')
# >>> db.session.add(u)
# >>> db.session.commit() 
# >>> # A db.session.rollback() will abort the session and remove any changes stored in the dabase, but then again apply a `db.session.commit()`

# >>> users = User.query.all()
# >>> users
# [<User Dion>, <User Jadzia>]
# >>> for u in users:
# ...     print(u.id, u.username)
# ... 
# 1 Dion
# 2 Jadzia

# >>> u = User.query.get(1)
# >>> u
# <User Dion>
# >>> u = User.query.get(2)
# >>> u
# <User Jadzia>
# >>> u.email
# 'jadzia@example.com'
# >>> u.id
# 2

# >>> u = User.query.get(1)
# >>> p = Post(body="My first post!", author=u)
# >>> db.session.add(p)
# >>> db.session.commit()

# >>> # Get all posts written by a user
# ... u = User.query.get(1)
# >>> u
# <User Dion>
# >>> posts = u.posts.all()
# >>> posts
# [<Post My first post!]
# >>> 
# >>> u = User.query.get(2)
# >>> u
# <User Jadzia>
# >>> u.posts.all()
# []
# >>> 
# >>> # Print post per author and body for all posts
# ... psots = Post.query.all()
# >>> for p in posts:
# ...     print(p.id, p.author.username, p.body)
# ... 
# 1 Dion My first post!
# >>> 
# >>> # Get all users in reverse alphabetical order
# ... User.query.order_by(User.username.desc()).all()
# [<User Jadzia>, <User Dion>]

# >>> users = User.query.all()
# >>> for u in users:
# ...     db.session.delete(u)
# ... 
# >>> posts = Post.query.all()
# >>> for p in posts:
# ...     db.session.delete(p)
# ... 
# >>> db.session.commit()

