#!/bin/bash

API="o.CAMwum16HvQlGh4zq0DxBGEbxxvZhgVQ"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Alert" -d body="$MSG"