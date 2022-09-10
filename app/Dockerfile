FROM python:3.10.4

WORKDIR //app

COPY requirements.txt //app//requirements.txt
RUN pip install -r //app//requirements.txt && apt-get update

COPY . //app

ENTRYPOINT ["python", "//app//pooling_start.py"]
