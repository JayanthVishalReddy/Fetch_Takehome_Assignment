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

      Create a YAML configuration file following the format described in endpoints.yml. This file should list the endpoints you want to monitor.

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

 ### My Understandings: 

•	Input Parsing: The program reads a YAML configuration file that defines the properties of each HTTP endpoint, including the endpoint’s name, URL, HTTP method, headers, and body content.

•	Endpoint Testing: Every 15 seconds, the program sends requests to the endpoints. An endpoint is considered “UP” if:

•	The HTTP response status code is between 200 and 299.

•	The response time is less than 500 milliseconds.

If either condition is not met, the endpoint is considered “DOWN.”

•	Logging Results: After each testing cycle, the program calculates the availability of each domain by comparing the number of “UP” results to the total number of tests performed for that domain. This percentage is logged to the console.

### Doubts Arised:

During the testing phase, I have  encountered a situation where it calculated availability percentages for monitored HTTP endpoints differ from expected values. For example:

 **Expected Output after Test Cycle #1:**

•	fetch.com has 33% availability percentage

•	www.fetchrewards.com has 100% availability percentage

 **Observed Output:**

•	fetch.com has 67% availability percentage

•	www.fetchrewards.com has 100% availability percentage

### Steps Taken to Clarify the Doubt

1.	Manual Testing: Conducted manual tests on the endpoints using tools like curl or requests in Python to independently verify their usual response codes and response times under similar conditions.

2.	Debugging: Added detailed debugging statements throughout the health check script to log each step’s output, such as connection attempts, received response codes, and response timings.

3.	Review Configuration: Re-examined the YAML configuration file to ensure that all endpoints are defined correctly and that no settings were altered unexpectedly.

4.	Network Checks: Checked the network conditions during test runs to rule out issues related to network latency or unreliability.

5.	Code Review: Conducted a thorough review of the script to ensure that all logic related to HTTP request handling, response evaluation, and availability calculation was functioning as intended.


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


