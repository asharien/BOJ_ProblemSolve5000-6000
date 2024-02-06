#!/bin/bash
today=$(date)
echo $today
git config --global user.name asharien
git config --global user.email asharien@naver.com 
git add .
git commit -m "Upload from Termux $today"
.././autofill.exp
