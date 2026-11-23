# Copilot instructions

## Repository structure

This repository contains independent course exercises in `tehtavat/viikko1` through `tehtavat/viikko6`; there is no root application, shared Python environment, or repository-wide test command. Most exercise projects have their own `pyproject.toml` and `uv.lock`. Run `uv` commands from the relevant project directory and check that project's manifest for its dependencies and test runner.

Most Python projects place implementation and tests under `src/`. Pytest-based projects commonly use `unittest.TestCase` and `*_test.py` test filenames. The week 3 web applications are separate Flask projects.

## Repository-wide constraints

- Run Python unit tests with `uv run pytest` from the relevant project directory; do not use bare `pytest`.
- Do not edit tests unless the task explicitly asks for test changes.
- Implement the smallest production-code change that makes the tests pass.
- In `tehtavat/viikko4/tdd-ostoskori`, do not change `src/ostos.py` or `src/tuote.py`.

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

The `verkkokauppa` project has `coverage` installed. From `tehtavat/viikko4/verkkokauppa`, measure coverage for `Kauppa` with:

```sh
uv run coverage run --source=kauppa -m pytest src/tests
uv run coverage report -m
```

## Architecture across exercises

- Each `tehtavat/viikkoN/<exercise>` directory is an independent exercise, usually with its own `pyproject.toml`, lockfile, dependencies, and test runner. There is no shared application or root test suite.
- Week 1 separates NHL data loading (`PlayerReader`) from queries (`StatisticsService`). The dependency-injection calculator passes an IO object into `Laskin`, keeping console access in `KonsoliIO`.
- Week 2's NHL reader turns API responses into `Player` objects, and `PlayerStats` performs filtering and sorting. `uv-web` is a separately buildable package.
- Week 3 contains independent Flask applications. In `login`, routes delegate account rules to services, which use repositories and entities; `webcounter` delegates counter state to its `Counter` model. Browser tests are written in Robot Framework.
- Week 4's `verkkokauppa.Kauppa` coordinates an inventory, shopping cart, bank, and reference-number generator. `tdd-ostoskori` separates products, individual purchases, and the cart; `mock-demo` demonstrates interaction tests with mocks.
- Week 5 contains independent domain exercises: `IntJoukko` implements integer-set operations, and `TennisGame` calculates tennis scores.
- Week 6's query-language exercise composes player matchers and passes them to statistics queries. The calculator separates Tkinter UI behavior from `Sovelluslogiikka`.

## Week 3 login application

`src/index.py` starts the Flask application; `src/app.py` maps HTTP routes to templates and delegates account operations to `src/services/user_service.py`. The service uses `src/repositories/user_repository.py` for user lookup and persistence. User registration validation is implemented by `UserService.validate` in `src/services/user_service.py`; `create_user` calls it before creating the user. Registration failures are handled by the route and shown as flashed messages.

The Robot suites are under `src/tests`. `resource.robot` shares Browser setup and page assertions; `AppLibrary.py` provides test setup actions, including resetting application state through the test reset endpoint. The app must be running on port `5001` while these suites execute because their browser pages and test setup requests target `localhost:5001`.

## Project-specific conventions

- Keep changes within the relevant exercise; projects have independent dependencies and may use different test frameworks.
- In the week 3 Flask applications, keep HTTP routing, business validation, and repository access in their existing layers rather than moving account rules into templates or route handlers.
- Robot suites share resource keywords and library setup. Extend these existing resources when adding common browser behavior instead of repeating browser initialization in each suite.
- In week 1, keep data loading in reader classes and query behavior in statistics services; preserve dependency injection in the calculator exercise.
- In week 4 mock-based exercises, use mocks to verify interactions and arguments rather than relying on concrete external services.
- In week 6 query-language, matchers expose `test(player)` and statistics queries consume that matcher interface.
