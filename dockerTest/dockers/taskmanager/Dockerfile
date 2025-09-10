FROM apache/flink:1.17.1-java11

USER root

# Install system dependencies for BCC/eBPF and building from source
RUN apt-get update && apt-get install -y \
    bison \
    build-essential \
    cmake \
    flex \
    git \
    clang \
    llvm \
    libclang-dev \
    llvm-dev \
    libelf-dev \
    python3 \
    python3-pip \
    libbpf-dev \
    iproute2 \
    net-tools \
    sudo \
    zip \
    kmod \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y python-is-python3

# Clone and build BCC from source (classic tools)
RUN git clone https://github.com/iovisor/bcc.git /bcc && \
    mkdir /bcc/build && cd /bcc/build && \
    cmake .. && make && make install && \
    rm -rf /bcc

# Install Python BCC package
RUN pip3 install bcc

#ENV FLINK_PROPERTIES="\
#jobmanager.rpc.address: jobmanager\n\
#taskmanager.numberOfTaskSlots: 4\n\
#jobmanager.memory.process.size: 2048m\n\
#taskmanager.memory.process.size: 4096m"

WORKDIR /
RUN mkdir taskmanager-logs
RUN mkdir taskmanager-logs/logs


#EXPOSE 8081

WORKDIR /taskmanager-logs

#CMD ["bash", "./scripts/run_job.sh"]

#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["taskmanager"]
