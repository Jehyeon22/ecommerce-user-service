FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt  # 캐시 비활성화로 빌드 최적화

# 애플리케이션 코드 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "app.py"]
