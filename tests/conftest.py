import os
os.environ["ENV"] = "test"
import pytest
from app import flaskapp, db
from app.models.user import UserModel
from app.models.category import CategoryModel
from app.models.item import ItemModel

@pytest.fixture(scope='module')
def client():
    client = flaskapp.test_client()
    ctx = flaskapp.app_context()
    ctx.push()

    yield client
    
    ctx.pop()

@pytest.fixture(scope='session')
def init_db():
    user1 = UserModel('Test User1', 'testuser1', 'testpassword123', 'testuser1@gmail.com')
    user2 = UserModel('Test User2', 'testuser2', 'testpassword123', 'testuser2@gmail.com')
    category1 = CategoryModel('Category 1', 'Test category number 1')
    category2 = CategoryModel('Category 2', 'Test category number 2')
    item1 = ItemModel('Item 1', 'Test item number 1', 10, 1, 1)
    item2 = ItemModel('Item 2', 'Test item number 2', 20, 1, 1)
    user1.save_to_db()
    user2.save_to_db()
    category1.save_to_db()
    category2.save_to_db()
    item1.save_to_db()
    item2.save_to_db()

    yield db

    db.session.close()
    db.drop_all()
