FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code


COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /code/


RUN python manage.py collectstatic --noinput


EXPOSE 8000


CMD ["gunicorn", "laptop_rental.wsgi:application", "--bind", "0.0.0.0:8000"]
