# Complete Guide to Using the FundamentalVision Application

Welcome to the complete guide for using the FundamentalVision application, a tool for fundamental analysis of stocks on Brazil's B3 stock exchange. This guide will walk you through the installation, configuration, and usage of the application.

## Index

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Initial Configuration](#initial-configuration)
4. [Using the Application](#using-the-application)
5. [Features](#features)
6. [Testing](#testing)
7. [Contribution](#contribution)
8. [License](#license)
9. [Contact](#contact)

## Installation

To install FundamentalVision, use pip:

```bash
pip install fundamentalvision
```

### Dependencies

The package requires the following libraries:

- pandas
- requests
- beautifulsoup4
- streamlit
- plotly
- fundamentus

These dependencies will be installed automatically when you install FundamentalVision.

## Project Structure

The project is structured as follows:

```
fundamentalvision/
│
├── fundamentalvision/        # Diretório do código fonte
│   ├── __init__.py           # Inicializador do pacote
│   └── acoes.py              # Obter dados de Ações
│   └── dashboard.py          # Renderizar os dados com Streamlit
│   └── data_handler.py       # Configuração do Dataframe
│   └── app.py  # Código principal
│
├── tests/                    # Diretório de testes
│   ├── __init__.py
│   └── test_acao.py          # Testes para o módulo Acao
│   └── test_dashboard.py     # Testes para o módulo Dashboard
│   └── test_data_handler.py  # Testes para o DataHandler 
│   └── test_app.py           # Testes para o App
│
├── LICENCE                   # Licenca do Projeto
├── README.md                 # Documentação do projeto
├── setup.py                  # Script de configuração para distribuição
└── requirements.txt          # Dependências do projeto
```

## Initial Configuration

Before running the application, you may need to configure the locale to ensure data is displayed correctly:

```python
import locale

# Set locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
```

## Using the Application

To use FundamentalVision, follow the example below:

```python
import locale
import pandas as pd
import streamlit as st
from fundamentalvision.acoes import Acao
from fundamentalvision.dashboard import Dashboard
import fundamentus

# Set locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Retrieve stock data
actions = fundamentus.get_resultado()

# Create and display the dashboard
dashboard = Dashboard(actions)
dashboard.exibir_dashboard()
```

## Features

- **Load Fundamental Data**: Loads financial information for a specific stock.
- **Retrieve Dividends**: Retrieves information on dividends paid by the stock.
- **Get Details**: Obtains additional details about the stock.
- **Track Price Fluctuations**: Collects data on stock price fluctuations.
- **Interactive Visualization**: Displays interactive charts and tables using Streamlit and Plotly.

## Testing

FundamentalVision includes automated tests using pytest. To run the tests, use the following command:

```bash
pytest
```

## Contribution

Contributions are welcome! Feel free to open issues or pull requests. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the remote repository (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For questions or suggestions, contact:

**Author:** Joel Ferreira  
**Email:** heannareis@gmail.com

---

### Project Summary (English)

**FundamentalVision** is a tool designed for fundamental stock analysis on Brazil’s B3 stock exchange. It retrieves and processes financial data, providing insights into company performance. The application allows users to visualize financial metrics interactively using Streamlit and Plotly. 

Key features include:
- **Stock data retrieval** from Fundamentus
- **Dividend tracking**
- **Stock price fluctuation analysis**
- **Interactive dashboards** for financial analysis
- **Automated testing** with pytest

The project is open-source and welcomes contributions from the community.