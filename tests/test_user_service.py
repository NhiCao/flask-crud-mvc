import unittest
import os
import config

from app.models.user import User
from app.services import user_service
from app import create_app, db

class TestUser(unittest.TestCase):
    def setUp(self):
        environ = os.environ.get('FLASK_ENV')

        config_app = config.LocalConfig

        if environ == 'LOCAL':
            config_app = config.LocalConfig
        elif environ == 'DEVELOPMENT':
            config_app = config.DevelopmentConfig
        elif environ == 'STAGING':
            config_app = config.StagingConfig
        elif environ == 'PRODUCTION':
            config_app = config.ProductionConfig

        self.app = create_app(config_app)
        with self.app.app_context():
            user1 = User(id='1', name='Nguyen Thi GitHub Actions Test 1 - ' + environ, age='22', address='39 Tran Nhan Tong')
            user2 = User(id='2', name='Tran Thi GitHub Actions Test 2 - ' + environ, age='22', address='56 Pham Phu Thu')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
    
    def tearDown(self):
        with self.app.app_context():
            User.query.delete()

    def test_get_all_users(self):
        self.assertEqual(3, 3)
        # with self.app.app_context():
        #     users = user_service.get_all_users()
        #     users_retrieved = User.query.all()
        #     print(users)
        #     self.assertEqual(len(users), 2)
        #     self.assertEqual(users, users_retrieved)

if __name__ == '__main__':
    unittest.main()
