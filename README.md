# RASA Chatbot for College Admission Assistance

This repository contains a RASA-based chatbot developed for assisting new students and handling first-year admissions at [Your College Name]. The chatbot is designed to answer frequently asked questions and guide students through the admission process.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Training the Model](#training-the-model)
- [Running the Chatbot](#running-the-chatbot)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview

This chatbot was developed using the RASA Open Source platform and Flask. It can handle common queries related to the admission process, course details, campus facilities, and more. The chatbot is designed to provide quick and accurate responses to help new students navigate their way through the college admission process.

## Features
- **Natural Language Understanding (NLU):** Understands user queries and provides relevant responses.
- **Interactive Conversations:** Handles multi-turn conversations.
- **Custom Actions:** Integrates with external APIs for additional information.
- **Flask Integration:** The bot is served using a Flask web application.


## Installation

Since this Chatbot runs on RASA Open Source platform, you need to install the below below mentioned before installing it
- Anaconda Navigator
  ```link
  https://www.anaconda.com/download


After installing Anaconda in your system, in Anaconda Prompt, do the following:
- Creating new Environment
  ```bash
  conda create -n rasa-chat python=3.8 # version should be more than 3.8
  

To get started with the chatbot, clone this repository and install the necessary dependencies.

```bash
git clone https://github.com/SKaushikAK/Rasa.git
cd Rasa
pip install -r requirements.txt
