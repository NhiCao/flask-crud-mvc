from app.models.user import User
from app import create_app, db

user1 = User(id='1', name='Nguyen Thanh Nam', age='22', address='39 Tran Nhan Tong')
user2 = User(id='2', name='Le Thi Lan Phuong', age='22', address='56 Pham Phu Thu')

app = create_app()
with app.app_context():
    # db.create_all()
    User.query.delete()
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()