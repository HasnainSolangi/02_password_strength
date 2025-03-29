# 🔐 Password Generator & Strength Checker - Project 02 (Python)

This Python application, built using Streamlit, provides a user-friendly interface to generate strong passwords and check the strength of existing passwords.

## Features

-   **Password Strength Check:**
    -      Evaluates password strength based on length, uppercase and lowercase letters, digits, and special characters.
    -      Provides feedback on how to improve weak passwords.
    -      Rejects common weak passwords (blacklist).
    -      Displays clear strength indicators (Strong, Moderate, Weak).
-   **Password Generator:**
    -      Generates secure passwords with customizable length.
    -      Includes uppercase and lowercase letters, digits, and special characters.
-   **User-Friendly Interface:**
    -      Intuitive Streamlit web application.
    -      Clear headings and feedback messages.
    -   Display of generated and entered passwords.

## Important Security Information

**Please be aware that even with strong passwords generated by this tool, your online security is not guaranteed.**

* **Password Managers:** We strongly recommend using a reputable password manager to securely store and manage your generated passwords. This is the safest way to handle complex, unique passwords for each of your online accounts.
* **Website Requirements:** Always check the specific password requirements of the websites or services you're using. Some sites may have unique restrictions or requirements that this generator does not account for.
* **Phishing and Other Threats:** Strong passwords protect against brute-force attacks, but they do NOT protect against phishing, malware, or other social engineering tactics. Be vigilant about suspicious emails, links, and websites.
* **Entropy and Advanced Security:** For extremely high-security applications, consider using a cryptographically secure random number generator (CSPRNG) and consulting security best practices. This generator uses the standard python random library, that is usually sufficient, but not as cryptographically secure as other libraries.
* **No Exclusion lists for charaters:** Some websites will refuse passwords that include some special characters.

**Your online security is a shared responsibility. Use strong passwords, but also practice safe browsing habits and be aware of potential threats.**

## Requirements

-   Python 3.6+
-   Streamlit (`pip install streamlit`)

## How to Run

1.  Clone the repository:

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

2.  Install the required packages:

    ```bash
    pip install streamlit
    ```

3.  Run the Streamlit app:

    ```bash
    streamlit run password_strength.py
    ```

    (Replace `password_strength.py` with the name of your Python file if it's different.)

4.  Open your browser to view the application.

## Code Explanation

-   **`generate_random_password(length=12)`:**
    -      Generates a random password of the specified length.
    -      Uses `string.ascii_letters`, `string.digits`, and `string.punctuation` to create a character set.
-   **`check_password_strength(password)`:**
    -      Checks the password against security criteria.
    -      Assigns a score based on password complexity.
    -      Provides feedback on how to improve weak passwords.
    -   Checks against a common password blacklist.
    -   Applies custom weights to uppercase and lowercase characters.
-   **Streamlit UI:**
    -      Uses Streamlit components (`st.title`, `st.header`, `st.text_input`, `st.slider`, `st.button`, `st.code`, `st.success`, `st.warning`, `st.error`, `st.write`) to create the user interface.

## Example Usage

1.  **Check Password Strength:**
    -      Enter a password in the "Check Your Password Strength" text input.
    -      The app will display the password, its strength, and any feedback.

2.  **Generate Password:**
    -      Use the slider to select the desired password length.
    -      Click the "Generate Secure Password" button.
    -      The app will display the generated password, its strength, and any feedback.
