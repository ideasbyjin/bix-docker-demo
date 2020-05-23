FROM python:3.7-slim-stretch

COPY . /

RUN cd / && pip install -r requirements.txt

CMD ["python", "iris_histogram.py"]

