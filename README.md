# Github Issues Tracker

This application tracks changes in the issues section of a specific Github repository and sends you an email notification when a new issue is created.

## Requirements

- Python 3.x
- `requests` and `json` modules
- `smtplib` and `email` modules

## Installation

1. Clone or download this repository.
2. Open the `tracker.py` file and fill in your Github API access token and email information.
3. To run the application, follow these steps:

- Open a terminal or command prompt and navigate to the directory where the application is located.
- Run the command `python tracker.py`.
- The application will connect to the Github API and check for changes in the issues section at regular intervals.
- If a new issue is created, an email notification will be sent.

## Usage

When the application is running, changes in the issues section of a specific Github repository are checked at regular intervals. If a new issue is created, an email notification is sent. Gmail is used to send the email, and the sender email address and password should be specified in the `tracker.py` file.

To use the application, you need to provide a valid Github API access token in the `tracker.py` file. You also need to provide your Gmail account information in the `tracker.py` file to send the email notifications. If your Gmail account uses two-factor authentication, you will need to create an application-specific password to allow the application to access your account.

## License

This application is released under the GNU General Public License v3.0. For more information, please see the `LICENSE` file.
