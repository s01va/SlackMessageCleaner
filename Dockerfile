FROM python:3.11
LABEL authors="s01va"

COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt

ENV PYTHONPATH /app
ENV TZ Asia/Seoul

CMD ["python", "main.py"]