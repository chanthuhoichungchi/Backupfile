#!/bin/bash

export PYTHONIOENCODING=utf8

touch "./.logs/setup.log"

pip install -r ./requirements.txt 2>&1 | tee "./.logs/setup.log"

if [ ! -f ".env" ] && [ ! -f "config.json" ]; then
  cp .example.env .env
  echo 'Đừng quên thêm các mã thông báo cần thiết vào tệp .env'
fi
