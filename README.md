
# Coding Task - REST API for Mobile App

## Overview
This task involves creating a REST API to support a mobile app similar to popular apps that identify spam numbers or allow users to find names by searching phone numbers. The API must be implemented using a language/framework of your choice, with preference for Django, Flask, or Rails. Persistence must be handled with a relational database using an ORM.

## Requirements

### Terminology and Assumptions
- **Registered Users and Contacts**: Each registered user can have zero or more personal "contacts."
- **Global Database**: Combines all registered users and their personal contacts (who may or may not be registered users).
- **UI Development**: You will develop the backend REST API endpoints. The frontend UI will be built separately.
- **Production Ready**: Write the code as if for production, focusing on performance and security.

### Data to be Stored for Each User
- Name  
- Phone Number  
- Email Address  

### Functional Specifications

#### Registration and Profile
- Users must register with at least a name, phone number, and password. Email is optional.
- Phone numbers must be unique per user.
- Users must be logged in to access any functionality (no public access).

#### Spam Reporting
- Users can mark any phone number as spam, enabling others to identify spammers via the global database. Numbers marked as spam may or may not belong to registered users.

#### Search Functionality
1. **By Name**
   - Search results display name, phone number, and spam likelihood.
   - Results prioritize names starting with the query, followed by names containing the query.

2. **By Phone Number**
   - If a registered user matches the phone number, only that result is displayed.
   - Otherwise, all entries matching the phone number completely are displayed. Multiple names can be associated with one phone number due to different users' contact books.

3. **Details Display**
   - Clicking a result displays all details, including spam likelihood.
   - Emails are shown only if the searched person is a registered user and the searcher is in their contact list.

#### Data Population
- Include a script to populate the database with random sample data for testing.

### Evaluation Criteria
- Completeness of functionality
- Correctness under testing
- Performance and scalability of APIs
- Security of APIs
- Data modeling and code structure
- Readability of code

### Submission Guidelines
- Reply to the provided email thread with your source code in a tar/zip file.
- Do not share the code publicly (e.g., GitHub).
- Exclude large folders (e.g., virtual environments).
- Include instructions for running the code.

## Additional Notes
- Ensure the API is production-ready with proper error handling, edge case coverage, and validations.
- Plagiarism is strictly prohibited. Detected cases will result in employment termination and potential blacklisting.




# Truecaller API

## Setup

```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_data
```


### Endpoints
- `POST /api/users/` - Create a new user

- `POST /api/token/` - Obtain JWT token

- `GET /api/contacts/` - List contacts (requires authentication)

- `POST /api/contacts/` - Create a new contact (requires authentication)

- `GET /api/contacts/<id>/` - Retrieve a contact (requires authentication)

- `PUT /api/contacts/<id>/report_spam/` - Report a contact as spam (requires authentication)