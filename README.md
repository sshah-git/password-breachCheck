# password-breachCheck
🔐 Password Breach Checker

A simple and secure web application that checks whether a password has been exposed in known data breaches using the k-Anonymity model from the Have I Been Pwned API.

🚀 Overview

This project allows users to safely check if their password has been compromised—without ever sending the full password over the internet.

Instead of transmitting the entire password, the app:

Hashes the password using SHA-1
Sends only the first 5 characters of the hash to the API
Compares the remaining hash locally

This ensures privacy while still leveraging a massive breach database.
