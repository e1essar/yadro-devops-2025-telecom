FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

WORKDIR /app

COPY httpstat_script.py /app/httpstat_script.py

RUN pip3 install --no-cache-dir requests

RUN chmod +x /app/httpstat_script.py

ENTRYPOINT ["python3", "/app/httpstat_script.py"]
