#!/bin/bash

rm -rf poetry.lock pyproject.toml .upm
pip3 uninstall poetry -y

if [ "${SOURCE_AUTO_UPDATE,,}" == "true" ]; then
  bash quick_update.sh
fi

if [ ! -d "venv" ] || [ ! -f "./venv/bin/requirements.txt" ] || [ ! "$REPL_SLUG-$REPL_OWNER" == "$(cat ./venv/.deployed)" ]; then
  rm -rf venv .config .cache local_database .logs Lavalink.jar pyproject.toml poetry.lock
  echo -e "\n####################################" \
          "\n### Khởi tạo env ảo... ###" \
          "\n####################################\n"
  python3 -m venv venv
  . venv/bin/activate
  python3 -m pip install -U pip
  echo -e "\n###################################################" \
          "\n### Cài đặt phụ thuộc...                  ###" \
          "\n### (Quá trình này có thể mất đến 3 phút). ###" \
          "\n###################################################\n"
  pip3 install -U -r requirements.txt --no-cache-dir
  cp -r requirements.txt ./venv/bin/requirements.txt
  echo -n "$REPL_SLUG-$REPL_OWNER" > ./venv/.deployed

elif ! cmp --silent -- "./requirements.txt" "./venv/bin/requirements.txt"; then
  echo -e "\n##############################################" \
          "\n### Cài đặt/cập nhật phụ thuộc... ###" \
          "\n##############################################\n"
  . venv/bin/activate
  pip3 install -U -r requirements.txt --no-cache-dir
  cp -r requirements.txt ./venv/bin/requirements.txt

else
  . venv/bin/activate

fi

python3 main.py