# ####### 👇 SIMPLE SOLUTION (x86 and M1) 👇 ########
FROM python:3.10.6

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY nba_predict nba_predict
COPY setup.py setup.py
RUN pip install .

CMD uvicorn nba_predict.api.fast:app --host 0.0.0.0 --port $PORT
