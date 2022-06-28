import pytest

from app.application.service.user import UserService
from app.domain.entity import User
from tests.fakes import FakeUserRepository

"""
- 페이크 객체 활용
- FakeUserRepository() 페이크 객체를 이용해서 의존성 대체
"""


@pytest.fixture
def user_service():
    repository = FakeUserRepository()
    user_service = UserService(repository=repository)
    return user_service


def test_create_user_well(user_service):
    user_name = "adam"

    user = user_service.create_user(user_name=user_name)

    assert user == User(name=user_name)


def test_create_user_duplicated(user_service):
    user_name = "adam"

    user_service.create_user(user_name=user_name)

    # 중복 가입
    with pytest.raises(ValueError):
        user_service.create_user(user_name=user_name)
