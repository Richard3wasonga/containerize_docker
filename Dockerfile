# Dockerfile, Image, Conatiner

FROM python:3.12

ADD main.py .

RUN pip install requests beautifulsoup4 lxml

CMD ["python", "./main.py"]