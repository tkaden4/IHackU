FROM python:3.7
MAINTAINER Kaden Thomas
COPY . /app
WORKDIR /app
RUN pip install flask gunicorn
EXPOSE 80
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "stolen:app"]
