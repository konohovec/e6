FROM python:3.8.5
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app/main.py /app/main.py
COPY ./app/utils.py /app/utils.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
