#!/bin/bash

./all_docker.sh | xargs -n1 realpath | xargs -n1 dirname
