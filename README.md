<<<<<<< HEAD
# Devops_Journey: Weather Dashboard Demo- Day 1
=======
# DevOps_All_Stars: Weather Data Collection System - Day 1
>>>>>>> dd23760 (Save changes before pulling remote updates)

Day 1: Building a weather data collection system using AWS S3 and OpenWeather API

## Overview
This project is a Weather Data Collection System that demonstrates core DevOps principles by combining:
- External API Integration (OpenWeather API)
- Cloud Storage (AWS S3)
- Infrastructure as Code
- Version Control (Git)
- Python Development
- Error Handling
- Environment Management

## Features
- Fetches real-time weather data for multiple cities
- Displays temperature (°F), humidity, and weather conditions
- Automatically stores weather data in AWS S3
- Supports multiple cities tracking
- Timestamps all data for historical tracking

## Technical Architecture
- **Language:** Python 3.x
- **Cloud Provider:** AWS (S3)
- **External API:** OpenWeather API
- **Dependencies:** 
  - boto3 (AWS SDK)
  - python-dotenv
  - requests

```markdown
## Project Structure
weather-dashboard/
  src/
    __init__.py
    weather_dashboard.py
  tests/
  data/
  .env
  .gitignore
  requirements.txt

## Setup Instructions
1. Clone the repository:
--bash
<<<<<<< HEAD
git clone https://github.com/CloudFay/DevOps_Journey.git
=======
git clone https://github.com/Enoredia/DevOpsAllStars.git/

>>>>>>> dd23760 (Save changes before pulling remote updates)
3. Install dependencies:
 pip install -r requirements.txt

4. Configure environment variables (.env):
OPENWEATHER_API_KEY=your_api_key
AWS_BUCKET_NAME=your_bucket_name

4.Configure AWS credentials:
aws configure

5. Run the application:
python3 src/weather_dashboard.py

What I Learned

AWS S3 bucket creation
Git workflow
Error handling
Cloud resource management

Resources

ShaeInTheCloud: https://youtu.be/A95XBJFOqjw?si=PV0pgFPyjNFRFJeG
Open weather API: https://openweathermap.org/api
