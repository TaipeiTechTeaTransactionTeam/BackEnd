@echo off
git add .
git reset HEAD manage.py
git commit -m "%1"
git push origin NawaNawa