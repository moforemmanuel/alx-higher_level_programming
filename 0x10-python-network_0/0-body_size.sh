#!/bin/bash
# display size of response
curl -s -o /dev/null "$1" -w '%{size_download}'