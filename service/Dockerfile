FROM postgres

WORKDIR src
ADD src/ /src/
# RUN  apt-get update  && apt-get install -y python3 &&  apt install -y python3-pip &&  apt-get install libpq-dev && pip3 install psycopg2 && pip3 install pandas

COPY  src/create_table.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
