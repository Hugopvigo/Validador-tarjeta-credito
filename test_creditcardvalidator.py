#!/usr/bin/env python3
"""
Tests unitarios para el Validador de Tarjetas de Crédito.
Unit tests for the Credit Card Validator.
"""

import unittest
from creditcardvalidator import CreditCard, luhn_check


class TestLuhnAlgorithm(unittest.TestCase):
    """Tests para el algoritmo de Luhn / Tests for the Luhn algorithm."""

    def test_valid_visa(self):
        self.assertTrue(luhn_check("4532015112830366"))

    def test_valid_mastercard(self):
        self.assertTrue(luhn_check("5425233430109903"))

    def test_valid_amex(self):
        self.assertTrue(luhn_check("374245455400126"))

    def test_invalid_number(self):
        self.assertFalse(luhn_check("1234567890123"))

    def test_all_zeros(self):
        self.assertTrue(luhn_check("0000000000000000"))

    def test_single_digit(self):
        self.assertTrue(luhn_check("0"))


class TestCardCompany(unittest.TestCase):
    """Tests para identificación de empresa / Tests for company identification."""

    def test_visa(self):
        self.assertEqual(CreditCard("4111111111111111").company, "VISA")

    def test_visa_debit(self):
        self.assertEqual(CreditCard("4012888888881881").company, "VISA")

    def test_mastercard(self):
        self.assertEqual(CreditCard("5555555555554444").company, "MASTERCARD")

    def test_amex(self):
        self.assertEqual(CreditCard("378282246310005").company, "AMEX")

    def test_amex_34(self):
        self.assertEqual(CreditCard("341111111111111").company, "AMEX")

    def test_maestro(self):
        self.assertEqual(CreditCard("5000000000000000").company, "MAESTRO")

    def test_maestro_67(self):
        self.assertEqual(CreditCard("6700000000000000").company, "MAESTRO")

    def test_diners(self):
        self.assertEqual(CreditCard("36110361103612").company, "DINERS")

    def test_discover(self):
        self.assertEqual(CreditCard("6011111111111117").company, "DISCOVER")

    def test_discover_65(self):
        self.assertEqual(CreditCard("6500000000000000").company, "DISCOVER")

    def test_jcb(self):
        self.assertEqual(CreditCard("3530111333300000").company, "JCB")

    def test_unionpay(self):
        self.assertEqual(CreditCard("6200000000000000").company, "UNIONPAY")

    def test_unknown(self):
        self.assertEqual(CreditCard("1234567890123").company, "UNKNOWN")


class TestCardValidation(unittest.TestCase):
    """Tests para validación completa / Tests for full validation."""

    def test_valid_card(self):
        result = CreditCard("4532015112830366").validate()
        self.assertTrue(result["is_valid"])
        self.assertTrue(result["length_ok"])
        self.assertTrue(result["luhn_ok"])
        self.assertEqual(result["company"], "VISA")

    def test_invalid_luhn(self):
        result = CreditCard("4532015112830367").validate()
        self.assertFalse(result["is_valid"])
        self.assertTrue(result["length_ok"])
        self.assertFalse(result["luhn_ok"])

    def test_too_short(self):
        result = CreditCard("41111").validate()
        self.assertFalse(result["is_valid"])
        self.assertFalse(result["length_ok"])

    def test_too_long(self):
        result = CreditCard("4" * 20).validate()
        self.assertFalse(result["is_valid"])
        self.assertFalse(result["length_ok"])

    def test_empty_string(self):
        result = CreditCard("").validate()
        self.assertFalse(result["is_valid"])
        self.assertFalse(result["length_ok"])


if __name__ == "__main__":
    unittest.main()
