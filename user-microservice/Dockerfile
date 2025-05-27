FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN prisma generate

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]