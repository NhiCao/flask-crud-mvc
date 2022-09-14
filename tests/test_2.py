import unittest
from app.models.user import User
from app.services import user_service
from app import create_app, db

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    def test_get_all_users(self):
        with self.app.app_context():
            users = user_service.get_all_users()
            users_retrieved = User.query.all()
            self.assertEqual(users, users_retrieved)

if __name__ == '__main__':
    unittest.main()
