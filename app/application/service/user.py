from app.domain.entity import User


# 클라이언트가 무엇을 해줄지, 유즈케이스부터 작성
# 어떤도구 어떤 프레임워크를 사용할지는 나중에
def create_user(user_name: str):
    user = User(name=user_name)
    return user
