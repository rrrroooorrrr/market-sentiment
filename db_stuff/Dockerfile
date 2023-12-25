# Use the official Alpine Linux image as the base image
FROM alpine:latest

# Install MongoDB and other required packages
RUN apk add --no-cache mongodb-tools

# Create a directory to store MongoDB data
RUN mkdir -p /data/db

# Expose the default MongoDB port
EXPOSE 27017

# Start the MongoDB server
CMD ["mongod"]
