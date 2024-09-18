# Fetch_Takehome_Assesment
# Health Check Monitor

## Overview
This Health Check Monitor is a Python application designed to periodically check the health of HTTP endpoints specified in a YAML configuration file. The application tests each endpoint every 15 seconds, logging the availability percentage of each URL domain over time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.8 or later
- pip for managing Python packages

### Installation

Follow these steps to set up your development environment:

1. **Clone the repository**
   ```
   git clone https://github.com/JayanthVishalReddy/Fetch_Takehome_Assignment.git
```
    cd health-check-monitor
```
2.	**Install the necessary Python packages** 
```
   python health_monitor.py /path/to/your/config.yaml
```
3. **Configuration**

      Create a YAML configuration file following the format described in sample-config.yaml. This file should list the endpoints you want to monitor.

4. **Usage**

To run the application, use the following command:
```
   python health_monitor.py /path/to/your/config.yaml
```
Replace /path/to/your/config.yaml with the path to your configuration file.
5. **Running the Tests**
## Running the Automated Tests

### Prerequisites
   Ensure you have all dependencies installed:
```
pip install -r requirements.txt
```
Running the Tests

   Execute the automated tests by running the following command in the project directory:
```
pytest
```
**What the Tests Cover**

  •	**Endpoint Accessibility**: Verifies that all endpoints are accessible and return expected status codes.


  •	**Response Time**: Checks that the response times for each endpoint are below the defined thresholds. 


  •	**Availability Calculation**: Validates that the availability percentage calculations are accurate. 



**Interpreting Test Results**

A test is considered passing if it meets all assertions without exceptions. Failing tests will output errors and stack traces relevant to the assertion failures.

**Troubleshooting**

If tests fail:

•	Check if all services and endpoints are up and running.


•	Ensure network configurations allow HTTP requests to the tested endpoints.


•	Verify environment variables and other configurations are correctly set up according to the project requirements.

### Built With

•	Python - The programming language used.


•	Requests - Used to make HTTP requests.


•	PyYAML - Used for YAML file parsing.

## Authors

- Jayanth Vishal Reddy Godi - Initial work - [JayanthVishalReddy](https://github.com/JayanthVishalReddy)

## Acknowledgments

- Hat tip to the developers of the `requests` Python library for making HTTP requests much easier.
- Inspiration from [HealthChecks.io](https://healthchecks.io) for robust monitoring solutions.
- Thanks to all open-source contributors whose tools and libraries made this project possible.
- Special thanks to [Python's official documentation](https://docs.python.org/3/) for being an invaluable resource.
- Gratitude to **Dakota Favors** at Fetch company who provided this opportunity to showcase my skills.

## Contact

For any queries, you can reach out to jayanthvishalreddy.godi@sjsu.edu.


