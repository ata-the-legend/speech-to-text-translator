FROM python:3.11.4-slim-buster

EXPOSE 8000
WORKDIR /app

RUN apt-get update && apt-get install -y curl jq

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]