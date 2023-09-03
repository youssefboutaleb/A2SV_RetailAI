
<div align="center">
  <h1>RetailAI Project</h1>
</div>

<p align="center">

 
   <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/forks" target="_blank">
    <img src="https://img.shields.io/github/forks/youssefboutaleb/A2SV_RetailAI" alt="Badge showing the total of project forks"/>
  </a>

  <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/stargazers" target="_blank">
    <img src="https://img.shields.io/github/stars/youssefboutaleb/A2SV_RetailAI" alt="Badge showing the total of project stars"/>
  </a>

  <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/tree/main/commits/main" target="_blank">
    <img src="https://img.shields.io/github/commit-activity/m/youssefboutaleb/A2SV_RetailAI/tree/main?" alt="Badge showing average commit frequency per month"/>
  </a>

  <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/commits/main" target="_blank">
  <img src="https://img.shields.io/github/last-commit/youssefboutaleb/A2SV_RetailAI/main?" alt="Badge showing when the last commit was made"/>
</a>


  <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/tree/main/issues" target="_blank">
    <img src="https://img.shields.io/github/issues/youssefboutaleb/A2SV_RetailAI/tree/main?" alt="Badge showing the total of project issues"/>
  </a>

  <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/tree/main/pulls" target="_blank">
    <img src="https://img.shields.io/github/issues-pr/youssefboutaleb/A2SV_RetailAI/tree/main?" alt="Badge showing the total of project pull-requests"/>
  </a>
  <a href="https://badge.fury.io/py/tensorflow" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/tensorflow.svg" alt="Python Version Badge"/>
  </a>

  <a href="https://github.com/youssefboutaleb/A2SV_RetailAI/blob/main/LICENSE.md" target="_blank">
  <img alt="Badge showing project license type" src="https://img.shields.io/github/license/youssefboutaleb/A2SV_RetailAI?color=f85149">
</a>

</p>



## Purpose

The Retailors Project aims to address common challenges faced by retailers:

#### Inventory Optimization: 
By leveraging Generative AI models like ARIMA, the platform helps retailers optimize their inventory levels, reducing costs and minimizing stockouts.

#### Demand Forecasting:
The AI models provide accurate demand forecasts, aiding retailers in making informed decisions regarding stock replenishment and purchasing.

#### User Support:
The integration of the Llama Chatbot API enhances customer support by providing answers to questions related to data outcomes and retail operations.

## How Predictive AI Models Address the Problem
#### ARIMA Model:
The ARIMA model is employed for time-series forecasting. It analyzes historical sales and inventory data to generate predictions for future demand. These predictions guide retailers in making inventory decisions, reducing excess stock, and improving overall efficiency.

#### Linear Regression Model:
Linear regression complements ARIMA by providing additional insights. It helps retailers understand how various factors, such as promotions or marketing campaigns, impact demand. This information aids in fine-tuning inventory strategies.


## Overview

The Retailors Project is a web-based platform that utilizes Generative AI models to assist retailers in optimizing their inventory management and demand forecasting. This README file provides an overview of the project structure, its purpose, and how Generative AI models are addressing the problem.
## Project Structure

The project is organized into the following components:

### Frontend: 
This directory contains the HTML, CSS, and JavaScript files for the website's user interface.

### Backend: 
The backend is built using Flask, a Python web framework. It includes routes for handling user input, making predictions with Generative AI models, and serving results.

### AI Models:
We have incorporated two main Generative AI models into the project:

#### ARIMA (AutoRegressive Integrated Moving Average):
This model is used for time-series forecasting, helping retailers predict future demand based on historical data.
#### Linear Regression: 
Linear regression is employed for additional predictive analytics.

#### API Integration: 
The project integrates with external APIs, including the Llama Chatbot API, to enhance user experience and provide additional support to customers.

### Database: 
A database, implemented using PostgreSQL, stores historical sales and inventory data for analysis and training of AI models.
## Run Locally

To run the Retailors Project locally, follow these steps:

#### Clone the repository 

```bash
  git clone https://github.com/youssefboutaleb/A2SV_RetailAI.git
```

#### Go to the project directory

```bash
  cd A2SV_RetailAI
```

#### Set up a virtual environment and install the required Python packages 
 Create a Virtual Environment

```bash
  python -m venv <venv>
```
 Activate the Virtual Environment:
- On Windows:

```bash
.\<venv>\Scripts\activate
```
- On macOS and Linux:

```bash
source venv/bin/activate
```
#### Install Required Packages 


```bash
pip install -r requirements.txt
```
#### Start the server

```bash
  python app.py

```
#### Deactivate the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running the following command:

```bash
deactivate
```







