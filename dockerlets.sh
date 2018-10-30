#!/bin/bash
docker build -t xorful $PWD/cryptography/xorful/
docker build -t php-e $PWD/web/php/
docker build -t docs $PWD/web/docs/
docker build -t credentials $PWD/web/stolen-credentials/
docker build -t picky $PWD/web/picky-web/
