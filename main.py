from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

# app/routers/__init__.py 덕분에 이렇게 한 번에 가져올 수 있습니다.
from app.routers import (
    chat_router, 
    mbti_router, 
    python_router, 
    report_router, 
    stt_router, 
    goalskill_router
)

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록 (조립)
app.include_router(chat_router)
app.include_router(mbti_router)
app.include_router(python_router)
app.include_router(report_router)
app.include_router(stt_router)
app.include_router(goalskill_router)

# 프론트엔드 정적 파일 연결
# 현재 파일 위치 기준 상위 폴더의 front 폴더를 찾습니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
front_path = os.path.join(os.path.dirname(current_dir), "front")

if os.path.exists(front_path):
    app.mount("/", StaticFiles(directory=front_path, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # 실행 시: back 폴더에서 python main.py
    uvicorn.run(app, host="0.0.0.0", port=5450, log_level="debug")