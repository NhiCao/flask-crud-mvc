import unittest
from app.models.user import User
from app.services import user_service
from app import create_app, db

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

        User.query.delete()

        user1 = User(id='1', name='Nguyen Thi GitHub Actions Test 1', age='22', address='39 Tran Nhan Tong')
        user2 = User(id='2', name='Nguyen Thi GitHub Actions Test 2', age='22', address='56 Pham Phu Thu')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    def test_get_all_users(self):
        with self.app.app_context():
            users = user_service.get_all_users()
            users_retrieved = User.query.all()
            self.assertEqual(users, users_retrieved)

if __name__ == '__main__':
    unittest.main()
