"""Carrinho de compras feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from app.carrinho_compras import CarrinhoCompras


@scenario('features\carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""


@scenario('features\carrinho.feature', 'Remover item do carrinho')
def test_remover_item_do_carrinho():
    """Remover item do carrinho."""


@given('que tenho um carrinho de compras com o item "Camiseta" e preco de R$ 29.99')
def _():
    """que tenho um carrinho de compras com o item "Camiseta" e preco de R$ 29.99."""
    raise NotImplementedError


@when('eu adiciono o item "Calþa" com o preco R$ 49.99')
def _():
    """eu adiciono o item "Calþa" com o preco R$ 49.99."""
    raise NotImplementedError


@when('eu removo o item do carrinho')
def _():
    """eu removo o item do carrinho."""
    raise NotImplementedError


@then('o carrinho de compras deve estar vazio')
def _():
    """o carrinho de compras deve estar vazio."""
    raise NotImplementedError


@then('o total do carrinho de compras deve ser R$ 79.98')
def _():
    """o total do carrinho de compras deve ser R$ 79.98."""
    raise NotImplementedError
