Feature: Carrinho de compras

    Como usuario
    Eu quero adicionar e remover itens do meu carrinho de compras
    Para gerenciar minhas compras
    
    Scenario: Adicionar itens ao carrinho
        given que tenho um carrinho de compras com o item "camiseta" e preco de R$ 29.99
        when eu adiciono o item "calca" com o preço R$ 49.99
        then o total do carrinho de compras deve ser R$ 79.98
    
    Scenario: Remover item do carrinho
        given que tenho um carrinho de compras com o item "camiseta" e preco de R$ 29.99
        when eu removo o item do carrinho
        then o carrinho de compras deve estar vazio
