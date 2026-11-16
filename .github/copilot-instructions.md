# Copilot instructions

## Repository structure

This repository contains independent course exercises in `tehtavat/viikko1` through `tehtavat/viikko6`; there is no root application, shared Python environment, or repository-wide test command. Most exercise projects have their own `pyproject.toml` and `uv.lock`. Run `uv` commands from the relevant project directory and check that project's manifest for its dependencies and test runner.

Most Python projects place implementation and tests under `src/`. Pytest-based projects commonly use `unittest.TestCase` and `*_test.py` test filenames. The week 3 web applications are separate Flask projects.

## Build, test, and lint

For a project with pytest in its development dependencies, run from that project directory:

```sh
uv sync
uv run pytest
uv run pytest src/tests/example_test.py::TestExample::test_case
```

Replace the example test node with the selected file, class, and method. The `uv-web` project declares a build backend; from `tehtavat/viikko2/uv-web`, build with `uv build`.

Robot Framework projects:

- `tehtavat/viikko3/hello-robot`: `uv run robot src/tests`. Select one test with `uv run robot --test "Increase Counter Once" src/tests/increase_counter.robot`.
- `tehtavat/viikko3/login`: from `tehtavat/viikko3/login`, start the Flask app with `uv run python src/index.py`. It listens on port `5001`. Keep it running in one terminal while running `uv run robot src/tests` in another. Select one test with `uv run robot --test "Login With Correct Credentials" src/tests/login.robot`. Browser tests default to headed Chromium; use `--variable HEADLESS:true` for non-interactive execution.
- `tehtavat/viikko3/webcounter`: CI runs `uv sync`, `uv run rfbrowser install --with-deps chromium`, then `bash run_robot_tests.sh`. The script starts its own Flask app and runs its Robot suite.

If a Browser-based Robot suite cannot find Chromium, install it with `uv run rfbrowser install --with-deps chromium`.

Linting is configured for week 2 only. From the repository root, run:

```sh
uv run --project tehtavat/viikko2/nhl-reader pre-commit run --config tehtavat/viikko2/.pre-commit-config.yaml --all-files
```

The only checked-in GitHub Actions workflow is `tehtavat/viikko3/webcounter/.github/workflows/main.yaml`; it runs the webcounter Robot workflow with a PostgreSQL service.

## Week 3 login application

`src/index.py` starts the Flask application; `src/app.py` maps HTTP routes to templates and delegates account operations to `src/services/user_service.py`. The service uses `src/repositories/user_repository.py` for user lookup and persistence. User registration validation is implemented by `UserService.validate` in `src/services/user_service.py`; `create_user` calls it before creating the user. Registration failures are handled by the route and shown as flashed messages.

The Robot suites are under `src/tests`. `resource.robot` shares Browser setup and page assertions; `AppLibrary.py` provides test setup actions, including resetting application state through the test reset endpoint. The app must be running on port `5001` while these suites execute because their browser pages and test setup requests target `localhost:5001`.

## Project-specific conventions

- Keep changes within the relevant exercise; projects have independent dependencies and may use different test frameworks.
- In the week 3 Flask applications, keep HTTP routing, business validation, and repository access in their existing layers rather than moving account rules into templates or route handlers.
- Robot suites share resource keywords and library setup. Extend these existing resources when adding common browser behavior instead of repeating browser initialization in each suite.
