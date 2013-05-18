#!/bin/sh

CURDIR=`dirname "$0"`
wget -P $CURDIR -rk -l 1 -A pdf "https://www.ridemetro.org/News/Documents/RidershipReport.aspx"
