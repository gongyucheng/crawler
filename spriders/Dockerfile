FROM python:3.5
FROM scrapinghub/splash:latest
ENV PATH /usr/local/bin:$PATH
COPY ./ /code
WORKDIR /code/
RUN pip install -r /code/requirements.txt

CMD python run.py


