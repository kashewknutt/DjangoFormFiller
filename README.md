# Django Form Filler

This project is designed to demonstrate proficiency in Selenium by automating the process of filling out and submitting a Google form. It also captures a screenshot of the confirmation page.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Google Chrome browser

### Installing Required Packages

1. **Clone the Repository**

    ```bash
    git clone https://github.com/kashewknutt/DjangoFormFiller.git
    cd DjangoFormFiller
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv env
    ```

3. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Download and Set Up ChromeDriver

1. **Download ChromeDriver**

    - [Windows](https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/win64/chromedriver-win64.zip)
    - [Linux](https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip)
    - [macOS](https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/mac-x64/chromedriver-mac-x64.zip)

2. **Extract and Rename**

    Extract the downloaded zip file and rename the folder to `chromedriver`. Place this folder inside `formFiller/main/scripts/`.

    The directory structure should look like this:

    ```
    DjangoFormFiller/
    ├── formFiller/
    │   ├── main/
    │   │   ├── scripts/
    │   │   │   ├── chromedriver/
    │   │   │   │   ├── chromedriver.exe  # (or chromedriver depending on your OS)
    │   │   │   ├── form_submission.py
    ```

### Running the Form Submission Script

1. **Navigate to the Script Directory**

    ```bash
    cd formFiller/main/scripts/
    ```

2. **Run the Script**

    ```bash
    python form_submission.py
    ```

    This script will:
    - Open the provided Google form.
    - Fill in the form with sample data.
    - Submit the form.
    - Capture a screenshot of the confirmation page.
    - Save the screenshot as `confirmation_page.png`.

## Documentation

### Approach

1. **Setting Up Selenium**

    - Initialized Selenium WebDriver with the path to the ChromeDriver.
    - Opened the provided Google form URL.

2. **Filling Out the Form**

    - Located each input field using its XPATH.
    - Sent the sample data to each field.

3. **Submitting the Form**

    - Clicked the submit button.
    - Waited for the confirmation page to load.

4. **Capturing the Screenshot**

    - Captured and saved a screenshot of the confirmation page as `confirmation_page.png`.

This project demonstrates proficiency in using Selenium for web automation and form submission.
