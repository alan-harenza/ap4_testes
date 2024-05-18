"""Carrinho de compras feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pytest import fixture
from app.carrinho_compras import CarrinhoCompras


@fixture
def carrinho():
    return CarrinhoCompras()


@scenario('carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""


@given('que tenho um carrinho de compras com o item "camiseta" e preco de R$ 29.99')
def carrinho_com_camiseta_1(carrinho):
    """que tenho um carrinho de compras com o item "camiseta" e preco de R$ 29.99."""
    carrinho.adicionar_item(CarrinhoCompras, "Camiseta", 29.99)
    assert carrinho.total() == 29.99


@when('eu adiciono o item "calca" com o preco R$ 49.99')
def adicionar_calca(carrinho):
    """eu adiciono o item "calca" com o preco R$ 49.99."""
    carrinho.adicionar_item("Calca", 49.99)


@then('o total do carrinho de compras deve ser R$ 79.98')
def total_79_98():
    """o total do carrinho de compras deve ser R$ 79.98."""
    assert carrinho.total() == 79.98


@scenario('carrinho.feature', 'Remover item do carrinho')
def test_remover_item_do_carrinho():
    """Remover item do carrinho."""


@given('que tenho um carrinho de compras com o item "camiseta" e preco de R$ 29.99')
def carrinho_com_camiseta_2(carrinho):
    """que tenho um carrinho de compras com o item "camiseta" e preco de R$ 29.99."""
    carrinho.adicionar_item(CarrinhoCompras, "Camiseta", 29.99)
    assert carrinho.total() == 29.99


@when('eu removo o item do carrinho')
def remover_item():
    """eu removo o item do carrinho."""
    carrinho.remover_item()


@then('o carrinho de compras deve estar vazio')
def carrinho_vazio():
    """o carrinho de compras deve estar vazio."""
    assert carrinho.esta_vazio()
