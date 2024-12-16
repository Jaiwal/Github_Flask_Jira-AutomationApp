
# GitHub-Jira Automation Flask Web Application

[![Screenshot-2024-12-16-at-7-15-27-PM.png](https://i.postimg.cc/SxXFm3J2/Screenshot-2024-12-16-at-7-15-27-PM.png)](https://postimg.cc/QFrnb6gh)
## Overview
This GitHub-Jira integration project involves a Flask web application hosted on an AWS EC2 instance. The application automates the creation of Jira issues based on GitHub issue comments. Specifically, when a user comments "/jira" on a GitHub issue, the web application triggers a process that utilizes GitHub webhooks, Jira API automation, and AWS EC2.

## How It Works

1. **GitHub Webhooks:**
   - The Flask web application is configured to receive GitHub webhook events.
   - GitHub issues trigger events that contain information about comments, which the application analyzes.

3. **GitHub Issue Comment Processing:**
   - When a comment is made on a GitHub issue, the application checks if it contains the "/jira" command.

5. **Jira API Automation:**
   - If the "/jira" command is detected, the application uses the Jira REST API to create a new issue on the Jira board.
   - Key details such as project, issue type, and summary are included in the API request payload.

6. **AWS EC2 Hosting:**
   - The Flask web application is hosted on an AWS EC2 instance.
   - Ensure you have launched an EC2 instance, and you can access it securely.

7. **Setup After Creating EC2 Instance:**
   - Connect to your EC2 instance securely using SSH.
   - Run these commands :
     ```bash 
        $ sudo apt-get update
        $ sudo apt-get install python3
        $ sudo apt-get install python3-pip
        $ pip install flask
        $ vim your-filename.py
        $ python3 your-filename.py
     ```
     - It will initiate the Flask application

# Troubleshooting Guide

## Problem:

Webhooks are failing, or the Flask application returns a 500 error or issue not getting created

## Possible Causes and Solutions:

1. **Webhooks Configuration:**
   - Verify GitHub webhook settings (payload URL, content type, and secret).

2. **Flask Application Logs:**
   - Check application logs for errors (commonly in `/var/log` or the app directory).

3. **EC2 Security Groups:**
   - Go to EC2 console > Security Groups.
   - Ensure Inbound Rules allow necessary ports (e.g., 80, 443 , 5000) for GitHub IPs.


 Happy coding! 🚀
