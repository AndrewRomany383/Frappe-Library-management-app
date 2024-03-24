### Library Management System

Library Management System

### Installation

You can install this app using the [bench](https://github.com/AndrewRomany383/Frappe-Library-management-app) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch LMSv1
bench install-app library_management
```

### Testing the APIs
```make get request for those four endpoints

http://library.localhost:8000/api/method/library_management.library_management_system.doctype.article.api.get_all_articles_by_specific_fields_by_orm

http://library.localhost:8000/api/method/library_management.library_management_system.doctype.article.api.get_all_articles_by_all_fields_by_orm

http://library.localhost:8000/api/method/library_management.library_management_system.doctype.article.api.get_all_articles_by_specific_fields_by_sql

http://library.localhost:8000/api/method/library_management.library_management_system.doctype.article.api.get_all_articles_by_all_fields_by_sql
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
