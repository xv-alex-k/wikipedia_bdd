## Simple project using Page Object model and selenium to automate https://wikipedia.org

### Installation
+ Install python
```
brew install python
```
+ Install chromedriver
```
brew install chromedriver
```
+ Install dependencies
```
pip install -r requirements.txt
```
+ Set username and password for wikipedia.org
```
├──tests/login.py
username = "your_username"
password = "your_password"
```

### Create page objects:
+ Base page 
+ Login page
+ Topic page
+ Main page
+ Search Results page

### Test cases:
+ Valid Search
+ Invalid Search
+ Successful login

### Repository tree
```
.
├── pages
│   └── base_page.py
│       └── topic_page.py
│           ├── login_page.py
│           ├── main_page.py
│           └── search_results_page.py
├── tests
│   └── test.py
├── requirements.txt
└── README.md
```