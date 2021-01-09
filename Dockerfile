FROM python:3

WORKDIR /usr/src/app

COPY sandbox-installs.csv
COPY halfbrick_rohan.py
COPY requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./halfbrick_rohan.py"]
