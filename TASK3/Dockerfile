FROM python:3.8
COPY . /TASK3/app
WORKDIR /TASK3/app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--reload"]