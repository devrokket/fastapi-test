# from typing import Union
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# # 경로 / 및 /items/{item_id}에서 HTTP 요청 받기.
# # 두 경로 모두 GET 연산(HTTP 메소드 로 알려진)을 받습니다.
# # 경로 /items/{item_id}는 경로 매개변수 int형 이어야 하는 item_id를 가지고 있습니다.
# # 경로 /items/{item_id}는 선택적인 str형 이어야 하는 경로 매개변수 q를 가지고 있습니다.
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI

app = FastAPI() #app 변수는 FastAPI 클래스 '인스턴스'


@app.get("/") #FastAPI에게 바로 아래에 있는 함수가 다음으로 이동하는 요청을 처리한다는 것을 알려줍니다.
async def root():
    return {"message": "My name is byeongrok"}