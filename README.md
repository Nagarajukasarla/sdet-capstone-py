# SDET Capstone Project - WordPress Website Testing

## Overview

This project is an automated testing suite for the WordPress website using Selenium WebDriver and the Behave BDD (Behavior-Driven Development) framework. It demonstrates best practices in test automation, including the Page Object Model pattern, and covers key functionalities such as page navigation, theme browsing, and search capabilities.

## Features Tested

- **Page Title Verification**: Ensures the WordPress homepage loads correctly with the expected title.
- **Navigation to Themes**: Tests mouse hover and click actions to navigate to the themes section.
- **Theme Search**: Verifies the ability to search for specific themes (e.g., "astra") and displays results.

## Project Structure

```
sdet-capstone/
├── README.md
├── requirements.txt
├── drivers/
│   └── driver_manager.py
├── features/
│   ├── environment.py
│   ├── wordpress.feature
│   └── steps/
│       └── wordpress_steps.py
└── pages/
    ├── wordpress_page.py
    └── themes_page.py
```

- **drivers/**: Contains the driver management module for setting up Selenium WebDriver.
- **features/**: Holds BDD feature files and step definitions.
  - `environment.py`: Behave hooks for setup and teardown.
  - `wordpress.feature`: Gherkin feature file defining test scenarios.
  - `steps/`: Step definitions implementing the feature steps.
- **pages/**: Page Object Model classes for encapsulating web page interactions.
- **requirements.txt**: Python dependencies.

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- Internet connection (for downloading WebDriver and accessing WordPress site)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sdet-capstone
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   This will install:
   - `selenium`: For browser automation
   - `behave`: BDD framework for Python
   - `webdriver-manager`: Automatic WebDriver management

## Running the Tests

Execute all tests using Behave:

```
behave
```

To run specific features or scenarios:

```
behave features/wordpress.feature
```

For verbose output:

```
behave -v
```

## Test Scenarios

### Scenario 1: Verify title of WordPress page
- Launches the WordPress website
- Verifies the page title contains "WordPress.org"

### Scenario 2: Navigate to Themes
- Launches the WordPress website
- Hovers over the "Extend" menu
- Clicks on "Themes"
- Verifies the themes page is displayed

### Scenario 3: Search for a theme
- Launches the WordPress website
- Navigates to the themes page
- Searches for the "astra" theme
- Verifies themes are displayed in the results

## Configuration

The project uses Chrome WebDriver with the following options:
- `--start-maximized`: Opens the browser in maximized mode

WebDriver is automatically managed and downloaded using `webdriver-manager`.

## Page Object Model

The project implements the Page Object Model pattern:

- **WordPressPage**: Handles interactions with the main WordPress page, including navigation to themes.
- **ThemesPage**: Manages theme search functionality.

## Troubleshooting

- **WebDriver issues**: Ensure Chrome browser is up to date. The `webdriver-manager` should handle driver downloads automatically.
- **Test failures**: Check internet connection and WordPress site availability.
- **Import errors**: Verify all dependencies are installed via `pip install -r requirements.txt`.

## Technologies Used

- **Python**: Programming language
- **Selenium WebDriver**: Browser automation
- **Behave**: BDD testing framework
- **ChromeDriver**: Browser driver
- **WebDriver Manager**: Automatic driver management

## License

This project is for educational purposes as part of an SDET capstone project.