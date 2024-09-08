# IPL 2024 Auction Data Analysis

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Features](#features)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Overview
This project conducts analysis on the players auctioned during the Indian Premier League (IPL) 2024 season. It provides insights into individual player performance as well as team dynamics based on the data collected from the auction. Users can interactively explore player and team statistics using the provided Streamlit web application.

## Prerequisites
Ensure you have Python installed on your system. You can install the required packages using the following command:

pip install numpy pandas streamlit streamlit-option-menu

## Getting Started
1. Clone the repository to your local machine:
git clone <repository-url>

2. Navigate to the project directory:
cd <project-directory>

3. Place your IPL 2024 auction data CSV file named `IPL 2024 SOLD PLAYER DATA ANALYSIS.csv` in the project directory.

4. Run the Streamlit application:
streamlit run app.py

5. The application will open in your default web browser. You can then interact with the interface to explore player and team analysis.

## Features
- **Home:** Displays the complete dataset of players auctioned in IPL 2024.
- **Player Analysis:** Allows users to select a player and view detailed analysis including their performance metrics.
- **Team Analysis:** Enables users to select a team and view comprehensive analysis of team statistics.

## File Structure
- `app.py`: Main Python script containing the Streamlit application code.
- `player_analysis.py`: Module for player-specific analysis.
- `team_analysis.py`: Module for team-specific analysis.
- `IPL 2024 SOLD PLAYER DATA ANALYSIS.csv`: CSV file containing the IPL 2024 auction data.

## Usage
- Upon running the application, navigate through the sidebar to access different analysis options.
- Select a player or team from the dropdown menu and click on "Show Analysis" to view the corresponding insights.

## Contributors
- Abhijit Maharana

## License
This project is licensed under the [MIT License](LICENSE).
