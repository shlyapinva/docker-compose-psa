FROM ubuntu:latest

LABEL maintainer="shlyapinva@mail.ru"

ARG USER=deploer


RUN useradd -m ${USER} && \
    apt-get update -yq && \
    apt-get install -yq python3-pip python3-psycopg2 libpq-dev git  && \
    apt-get clean && \
    rm -rf \
      /var/lib/apt/lists/* \
      /tmp/* \
      /var/tmp/*
      
      
WORKDIR /home/${USER}

USER user ${USER}

RUN git clone https://github.com/mbaran0v/python-sample-app &&\
    cd ./python-sample-app && \
    chmod -R  777 static && \
    pip3 install -r requirements.txt
    

WORKDIR /home/${USER}/python-sample-app

EXPOSE 5000

#CMD ["python3", "app.py"]
#ENTRYPOINT [ "entrypoint.sh" ]
CMD sleep 15 &&python3 app.py


