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


#수정했어요  11