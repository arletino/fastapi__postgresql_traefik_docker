FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
RUN mkdir ./build
WORKDIR /build
COPY ./app/ ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#RUN apt update && apt install -y python3-pip                                  \
#    && pip3 install -r /build/requirements.txt                               \
#    && apt remove -y python3-pip                                              \
#    && apt autoremove --purge -y                                              \
#    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list
#EXPOSE 80
#CMD ["python3","-m", "uvicorn", "main:app", "--host=0.0.0.0", "--port", "80"]

