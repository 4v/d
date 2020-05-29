FROM amd64/centos
RUN yum -y install wget \
    && wget -O /etc/yum.repos.d/CentOS-Base-163.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo \
    && yum clean all && yum makecache \
    && yum -y install git vim unzip cmake make gcc gcc-c++ && mkdir /opt/ls/
WORKDIR /opt/ls
RUN git clone https://github.com/taosdata/TDengine.git \
    && cd TDengine && mkdir build && cd build \
    && cmake .. && cmake --build . 
WORKDIR /opt/ls/TDengine/build
RUN make install && sed -i 's/# charset/  charset/g' /etc/taos/taos.cfg \
    && cp /opt/ls/TDengine/build/build/lib/libtaos.so /usr/lib64 && ldconfig
# create default db
RUN sed -i 's/# defaultDB/  test/g' /etc/taos/taos.cfg 
# RUN yum -y install java-1.8.0-openjdk-devel.x86_64 && echo 'export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-2.b15.el7_2.x86_64' > /etc/profile && echo 'export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar' >> /etc/profile && echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile && source /etc/profile
EXPOSE 6035 6020
CMD ["taosd"]