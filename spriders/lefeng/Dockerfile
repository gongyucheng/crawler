FROM python:3.5
ENV PATH /usr/local/bin:$PATH
COPY ./ /code
WORKDIR /code/
RUN pip install -r /code/lefeng/requirements.txt

CMD python run.py


