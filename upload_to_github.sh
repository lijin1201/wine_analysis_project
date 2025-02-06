#!/bin/bash


git config --global user.name "Li, Jin"
git config --global user.email "lijin1201@gmail.com"
git init
git add .
git commit -m "First commit"
git remote add origin https://github.com/lijin1201/wine_analysis_project.git
git push -u origin master
