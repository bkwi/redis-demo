FROM python:3.11.2-slim-bullseye

ENV PROJECT_DIR=/code
WORKDIR $PROJECT_DIR

COPY ./requirements/worker.txt /$PROJECT_DIR/requirements.txt
RUN pip install -r requirements.txt
