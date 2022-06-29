import pytest

from app.domain.entity import User
from app.infrastructure.database.orm import db, UserModel
from app.infrastructure.database.repository.user import UserRepository


@pytest.fixture
def init_databases():
    # 파일형태에 DB에 저장하지 않고 메모리에 임시적으로 데이터 저장
    db.init(database=":memory:")
    db.connect()
    UserModel.create_table()


# Default : fixture(scope="function")
# 함수가 불릴 떄마다 init_database() 호출하여 초기화
def test_create_user_repository(init_databases):
    name = "adam"
    _user = User(name=name)
    repository = UserRepository()

    created_user = repository.create(_user)
    # user = repository.find_one(_user)

    assert _user == created_user
