#!/usr/bin/env python3
"""気象庁のエリアコードをエリア名で検索する。"""

import argparse
import json
import urllib.error
import urllib.request

AREA_URL = "https://www.jma.go.jp/bosai/common/const/area.json"


def main():
    parser = argparse.ArgumentParser(
        description="エリア名で部分一致検索し、エリアコードとエリア名を出力する。",
        epilog="ヒットしなかった場合は全エリアを出力する。",
    )
    parser.add_argument("name", help="検索するエリア名（部分一致）")
    args = parser.parse_args()

    try:
        with urllib.request.urlopen(AREA_URL) as res:
            offices = json.load(res)["offices"]
    except urllib.error.URLError:
        print("エリア情報を取得できませんでした。")
        return

    matches = {code: v["name"] for code, v in offices.items() if args.name in v["name"]}
    if not matches:
        matches = {code: v["name"] for code, v in offices.items()}

    for code, area_name in matches.items():
        print(f"{code}: {area_name}")


if __name__ == "__main__":
    main()
