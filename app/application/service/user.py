from signal import raise_signal
from app.application.interfaces.user_repository import AbstractRepository
from app.domain.entity import User


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    # 클라이언트가 무엇을 해줄지, 유즈케이스부터 작성
    # 어떤도구 어떤 프레임워크를 사용할지는 나중에
    def create_user(self, user_name: str):
        # 데이터베이스에 저장
        _user = User(name=user_name)

        # 데이터베이스에서 해당 이름이 있는지 확인, 있다면 Exception 발생
        if self.repository.find_one(model=_user):
            raise ValueError("유저가 이미 존재합니다.")
        user = self.repository.create(_user)

        return user
