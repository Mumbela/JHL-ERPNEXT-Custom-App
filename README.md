### JHL Custom

Judibela Holdings Limited ERPNext customizations

### Installation

The repository root contains the packaging metadata used by Bench and `uv`,
plus a small `setup.py` compatibility entry point for older Bench versions.
The Python app source is in the root `jhl_custom/` package, matching the layout
Bench expects when it resolves the installed app version.

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
cd $PATH_TO_YOUR_BENCH/apps/jhl_custom
git pull --ff-only
cd ../..
bench migrate
```

Keep the app version in `jhl_custom/__init__.py`; both packaging entry points
read it when Bench installs the package. Declare runtime Python dependencies
in the root `pyproject.toml` so Bench installs them with the app.

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/jhl_custom
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
