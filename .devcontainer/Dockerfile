FROM python:3.9
# Timezone Setting
ENV TZ='Asia/Tokyo'
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# pip install
RUN pip install --upgrade pip \
    && pip install numpy \
    && pip install matplotlib \
    && pip install ipykernel \
    && pip install autopep8 \
    && pip install pytest \
    && pip install requests \
    && pip install lxml \
    && pip install cssselect
# python_crawling_scraping
RUN apt update \
    && apt -y install tree