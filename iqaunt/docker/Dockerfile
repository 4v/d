FROM jupyter/tensorflow-notebook
MAINTAINER hexj 'hexj001@qq.com'

USER root
COPY source.list /etc/apt/source.list
# 修改docker的时区
RUN sudo apt update -y \
    && apt install -y apt-utils tzdata python3-tk git unzip \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime 

USER jovyan
ADD pip.conf /home/jovyan/.pip/pip.conf
RUN pip install --upgrade pip
# RUN sudo apt install -y python3-tk git unzip
# RUN pip install -r https://raw.githubusercontent.com/yutiansut/QUANTAXIS/master/requirements.txt -i https://pypi.doubanio.com/simple
RUN pip install --upgrade tushare pytdx pandas_datareader sklearn
# pandas beautifulsoup4 matplotlib tensorflow keras installed 

EXPOSE 8010 8888
