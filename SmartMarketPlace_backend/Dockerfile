#Escojo la imagen de python que voy a usar
FROM python:3.9.6
#Variable del ambiente que envia el output de python directo al terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
#Creo un directorio llamado smp-back
RUN mkdir /smp-back
#Escojo ese directorio sm-back como mi directorio de trabajo
WORKDIR /smp-back
#Copio Requirements.txt a smp-back
COPY requirements.txt /smp-back
#Corre el pip install de los requerimientos
RUN pip install -r requirements.txt
RUN apt-get -q update && apt install wait-for-it
#Copio el resto de cosas
COPY . /smp-back