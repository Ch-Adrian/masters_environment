FROM apache/flink:1.17.1-java11

RUN apt-get clean
RUN apt-get update

WORKDIR /
RUN mkdir workspace
RUN mkdir workspace/tasks
RUN mkdir workspace/scripts
RUN mkdir workspace/output

EXPOSE 8081

WORKDIR /workspace

CMD ["jobmanager"]