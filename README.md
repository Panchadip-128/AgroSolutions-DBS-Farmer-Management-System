# Farm Management System (FMS)
## Overview
The Farm Management System (FMS) is a web-based application designed to manage farmer data, farming products, and associated records. It provides user authentication, product management, farmer details management, and dynamic SQL query execution. The system aims to enhance farming-related operations by offering a seamless interface for data handling and insights.

## Features
1. User Authentication
Login Page: Users can securely log in using their email address and password.

Signup Page: New users can register by providing their username, email address, and password.

Ensures secure access to the system.

2. Agro Products Management
View a list of available agro products with details such as:

Product Name

Price

Description

Owner Name

Owner Email

Products can be added through the "Add Agro Products" page by filling out:

Farmer Name

Farmer Email

Product Name

Product Description

Product Price

Users can purchase products directly via the "Purchase" button.

3. Farmer Details Management
View detailed information about registered farmers, including:

Farmer Name

Aadhar Number

Age

Gender

Phone Number

Address

Farming Type

Perform actions on farmer records:

Edit: Update farmer details.

Delete: Remove farmer records.

Add Agro Product: Link agro products to specific farmers.

4. Add Agro Products
Allows users to add new farming products with detailed information such as:

Farmer Name

Farmer Email

Product Name

Product Description

Price

5. Custom SQL Queries
Execute predefined SQL queries to retrieve specific data about farmers and farming products.

Examples include:

Farmers with Age Above 50

Farmers Registered in the Last 30 Days

Top 5 Oldest Farmers

Gender Distribution of Farmers

Results are displayed dynamically in a tabular format. and any sql queries can be inserted and performed likewise


Backend Framework: Flask (Python)

Database: SQL-based database for storing farmer and product information.

Frontend: HTML, CSS, JavaScript for user interface design.

Hosting: Localhost (127.0.0.1:5000) during development.

How to Run
Clone the repository from your version control system.

Install required dependencies 


pip install flask sqlalchemy

Set up the database schema and populate it with sample data.

Run the Flask server using:


python app.py
Access the application via http://127.0.0.1:5000.

![fms1](https://github.com/user-attachments/assets/8eaa3838-7047-458f-96fb-a9de823408ce)
![fms2](https://github.com/user-attachments/assets/3712089b-ccd1-4691-8f14-2bf88261c168)
![fms3](https://github.com/user-attachments/assets/091aa8fe-d61b-4186-b2d9-d39f15487057)
![fms4](https://github.com/user-attachments/assets/4ec5db44-15bd-45d8-b34d-551c254f1780)
![fms5](https://github.com/user-attachments/assets/4ef894ef-8d0f-4cd6-a337-5ce0d3fbf228)
![fms7](https://github.com/user-attachments/assets/fd480455-82b5-4bd6-b0dd-84ca20fad06d)
![fms8](https://github.com/user-attachments/assets/ddefb1ad-a1df-4ded-896e-38d4f441aaf9)
![fms9](https://github.com/user-attachments/assets/f4e2134b-2882-412e-be3b-c1bef1910c1f)
![fms 10](https://github.com/user-attachments/assets/72248e34-aa0f-4095-8278-64ee7dffe09b)
![fms 11](https://github.com/user-attachments/assets/284fc71b-d3a0-4b56-a3ac-7b893fe83161)
![fms12](https://github.com/user-attachments/assets/1b8dfbb3-bfd2-4feb-b6fa-836b76c6549f)
![fms13](https://github.com/user-attachments/assets/0b8e5c77-609d-41b8-9552-7d7982deb1c3)
![fms14](https://github.com/user-attachments/assets/319e095f-2b62-4606-9a64-c6d776b9ee59)
![fms15](https://github.com/user-attachments/assets/f6a718df-1344-48b3-8019-ba95aed5546c)
![fms16](https://github.com/user-attachments/assets/a2832e59-4776-409f-b733-8f07535118cd)
![fms17](https://github.com/user-attachments/assets/3ec6ac0e-cbfd-4e50-9398-798d532c8388)



