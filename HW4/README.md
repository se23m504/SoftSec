# Authentication

## Project structure

- `basic/`: Contains the implementation for basic form authentication.
- `digest/`: Contains the implementation for HTTP digest authentication.
- `google/`: Contains the implementation for Google OAuth authentication.

## Prerequisites

- `python >= 3.11`
- `python-venv`

In Kali Linux, you can run `apt install python3.11-venv` as the root user.

## Usage

### Basic

1. Open the terminal.

2. Navigate to the project directory:

   ```bash
   cd SoftSec/HW4/basic
   ```

3. Run the application:

   ```bash
   bash run.sh
   ```

### Digest and Google


1. Open the terminal.

2. Navigate to the project directory:

   ```bash
   cd SoftSec/HW4/basic
   ```

3. Configure the `.env`:

   ```bash
   cp .env.dev .env
   ```

3. Run the application:

   ```bash
   bash run.sh
   ```

Note: For the Google OAuth authentication, you will need to create a Google Client ID and Client Secret. Refer to the Google Developer Console documentation on how to create these credentials.
