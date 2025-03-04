# sustainability-project

## Overview

A tool that measures the power consumption of code execution and compares results before and after linting. It helps developers to write more energy-efficient code by providing insights into power usage.

## Features

## Installation
Installation and Usage Instructions

### Prerequisites

Before running the application, make sure you have:

    Python 3.8+
    pip (Python package installer)

### Step 1: Clone the Repository

Run the following command in your terminal:

    git clone git@github.com:Honkajo/sustainability-project.git

Then navigate into the project directory:

    cd sustainability-project

### Step 2: Set Up a Virtual Environment

Create a virtual environment:

For Windows:

    python -m venv venv
    .\venv\Scripts\activate

For macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

### Step 3: Install Dependencies

Install the required Python packages:

    pip install -r requirements.txt

### Step 4: Run the Application

Start the Flask server with:

    flask run

The app will be accessible at http://127.0.0.1:5000/.

## How to use

1. Go to http://127.0.0.1:5000/.

2. Upload a .py file using the form.

3. Click Upload.

4. Website shows all the data from CodeCarbon that is collected
