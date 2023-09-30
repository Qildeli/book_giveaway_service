FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Command to run on container start
CMD ["gunicorn", "book_giveaway_service.wsgi:application", "--bind", "0.0.0.0:8000"]

