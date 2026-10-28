### JHL Custom

Judibela Holdings Limited ERPNext customizations

### Installation

The repository root contains a small `setup.py` compatibility entry point for
Bench versions that still require one. The Python app package and its project
metadata remain in `jhl_custom/`.

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/Mumbela/JHL-ERPNEXT-Custom-App.git --branch main
bench install-app jhl_custom
```

### Updating during development

After pushing changes to the configured branch, update the app checkout and
apply any database or DocType changes with:

```bash
cd $PATH_TO_YOUR_BENCH/apps/JHL-ERPNEXT-Custom-App
git pull --ff-only
cd ../..
bench migrate
```

Keep the app version in `jhl_custom/__init__.py`; the root `setup.py` reads it
when Bench installs the package. Declare any runtime Python dependencies in
the root `setup.py` so Bench installs them with the app.

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/JHL-ERPNEXT-Custom-App/jhl_custom
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
