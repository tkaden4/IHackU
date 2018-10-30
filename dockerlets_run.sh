#!/bin/bash

docker run -p 8001:80 -d xorful
docker run -p 8002:80 -d php-e
docker run -p 8003:80 -d docs
docker run -p 8004:80 -d credentials
docker run -p 8005:80 -d picky
