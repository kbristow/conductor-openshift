FROM python:2.7

COPY . .

ENV USER_ID=1001

COPY ./scripts/entrypoint.sh ./entrypoint.sh

RUN chmod +x "./entrypoint.sh"

RUN pip install -r requirements.txt

USER ${USER_ID}

ENTRYPOINT ["./entrypoint.sh"]