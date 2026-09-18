---
name: jma-forecast
description: 気象庁（JMA）の天気予報を取得する。天気・風・波・降水確率・気温を取得できる。
compatibility: Requires Python 3 and internet access to www.jma.go.jp. Uses only the Python standard library.
allowed-tools: Bash(python3 scripts/find_area.py:*) Bash(python3 scripts/get_forecast.py:*)
---

## 天気予報取得

1. `python3 scripts/find_area.py <エリア名>` で、エリアコードを取得。
2. `python3 scripts/get_forecast.py <エリアコード>` で、天気予報を取得。

## スクリプト仕様

### find_area.py

- 指定したエリア名に部分一致した `エリアコード: エリア名` が、1行1件で返る。
- 1件もヒットしなかった場合は、全エリアが返る。その中から該当するエリアを選ぶ。
- 取得できない場合は、その旨のメッセージが返る。

### get_forecast.py

- 指定したエリアコードの天気予報が、JSON で返る。
- 取得できない場合は、その旨のメッセージが返る。
