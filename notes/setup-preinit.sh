#!/bin/bash
# Create empty initial files for project maintenance

# Virtual environment
virtualenv venv
source venv/bin/activate

# Dependencies and Automation
git init
touch .gitignore
touch pyproject.toml
touch Makefile
touch README.md
touch LICENSE

# Docker
touch Dockerfile
touch docker-compose.yml
touch .dockerignore
