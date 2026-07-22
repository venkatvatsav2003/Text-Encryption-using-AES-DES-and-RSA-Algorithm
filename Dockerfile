FROM python:3.11-slim

WORKDIR /crypto

RUN pip install --no-cache-dir cryptography pyyaml

COPY . /crypto
RUN mkdir -p keys

ENTRYPOINT ["./crypto.sh"]
CMD ["help"]
