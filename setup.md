📱 iOS UI Automation Tests (Appium + Python + Pytest)

This repository contains end-to-end UI automation tests for the UIKitCatalog iOS sample application, using:

Appium

Python

Pytest

Page Object Model (POM)

The goal is to demonstrate clean, maintainable mobile automation following modern best practices.

🚀 A. Setup: Appium + macOS Environment (iOS Automation)

These steps prepare your machine for iOS Appium tests.

1. Install Appium
npm install -g appium
appium -v

2. Install Appium Inspector (optional but highly useful)
brew install --cask appium-inspector

3. Install the iOS Appium driver (XCUITest)
appium driver install xcuitest
appium driver list

4. Accept Xcode license
sudo xcodebuild -license accept

5. Install Xcode Command Line Tools
xcode-select --install


Ensure:
Xcode → Settings → Locations → Command Line Tools
is properly set.

6. Install required utilities (Appium dependencies)
brew install carthage
brew install ios-deploy
brew install ffmpeg

7. Install simulator utilities (optional but recommended)
brew tap wix/brew
brew install applesimutils

8. Verify iOS automation environment
appium driver doctor xcuitest


Everything should be GREEN OK.

🐍 B. Python + Pytest Setup
1. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

2. Install Python dependencies
pip install -r requirements.txt


If you are installing manually:

pip install pytest Appium-Python-Client

📦 C. Project Structure
.
├── app/
│   └── UIKitCatalog.app
│
├── pages/
│   ├── main_page.py
│   └── activity_monitors_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_main_navigation.py
│   └── test_activity_indicators.py
│
├── utils/
│   └── capabilities.py
│
├── README.md
└── requirements.txt

📱 D. UIKitCatalog Sample App

This project uses Apple’s UI sample app: UIKitCatalog.app

1. Clone the sample project
git clone https://github.com/appium/ios-uicatalog.git

2. Build the iOS simulator app
cd ios-uicatalog
npm install
npm run build:uicatalog:simulator


You’ll get:

UIKitCatalog.app

3. Place the built app into your project
mkdir app
mv ios-uicatalog/UIKitCatalog/build/Build/Products/Release-iphonesimulator/UIKitCatalog.app app/


The folder must remain named exactly:

UIKitCatalog.app

🧪 E. Running the Tests
1. Start Appium (in a separate terminal)
appium

2. Run the tests
pytest -v


The simulator will:

Boot automatically

Launch the UIKitCatalog app

Run all navigation tests

🧱 F. Notes on the Test Structure

Tests follow Page Object Model

Fixtures initialize the driver only once per test

Navigation and UI element access live inside pages/

Tests are grouped by feature:

test_main_navigation.py

test_activity_indicators.py