FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --root-user-action=ignore

COPY ./ /code/

CMD ["python", "./app.py", "--host", "90.156.227.209", "--port", "8081"]