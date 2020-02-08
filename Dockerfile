FROM python:2

RUN pip install Flask
RUN pip install pandas
RUN pip install yfinance
RUN pip install lxml

COPY . .

EXPOSE 5000

CMD ["python", "dystapi.py"]
