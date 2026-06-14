<div align="center">

# 💳 Validador de Tarjetas de Crédito / Credit Card Validator

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Algorithm](https://img.shields.io/badge/Algorithm-Luhn-blue?style=for-the-badge)

Valida números de tarjeta de crédito con el **algoritmo de Luhn** e identifica la empresa emisora.
Validates credit card numbers with the **Luhn algorithm** and identifies the issuing company.

</div>

---

## 📋 Descripción / Description

**🇪🇸 Español:**
Este proyecto valida números de tarjetas de crédito utilizando el estándar industrial **algoritmo de Luhn** (ISO/IEC 7812-1). Además de verificar la integridad del número, identifica la empresa emisora (Visa, Mastercard, Amex, etc.).

**🇬🇧 English:**
This project validates credit card numbers using the industry standard **Luhn algorithm** (ISO/IEC 7812-1). Beyond verifying the number's integrity, it identifies the issuing company (Visa, Mastercard, Amex, etc.).

---

## ✨ Características / Features

| Característica / Feature | Descripción / Description |
|--------------------------|---------------------------|
| 🔢 Algoritmo de Luhn | Validación checksum estándar industrial / Industry-standard checksum validation |
| 🏢 Empresas soportadas | Visa, Mastercard, Amex, Maestro, Diners, Discover, JCB, UnionPay, Euro6000 |
| 🌐 Bilingüe | Textos en español e inglés / Bilingual Spanish and English interface |
| ✅ Validación completa | Longitud (13-19 dígitos) + checksum Luhn / Length (13-19 digits) + Luhn checksum |
| 🛡️ Input seguro | Solo acepta dígitos, sin espacios ni caracteres especiales / Only accepts digits |

---

## 🏢 Tarjetas Soportadas / Supported Cards

| Empresa / Company | Prefijos / Prefixes | Longitud / Length |
|-------------------|---------------------|-------------------|
| 💚 **VISA** | `4` | 13, 16, 19 |
| 🟠 **MASTERCARD** | `51`-`55` | 16 |
| 🔵 **AMEX** | `34`, `37` | 15 |
| 🟣 **MAESTRO** | `50`, `58`, `63`, `67` | 12-19 |
| 🔴 **DINERS** | `36`, `38`, `39` | 14 |
| 🟡 **DISCOVER** | `6011`, `65` | 16 |
| 🟢 **JCB** | `3528`-`3589` | 16 |
| 🔵 **UNIONPAY** | `62` | 16-19 |
| ⚪ **EURO6000** | `402400`-`402403` | 16 |

---

## 🚀 Instalación / Installation

```bash
# Clonar el repositorio / Clone the repository
git clone https://github.com/Hugopvigo/Validador-tarjeta-credito.git

# Entrar al directorio / Navigate to directory
cd Validador-tarjeta-credito

# Ejecutar / Run
python creditcardvalidator.py
```

**Requisitos / Requirements:** Python 3.8 o superior / Python 3.8 or higher (sin dependencias externas / no external dependencies)

---

## 📖 Uso / Usage

```bash
$ python creditcardvalidator.py
```

### Ejemplos / Examples

**✅ Tarjeta válida / Valid card:**
```
Introduce el número de la tarjeta / Enter card number: 4532015112830366

==================================================
  Tarjeta / Card       : 4532015112830366
  Empresa / Company    : VISA
  Longitud / Length OK : Sí / Yes
  Luhn OK              : Sí / Yes
==================================================
  ✅  Tarjeta VÁLIDA / Card VALID
==================================================
```

**❌ Tarjeta inválida / Invalid card:**
```
Introduce el número de la tarjeta / Enter card number: 1234567890123

==================================================
  Tarjeta / Card       : 1234567890123
  Empresa / Company    : UNKNOWN
  Longitud / Length OK : Sí / Yes
  Luhn OK              : No
==================================================
  ❌  Tarjeta NO VÁLIDA / Card INVALID
==================================================
```

**🚫 Error de entrada / Input error:**
```
Introduce el número de tarjeta / Enter card number: abc123
Error: solo se permiten dígitos / Error: only digits are allowed.
```

---

## 🧪 Tests / Testing

```bash
python -m pytest test_creditcardvalidator.py -v
```

---

## 📁 Estructura del Proyecto / Project Structure

```
Validador-tarjeta-credito/
├── creditcardvalidator.py              # Código principal / Main code
├── Validador tarjeta notebook.ipynb    # Versión Jupyter / Jupyter version
├── test_creditcardvalidator.py         # Tests unitarios / Unit tests
├── README.md                           # Este archivo / This file
└── .gitignore
```

---

## 🔧 Algoritmo de Luhn / Luhn Algorithm

El **algoritmo de Luhn** es un método simple de checksum utilizado para validar números de identificación, como números de tarjetas de crédito. Fue inventado por Hans Peter Luhn en 1954 y está descrito en el estándar **ISO/IEC 7812-1**.

The **Luhn algorithm** is a simple checksum method used to validate identification numbers such as credit card numbers. It was invented by Hans Peter Luhn in 1954 and is described in the **ISO/IEC 7812-1** standard.

**Pasos / Steps:**
1. Empezando por la derecha, duplicar cada segundo dígito / Starting from the right, double every second digit
2. Si el resultado del duplicado es > 9, sumar los dígitos / If the doubled result is > 9, sum the digits
3. Sumar todos los dígitos / Sum all digits
4. Si la suma total es múltiplo de 10, el número es válido / If the total sum is a multiple of 10, the number is valid

---

## 📄 Licencia / License

MIT License - Ver [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor / Author

**Hugo P. Vigo** - [GitHub](https://github.com/Hugopvigo)

---

<div align="center">

Hecho con ❤️ en Python / Made with ❤️ in Python

</div>
