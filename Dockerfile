FROM python:3.5
ENV PATH /usr/local/bin:$PATH
COPY ./quchenshi /code
WORKDIR /code/quchenshi
RUN pip install -r /code/quchenshi/requirements.txt

CMD [ "scrapy", "crawl","quchenshi" ]


