FROM python:3.12.4
WORKDIR /app
COPY . /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
EXPOSE 500
CMD ["python3", "app.py"]
