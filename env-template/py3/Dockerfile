FROM python:3.7-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && cat /etc/apk/repositories \
    && echo -e "[global]\nindex-url = http://mirrors.aliyun.com/pypi/simple/\n[install]\ntrusted-host=mirrors.aliyun.com">>/etc/pip.conf 
RUN apk add --no-cache build-base python3-dev libstdc++ && \
    apk add --no-cache --virtual .build-deps g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && pip install --upgrade pip
# RUN apk add --update build-base python python-dev py-pip && pip install --upgrade pip
