"""Tests for the important CLI functions.

We patch input() and the external API so the tests are fast and do not
need the internet or real typing.
"""
from unittest.mock import patch

import cli
import cli_actions
import models


def test_view_inventory(capsys):
    cli_actions.view_inventory()
    output = capsys.readouterr().out
    assert "Milk" in output


@patch("builtins.input", side_effect=["Eggs", "12", "60"])
def test_add_item(_inp):
    cli_actions.add_item()
    assert models.get_item(3)["product_name"] == "Eggs"


@patch("builtins.input", side_effect=["1", "50", "10"])
def test_update_item(_inp):
    cli_actions.update_item()
    assert models.get_item(1)["quantity"] == 50


@patch("builtins.input", side_effect=["2"])
def test_delete_item(_inp):
    cli_actions.delete_item()
    assert models.get_item(2) is None


@patch("cli_actions.external_api.lookup_by_name")
@patch("builtins.input", side_effect=["milk"])
def test_search_api(_inp, mock_lookup, capsys):
    mock_lookup.return_value = {"product_name": "Milk", "quantity": 1, "price": 0}
    cli_actions.search_api()
    assert "Milk" in capsys.readouterr().out


@patch("cli_actions.external_api.lookup_by_name")
@patch("builtins.input", side_effect=["juice"])
def test_import_api(_inp, mock_lookup):
    mock_lookup.return_value = {"product_name": "Juice", "quantity": 1, "price": 0}
    cli_actions.import_api()
    assert models.get_item(3)["product_name"] == "Juice"


def test_handle_choice_exit():
    assert cli.handle_choice("7") is False


def test_handle_choice_invalid(capsys):
    assert cli.handle_choice("99") is True
    assert "Invalid" in capsys.readouterr().out
