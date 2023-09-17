#!/bin/bash

export PYTHONIOENCODING=utf8

trap 'kill $(jobs -pr)' SIGINT SIGTERM EXIT

echo "Tạo tệp VENV (vui lòng chờ đợi ...)"

rm -rf venv

if [ -x "$(command -v py)" ]; then
  py -3 -m venv venv
else
  python3 -m venv venv
fi

if [ ! -d "venv" ]; then
  echo "Thư mục VENV đã không được tạo! Kiểm tra xem bạn đã cài đặt Python một cách chính xác (và được cấu hình trong Path/Env)"
  sleep 45
  exit 1
fi

if [[ $OSTYPE == "msys" ]]; then
  VENV_PATH=venv/Scripts/activate
else
  VENV_PATH=venv/bin/activate
fi

source $VENV_PATH

mkdir -p ./.logs

touch "./.logs/setup.log"

python -m pip install -U pip

pip install -r ./requirements.txt 2>&1 | tee "./.logs/setup.log"

if [ ! -f ".env" ] && [ ! -f "config.json" ]; then
  cp .example.env .env
  echo 'Đừng quên thêm các mã thông báo cần thiết vào tệp .env'
fi

x=msgbox("Đừng quên thêm các thông cần thiết (TOKEN,PREFIX,SPOTIFY_TOKEN) vào tệp .env", 0+64, "Thông Báo")

sleep 30s

sleep 30s
