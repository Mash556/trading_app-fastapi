FROM python:3.10

# создадим новую папку
RUN mkdir /fastapi_app

# и эта новая созданная папка является нашим рабочим директорием
WORKDIR /fastapi_app

# копируем файл requirements в папочку fastapi_app и  
copy requirements.txt .

# и устанавливаем эти зависимости
run pip install -r requirements.txt

# копируем все папки и файлы в наш текущую рабочую деректорию

COPY . .
ENTRYPOINT ["docker/entrypoint.sh"]

RUN chmod a+x docker/*.sh


# переходим в папочку src чтобы запустить проект
WORKDIR src

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

