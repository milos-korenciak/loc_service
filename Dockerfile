# https://docs.docker.com/engine/reference/builder/

FROM continuumio/miniconda3

COPY . loc_service
WORKDIR /loc_service

RUN  \
python -m pip install -U pip setuptools && \
python -m pip install -U -r requirements.txt && \
ps

EXPOSE 8088

CMD bash run.sh
