FROM alpine:3.17.0

# Init
RUN apk update && \
    apk add --no-cache gcc libc-dev python3 py3-pip

# Create user and set up password
RUN adduser -D -u 1000 challenge && \
    echo "challenge:$(head -c 32 /dev/urandom | base64)" | chpasswd

# Set up flag
WORKDIR /root/
COPY getflag.c .
RUN gcc getflag.c -o getflag && \
    chmod u+s getflag && \
    mv getflag ../ && \
    rm getflag.c
COPY flag.txt .

# Set up webapp
WORKDIR /app/
COPY ./challenge/ .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Switch to the challenge user
USER challenge

# Command to run the app
CMD ["python3", "app.py"]
