FROM python:3.10-rc-slim
WORKDIR /Bot
COPY . /Bot/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY Bot/rinbot.py .
ENTRYPOINT ["rinbot.py"]
