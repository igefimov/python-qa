FROM python:3.7
WORKDIR /opencart-test
ENV PATH="/opencart-test/drivers:${PATH}"

RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install -y dbus-x11 google-chrome-stable && \
  rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["pytest", "test3.py"]