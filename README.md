# Binance Futures Testnet Trading Bot

## Overview

This project implements a **Python-based CLI trading bot** that
interacts with the **Binance Futures Testnet (USDT‑M)**.\
The application demonstrates a clean modular architecture, API
interaction, structured logging, and proper error handling.

The bot allows users to place **Market** and **Limit** orders using
Binance Futures Testnet APIs through a command‑line interface.

------------------------------------------------------------------------

## Key Features

-   Place **Market Orders**
-   Place **Limit Orders**
-   Supports **BUY** and **SELL**
-   CLI‑based interaction
-   Modular code structure
-   Input validation before order execution
-   Centralized logging system
-   Exception handling for API errors and invalid inputs

------------------------------------------------------------------------

## System Architecture

The application follows a **layered modular design**:

1.  **CLI Layer**
    -   Parses user input from the command line
    -   Validates arguments
    -   Triggers order execution
2.  **Validation Layer**
    -   Ensures valid order parameters
    -   Prevents invalid API requests
3.  **Order Execution Layer**
    -   Handles order creation logic
    -   Sends requests to Binance Futures API
4.  **Client Layer**
    -   Responsible for establishing the Binance API connection
5.  **Logging Layer**
    -   Records API requests, responses, and errors for debugging and
        traceability

------------------------------------------------------------------------

## Project Structure

    trading_bot/
    │
    ├── bot/
    │   ├── __init__.py
    │   ├── client.py
    │   ├── orders.py
    │   ├── validators.py
    │   ├── logging_config.py
    │   └── cli.py
    │
    ├── logs/
    │   └── trading_bot.log
    │
    ├── requirements.txt
    └── README.md

### Module Responsibilities

  File                Responsibility
  ------------------- ---------------------------------------
  client.py           Initializes Binance Futures client
  orders.py           Contains order placement functions
  validators.py       Validates CLI input parameters
  logging_config.py   Configures application logging
  cli.py              CLI entry point for executing the bot

------------------------------------------------------------------------

## CLI Usage

### Market Order

    python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order

    python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000

------------------------------------------------------------------------

## Example CLI Output

    Order Summary
    -------------
    Symbol: BTCUSDT
    Side: BUY
    Order Type: MARKET
    Quantity: 0.01

    Order Result
    -------------
    Order ID: 12345678
    Status: FILLED

------------------------------------------------------------------------

## Logging

All application events are logged to:

    logs/trading_bot.log

Logged events include:

-   Order request payload
-   API responses
-   Errors and exceptions
-   Order execution results

This helps trace the full lifecycle of a trading request.

------------------------------------------------------------------------

## Error Handling

The application handles the following error scenarios:

-   Invalid CLI inputs
-   Incorrect order parameters
-   Binance API errors
-   Network issues during API calls

All errors are logged and presented with clear CLI messages.

------------------------------------------------------------------------

## Assumptions

-   Orders are executed on **Binance Futures Testnet**
-   API credentials are stored securely using environment variables
-   Quantity and price follow Binance Futures trading rules

------------------------------------------------------------------------



## Conclusion

This project demonstrates a **structured Python trading bot**
implementation using Binance Futures Testnet APIs.\
The design focuses on maintainability, modularity, and reliability while
providing a simple CLI interface for order execution.
