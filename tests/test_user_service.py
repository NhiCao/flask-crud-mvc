import unittest
import os
import sys
from sqlalchemy import func
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import config

from app.models.user import User
from app.services import user_service
from app import create_app, db



class TestUser(unittest.TestCase):
    def setUp(self):
        environ = os.environ.get('FLASK_ENV')
        print("\n----------environ--------------")
        print(environ)
        print("------------------------\n")

        for path in sys.path:
            print(path)

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
            max_user_id = 0
            result = db.session.query(func.max(User.id)).one()
            if result[0] is not None:
                max_user_id = result[0]
            
            user1 = User(id=max_user_id + 1, name='Nguyen Thi Test 1 - ' + environ, age='22', address='39 Tran Nhan Tong')
            user2 = User(id=max_user_id + 2, name='Tran Thi Test 2 - ' + environ, age='22', address='56 Pham Phu Thu')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
    
    def tearDown(self):
        with self.app.app_context():
            max_user_id = 0
            result = db.session.query(func.max(User.id)).one()
            if result[0] is not None:
                max_user_id = result[0]

            id1 = max_user_id
            user1 = User.query.filter_by(id=id1).first()
            db.session.delete(user1)
            id2 = max_user_id - 1
            user2 = User.query.filter_by(id=id2).first()
            db.session.delete(user2)
            # db.session.query(User).delete()
            db.session.commit()

    def test_get_all_users(self):
        with self.app.app_context():
            users = user_service.get_all_users()
            users_retrieved = User.query.all()
            self.assertGreaterEqual(len(users), 2)
            self.assertEqual(users, users_retrieved)

if __name__ == '__main__':
    unittest.main()
