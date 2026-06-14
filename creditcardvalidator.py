#!/usr/bin/env python3
"""
Credit Card Validator / Validador de Tarjetas de Crédito
Valida números de tarjeta usando el algoritmo de Luhn e identifica la empresa emisora.
Validates card numbers using the Luhn algorithm and identifies the issuing company.
"""

CARD_COMPANIES = [
    ("VISA",         ("4",)),
    ("MAESTRO",      ("50", "67", "58", "63")),
    ("MASTERCARD",   ("51", "52", "53", "54", "55")),
    ("AMEX",         ("37", "34")),
    ("DINERS",       ("36", "38", "39")),
    ("DISCOVER",     ("6011", "65")),
    ("JCB",          ("3528", "3529", "353", "354", "355", "356", "357", "358")),
    ("UNIONPAY",     ("62",)),
    ("EURO6000",     ("402400", "402401", "402402", "402403")),
]


def luhn_check(card_number: str) -> bool:
    """
    Implementa el algoritmo de Luhn para validar números de tarjeta.
    Implements the Luhn algorithm to validate card numbers.

    Returns True if the card number passes the checksum, False otherwise.
    Devuelve True si el número supera la verificación, False en caso contrario.
    """
    digits = [int(d) for d in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(divmod(d * 2, 10))
    return total % 10 == 0


class CreditCard:
    """
    Clase que representa y valida una tarjeta de crédito.
    Class that represents and validates a credit card.
    """

    def __init__(self, card_number: str) -> None:
        self.card_number = card_number

    @property
    def company(self) -> str:
        """
        Identifica la empresa emisora de la tarjeta.
        Identifies the card issuing company.

        Returns the company name or 'UNKNOWN' / 'DESCONOCIDA'.
        """
        for name, prefixes in CARD_COMPANIES:
            if self.card_number.startswith(prefixes):
                return name
        return "UNKNOWN"

    @property
    def is_valid_length(self) -> bool:
        """
        Verifica que la longitud del número esté entre 13 y 19 dígitos.
        Checks that the number length is between 13 and 19 digits.
        """
        return 13 <= len(self.card_number) <= 19

    def validate(self) -> dict:
        """
        Validación completa de la tarjeta.
        Full card validation.

        Returns a dict with: company, length_ok, luhn_ok, is_valid.
        Devuelve un dict con: empresa, longitud_ok, luhn_ok, es_valida.
        """
        length_ok = self.is_valid_length
        luhn_ok = luhn_check(self.card_number) if length_ok else False
        return {
            "company": self.company,
            "length_ok": length_ok,
            "luhn_ok": luhn_ok,
            "is_valid": length_ok and luhn_ok,
        }


def get_user_input() -> str:
    """
    Solicita y valida la entrada del usuario.
    Requests and validates user input.
    """
    while True:
        raw = input("Introduce el número de la tarjeta / Enter card number: ").strip()
        if not raw:
            print("Error: no se introdujo ningún número / Error: no number entered.")
            continue
        if not raw.isdigit():
            print("Error: solo se permiten dígitos / Error: only digits are allowed.")
            continue
        if len(raw) < 13 or len(raw) > 19:
            print("Error: la longitud debe ser entre 13 y 19 dígitos / Error: length must be between 13 and 19 digits.")
            continue
        return raw


def display_result(card: CreditCard) -> None:
    """
    Muestra el resultado de la validación en español e inglés.
    Displays the validation result in Spanish and English.
    """
    result = card.validate()
    print()
    print("=" * 50)
    print(f"  Tarjeta / Card       : {card.card_number}")
    print(f"  Empresa / Company    : {result['company']}")
    print(f"  Longitud / Length OK : {'Sí / Yes' if result['length_ok'] else 'No'}")
    print(f"  Luhn OK              : {'Sí / Yes' if result['luhn_ok'] else 'No'}")
    print("=" * 50)
    if result["is_valid"]:
        print("  ✅  Tarjeta VÁLIDA / Card VALID")
    else:
        print("  ❌  Tarjeta NO VÁLIDA / Card INVALID")
    print("=" * 50)


if __name__ == "__main__":
    card_number = get_user_input()
    card = CreditCard(card_number)
    display_result(card)
