### Hexlet tests and linter status:
[![Actions Status](https://github.com/Mirrasol/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Mirrasol/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b02b88dc8943e175a445/maintainability)](https://codeclimate.com/github/Mirrasol/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b02b88dc8943e175a445/test_coverage)](https://codeclimate.com/github/Mirrasol/python-project-52/test_coverage)

Task Manager - a web-service that helps to organize a responsive to-do list for your project. Connect with your teammates and create a customizable environment for tracking your tasks and goals!

## 1) Features

  - login to gain access to your team's task list
  - create new and update existing tasks on the go
  - assign tasks to registered members of your team
  - provide a short description of your tasks
  - add statuses and labels for further customization

## 2) Installation

This project is built using Django as the main framework. Please refer to the pyproject.toml file for the full list of required dependencies.

`git clone git@github.com:Mirrasol/python-project-52.git` - download the package from GitHub

`make install` - install using pip from your console

Don't for get to create the .env file that contains your secret key and information about database!

`SECRET_KEY = enter_your_key`

`DATABASE_URL = {provider}://{user}:{password}@{host}:{port}/{db}`


Check Makefile for the rest of the available commands.

## 3) Demo Web-page

Check an example web-page (hosted on Render.com):

https://python-project-52-6g2a.onrender.com
