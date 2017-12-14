FROM python:3.5
ENV PATH /usr/local/bin:$PATH
COPY ./ /code
WORKDIR /code/
RUN pip --default-timeout=100 install -r /code/requirements.txt

CMD ["/bin/bash"]


