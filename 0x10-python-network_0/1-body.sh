#!/bin/bash
# print body if status success
if [ $(curl -LI "$1" -o /dev/null -w '%{http_code}\n' -s) == "200" ]; then curl -sb "$1"; fi
