FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/
EXPOSE 5000/tcp
CMD [ "python3", "-u", "web.py"]
