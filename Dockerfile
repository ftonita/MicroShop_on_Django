FROM python:3

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

CMD [ "python3", "TestShop/manage.py", "runserver" ]
# CMD ["ls"]