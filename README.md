# Dash-GDP-Analysis

## Description

This project is an interactive data analysis dashboard built using Dash, a web application framework for Python. The dashboard visualizes Gapminder data, allowing users to explore the relationship between GDP per capita and life expectancy across different continents and years. Users can select a continent and a year to dynamically update the scatter plot, providing insights into global development trends.

## Why?

Understanding global development trends is crucial for policymakers, researchers, and the general public. This dashboard makes it easy to explore and analyze key indicators of development, such as GDP per capita and life expectancy, in an interactive and visually appealing way. By providing a tool to visualize this data, we can better understand the progress and challenges faced by different regions of the world.

## Quick Start

Follow these steps to run and use the Gapminder Data Dashboard:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/jeremiahwarinner/Dash-GDP-Analysis.git
   cd Dash-GDP-Analysis
2. **Install Required Libraries:**
   ensure you have Python installed. Then, install the necessary libraries using pip:
   ```bash
   pip install dash pandas plotly
4. **Run the Application:**
    ```bash
   python dashboardanalysis.py
6. **Access the Dashboard:**
   ```bash
   Open your web browser and go to http://127.0.0.1:8052/ to view the dashboard.

## Features
### Interactive Visualization
- **Dropdown Menu:** Select a continent to filter the data displayed on the scatter plot. The available continents are Asia, Europe, Africa, Americas, and Oceania.
- **Slider:** Choose a year to visualize the data for that specific year. The data spans from 1952 to 2007 in 5-year increments.
- **Dynamic Updates:** The scatter plot updates in real-time based on the selected continent and year, showing the relationship between GDP per capita and life expectancy.

### Data Insights
- **Scatter Plot:** The main visualization is a scatter plot where each point represents a country. The x-axis shows GDP per capita (log scale), and the y-axis shows life expectancy.
- **Bubble Size:** The size of each bubble represents the population of the country, providing an additional dimension of information.
- **Hover Information:** Hover over any point to see detailed information about the country, including the name, GDP per capita, and life expectancy.

## User-Friendly Interface
- **Title and Labels:** Clear titles and labels make the dashboard easy to understand and navigate.
- **Responsive Design:** The dashboard layout adjusts to different screen sizes, ensuring a good user experience on both desktop and mobile devices.
