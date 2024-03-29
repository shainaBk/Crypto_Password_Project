# Secure Password Storage Project TP5 PART I

## Team Members

- Shaïna BAKILI MUMBUKU
- Yassin BAKRIM
- GALAI Nour El Houda

## Project Overview

This project addresses the secure storage of user passwords, focusing on mitigating common threats such as mass and targeted password cracking, as well as database breaches. Utilizing modern cryptographic techniques, it aims to ensure the integrity and confidentiality of user passwords.

## Problem Statement

The digital security domain continually faces the challenge of securely storing user passwords. This project explores several key questions related to this challenge:

1. **Password Entropy**: Determining the minimum password length for case-insensitive alphanumeric characters to achieve 64 bits of entropy.
2. **Security Against Threats**: Protecting passwords against mass cracking, targeted attacks, and database breaches.
3. **Hashing Algorithm Selection**: Identifying a suitable slow, memory-hard hashing function to deter brute-force attacks while maintaining user convenience.
4. **Data Breach Mitigation**: Examining encryption's role in securing user passwords against offline attacks following a database breach.

## Implementation

### Environment Setup

- **Hashing**: `bcrypt` is used for hashing passwords, providing built-in salt for protection against rainbow table attacks and being computationally intensive to counter brute-force attempts.
- **Password Strength**: A mathematical approach based on entropy ensures passwords meet minimum complexity requirements.
- **Configuration**: Uses environment variables from a `.env` file, including a global `PEPPER`, to enhance security.

### Key Features

- **User Registration & Login**: Supports secure account creation and authentication.
- **Rate Limiting & Account Lockout**: Implements defenses against online brute-force attacks.
- **Pepper & Environmental Variables**: Adds an additional layer of security to the hashing process.

### Project Structure

- `Secure.py`: Contains the core logic for password handling.
- `CLI.py`: A command-line interface for user interaction.
- `users.csv`: A simple storage solution for user data.

### Configuration & Setup

#### `.env` File Setup

The `PEPPER` variable is crucial for password security and must be set in your `.env` file before running the application:

1. Create a `.env` file in the project's root directory.
2. Add your `PEPPER` value:

```
PEPPER=yourSecretPepperHere
```

**Important**: The `PEPPER` is integral to the security of the hashed passwords. Once set, it should not be changed to ensure the integrity of existing password hashes.

## Security Considerations

This project employs several strategies to enhance password security, including the use of a `PEPPER`, selecting `bcrypt` for its secure hashing capabilities, and implementing rate limiting and account lockout mechanisms.



