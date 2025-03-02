# App-Switch: Close Programs You Don’t Want
App-Switch lets you easily close apps that are running on your PC. It searches for the app you want to close and shuts it down. If the app tries to start up again, App-Switch will keep making sure it stays closed—unless you turn it off. *(Works on Windows with Python 3.11.9)*

## How to Use (No Python Needed)
If you don’t have Python or aren’t sure what it is, no problem! Just follow these 3 easy steps:

### 1️⃣ Step 1: Download
- Go to the **Releases** section and download the `.zip` file. 📥

### 2️⃣ Step 2: Extract
- Go to your **Downloads** folder.
Right-click the `.zip` file and choose **Extract All**. Pres **Enter** and wait for it to unzip. 📂

### 3️⃣ Step 3: Run the Program
 - Open the folder you just extracted. 📂

 - Scroll to the bottom and double-click `app_switch` to run it. ⚙️

*(If there’s another folder with the same name inside, open that first to find `app_switch`.)*

⚠️ **Note**: You might see a warning since the app will close other programs.

## 🐍 How to Use (With Python Installed)

If you have Python 3.11.9 or higher installed, follow these steps to get App-Switch running:

### 1️⃣ Step 1: Download the Files
- Click the green **Code** button and download the `.zip` file. 📥

### 2️⃣ Step 2: Extract the Files
- Go to your **Downloads** folder.
- Right-click the `.zip` file and choose **"Extract All"**. Press **Enter** and wait for it to unzip. 📂

### 3️⃣ Step 3: Install Dependencies
- Open a terminal or **Command Prompt** in the folder where you extracted the files. 💻
- Run this command to install the required libraries:
  ```bash
  pip install -r requirements.txt
  ```
  
  ### 4️⃣ Step 4: Run the Program
- In the same terminal or Command Prompt window, run the following command to start App-Switch:
  ```bash
  python app_switch.py
  ```
⚠️ **Note**: If you get any errors, make sure you’re using Python 3.11.9 by running `python --version`.
