from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()
    admin = User(username='admin', password='admin', is_admin=True)
    user = User(username='user', password='user')
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    
    print('Admin and user were created successfully')