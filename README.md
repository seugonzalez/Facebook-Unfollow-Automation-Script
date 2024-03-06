# Facebook Unfollow Automation Script

## Description
This Python script automates the process of unfollow pages on Facebook. Utilizing the Selenium WebDriver, it systematically navigates through a user's liked pages and 'unlikes' each one. This tool is especially useful for users looking to declutter their Facebook profile and manage their likes more effectively.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- A Facebook account

## Setup
1. Ensure Python is installed on your system.
2. Install Selenium WebDriver:
   ```bash
   pip install selenium
   ```
3. Download the appropriate WebDriver for your browser (e.g., ChromeDriver, EdgeDriver) and ensure it's in your PATH.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/facebook-unlike-script.git
   ```
2. Navigate to the cloned directory.
3. Open the script `unlike_pages.py` in a text editor.
4. Update the script with your Facebook login credentials and the path to your WebDriver.
5. Run the script:
   ```bash
   python unlike_pages.py
   ```
6. The script will start a browser session and begin the unfollow process.

## Disclaimer
This script is for educational purposes only. Automated actions on Facebook should comply with Facebook's terms of service. The author is not responsible for any actions taken against your Facebook account as a result of using this script.

## Contributing
Contributions to enhance this script are welcome. Please fork the repository and create a pull request with your improvements.

## License
[MIT License](LICENSE)
