#!/bin/bash

# 現在のディレクトリ名を取得して小文字に変換
contest_name=$(basename "$PWD" | tr '[:upper:]' '[:lower:]')

# 各ディレクトリに移動して oj d を実行
for problem in a b c d; do
  cd "$problem" || exit
  oj d "https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem}"
  cd ..
done
