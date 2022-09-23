#!/bin/bash
# catch me
curl -s -X PUT -H "Content-Type: text/html" 0.0.0.0:5000/catch_me -F "body=You got me!"
