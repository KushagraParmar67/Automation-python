# Automation-python
## Prerequisites

1. Python 3.7 or later.

## Installation

1. Clone this repository

2. Install requirements
```
pip install -r requirements.txt
```

3. Create a .env file in the root of this project with the following defined
```
SF_DFS_USERNAME=
SF_DFS_PASSWORD=
SF_LOGIN_URL=https://sunrun--majstg.sandbox.my.salesforce.com
SF_HOME_URL=https://sunrun--majstg.sandbox.my.salesforce.com/home/home.jsp
SF_CUSTOMER_NAME="Test Name" # Customer full Name
SF_CUSTOMER_LANGUAGE="Language" # Spanish or English 
```


## Scripts

### Create Retrofit Proposals

- The following script wil convert your lead to an opportunity.

```
$ python Lead_to_Opportunity.py
```

