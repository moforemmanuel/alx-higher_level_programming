#!/bin/bash
curl -s -o /dev/null "$1" -w '%{size_download}'
