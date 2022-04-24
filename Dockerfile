FROM vernonranis/img-python-base:1.01-3.10.4-3.15

COPY . .

CMD ["python", "./app.py"]