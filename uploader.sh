#!/bin/bash
curl -X POST -d temperature=@/tmp/temperature -d humidity=@tmp/humidity -d picture=@/tmp/tomatopi.jpg http://example.com

