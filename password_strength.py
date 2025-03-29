import string
import random
import streamlit as st
import re

COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "password123"]

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Very Weak Password - Avoid common passwords.", ["❌ This password is too common."]

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1 * 1.5

    if re.search(r"[a-z]", password):
        score += 1 * 1.5

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score >= 5:
        return "✅ Strong Password!", []
    else:
        if len(password) < 8:
            feedback.append("❌ Password should be at least 8 characters long.")

        if not re.search(r"[A-Z]", password):
            feedback.append("❌ Include at least one uppercase letter.")

        if not re.search(r"[a-z]", password):
            feedback.append("❌ Include at least one lowercase letter.")

        if not re.search(r"\d", password):
            feedback.append("❌ Add at least one number (0-9).")

        if not re.search(r"[!@#$%^&*]", password):
            feedback.append("❌ Include at least one special character (!@#$%^&*).")

        if score >= 3:
            return "⚠️ Moderate Password - Consider adding more security features.", feedback
        else:
            return "❌ Weak Password - Improve it using the suggestions below.", feedback

st.title("🔐 Password Generator & Strength Checker")

st.header("Check Your Password Strength")
custom_password = st.text_input("Enter your password:")

if st.button("Check Password"):
    if custom_password:
        strength, feedback = check_password_strength(custom_password)

        st.subheader("Password:")
        st.code(custom_password)

        st.subheader("Password Strength:")
        if "✅" in strength:
            st.success(strength)
        elif "⚠️" in strength:
            st.warning(strength)
        else:
            st.error(strength)

        if feedback:
            st.subheader("Feedback:")
            for message in feedback:
                st.write(message)
    else:
        st.warning("Please enter a password.")

st.header("Generate Secure Password")
length = st.slider("Password Length", min_value=8, max_value=20, value=12)

if st.button("Generate Secure Password"):
    random_password = generate_random_password(length)
    strength, feedback = check_password_strength(random_password)

    st.subheader("Generated Password:")
    st.code(random_password)

    st.subheader("Password Strength:")
    if "✅" in strength:
        st.success(strength)
    elif "⚠️" in strength:
        st.warning(strength)
    else:
        st.error(strength)

    if feedback:
        st.subheader("Feedback:")
        for message in feedback:
            st.write(message)