#!/bin/bash
sleep 2s
echo "pushing now"
git add .
git commit -m 'added pages'
git push origin master

