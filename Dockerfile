FROM python:3.7.0-stretch
LABEL mantainer="Vincenzo Palazzo v.palazzo1@studenti.unipi.it"
ADD ./ /code
WORKDIR code
ENV FLASK_APP=app.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python setup.py develop
EXPOSE 5001
CMD ["python", "app.py"]
