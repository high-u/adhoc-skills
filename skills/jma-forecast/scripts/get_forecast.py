#!/usr/bin/env python3
"""気象庁の短期予報を取得する。"""

import argparse
import json
import urllib.error
import urllib.request

FORECAST_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/{code}.json"


def convert_area(entry, time_defines):
    """配列のインデックスを日時キーに置き換える。weatherCodes は捨てる。"""
    out = {"area": entry["area"]}
    for key, values in entry.items():
        if key in ("area", "weatherCodes"):
            continue
        out[key] = dict(zip(time_defines, values))
    return out


def main():
    parser = argparse.ArgumentParser(
        description="指定したエリアコードの短期予報をJSONで出力する。",
        epilog="エリアコードは find_area.py で調べる。",
    )
    parser.add_argument("code", help="エリアコード（例: 130000）")
    args = parser.parse_args()

    try:
        with urllib.request.urlopen(FORECAST_URL.format(code=args.code)) as res:
            data = json.load(res)
    except urllib.error.URLError:
        print("予報を取得できませんでした。")
        return

    short_term = data[0]
    weather, pop, temp = short_term["timeSeries"]
    out = {
        "publishingOffice": short_term["publishingOffice"],
        "reportDatetime": short_term["reportDatetime"],
        "weather": [convert_area(a, weather["timeDefines"]) for a in weather["areas"]],
        "pop": [convert_area(a, pop["timeDefines"]) for a in pop["areas"]],
        "temp": [convert_area(a, temp["timeDefines"]) for a in temp["areas"]],
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
