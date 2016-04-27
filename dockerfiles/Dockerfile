FROM osuosl/django-centos:latest
RUN yum -y update

RUN yum -y install gdal-python\
                   geos-python\
                   proj\
                   proj-nad\
                   postgresql-devel

COPY requirements.txt /opt/
RUN echo 'source /opt/streamwebs/dockerfiles/startup.sh' >> /root/.bash_profile

RUN pip install -r /opt/requirements.txt
