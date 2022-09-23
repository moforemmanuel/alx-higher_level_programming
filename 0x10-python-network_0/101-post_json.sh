#!/bin/bash
# post json
curl -s -X POST -H "Content-Type: application/json" "$1" -d "$(cat $2)"
