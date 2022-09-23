#!/bin/bash
# catch me
curl -s -X PUT -H "Content-Type: text/html; charset=utf-8" 0.0.0.0:5000/catch_me -F "body=You got me!"
