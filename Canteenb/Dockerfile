FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /canteen

RUN echo " " > /etc/apt/sources.list ;
RUN echo \
    'deb http://mirrors.aliyun.com/debian/ buster main non-free contrib\n\
    deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib\n\
    deb http://mirrors.aliyun.com/debian-security buster/updates main\n\
    deb-src http://mirrors.aliyun.com/debian-security buster/updates main\n\
    deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib\n\
    deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib\n\
    deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib\n\
    deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib'\
    > /etc/apt/sources.list2

RUN apt-get clean && apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev libmariadb-dev-compat libmariadb-dev pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.py", "Canteen.wsgi:application"]