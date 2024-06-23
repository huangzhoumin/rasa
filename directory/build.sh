#!/usr/bin/env bash
#训练模型,重命名模型名字
# 默认只保留一个模型
function train() {
  rm -f models/*
  rasa train --domain ./domain.yml --endpoints ./endpoints.yml
  model_name=$(ls models/)
  mv models/${model_name} models/rasa-$(date +"%Y%m%d%H%M%S").tar.gz
}

function run() {
    name=$(ls models|tail -n 1)
    if [ "$name" = "" ];then
      echo "[error]不存在模型"
      exit 1
    fi
    rasa shell -m models/${name}  --endpoints endpoints.yml
}

function main() {
    if [ "$1" = "build" ];then
      train
    elif [ "$1" = "run" ]; then
      run
    fi
}

main $@
