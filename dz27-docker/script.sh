#!/usr/bin/env bash
# This will remove:
#        - all stopped containers
#        - all networks not used by at least one container
#        - all dangling images
#        - all build cache
docker system prune -f

# Build our image from a Dockerfile
docker build -t my_opencart_test .

# 2x Run container from the image

# This will pass
docker run -e ADMIN_URL="http://192.168.0.122/opencart/admin/" my_opencart_test
# This will pass too
docker run my_opencart_test
#This will fail
#docker run -e ADMIN_URL="http://fakeUrl.com" my_opencart_test
