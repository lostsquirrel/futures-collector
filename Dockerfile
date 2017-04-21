FROM registry.cn-hangzhou.aliyuncs.com/lisong/kline-base:0.1.0

ADD futures-collector/ /app
EXPOSE 9000

ENTRYPOINT [ "python", "/app/server.py" ]
