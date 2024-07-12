def criar_lista_compras():
    categorias = { 
        "frutas": {"melancia": 3, "pêssego": 2, "uva": 5, "maçã": 2, "pera": 3},
        "vegetais": {"brocólis": 4, "alface": 2, "tomate": 3, "cebola": 2, "cenoura": 3},
        "laticínios": {"leite": 4, "queijo": 5, "iogurte": 3},
        "carnes": {"frango": 6, "peixe": 8, "carne bovina": 10},
        "grãos": {"avelã": 3, "amendoim": 2, "girassol": 4, "milho": 2, "arroz": 5},
        "limpeza": {"sabão": 2, "detergente": 3, "desinfetante": 4}
    }

    lista_compras = []
    dinheiro_disponivel = 20

    print("Selecione as categorias de produtos que deseja adicionar à lista (Digite 'finalizar' para encerrar e 'ver' para ver a lista.):")
    for categoria in categorias:
        print("-", categoria)

    while True:
        print("\nDinheiro disponível: R$", dinheiro_disponivel)
        escolha = input("Categoria: ").lower()

        if escolha == "finalizar":
            break

        if escolha == "ver":
            if lista_compras:
                print("\nLista de Compras Atual:")
                for item, quantidade in lista_compras:
                    print("-", quantidade, item)
            else:
                print("Sua lista de compras está vazia.")
            continue

        if escolha in categorias:
            print("Itens disponíveis na categoria", escolha + ":")
            for item, preco in categorias[escolha].items():
                print("-", item, "(R$",preco,")")

            entrada_itens = input("Digite os itens com suas quantidades separados por vírgula (ex: 3 maçã, 2 uva) ou digite 'voltar' para selecionar outra categoria: ").lower()

            if entrada_itens == "voltar":
                continue

            itens_quantidades = entrada_itens.split(",")
            itens_adicionados = []

            total_compra = 0
            for item_quantidade in itens_quantidades:
                item_quantidade = item_quantidade.strip() 
                partes = item_quantidade.split()
                if len(partes) == 2 and partes[0].isdigit():
                    quantidade = int(partes[0])
                    item = partes[1]
                    if item in categorias[escolha]:
                        preco_item = categorias[escolha][item] * quantidade
                        total_compra += preco_item
                        if total_compra <= dinheiro_disponivel:
                            lista_compras.append((item, quantidade))
                            itens_adicionados.append((item, quantidade))
                        else:
                            print("Você não tem dinheiro suficiente para comprar", quantidade, item)
                    else:
                        print("Item", item, "inválido!")
                else:
                    print("Entrada inválida para o item:", item_quantidade)

            if itens_adicionados:
                print("Itens adicionados à lista de compras:")
                for item, quantidade in itens_adicionados:
                    print("-", quantidade, item)
                dinheiro_disponivel -= total_compra

        else:
            print("Categoria inválida!")

    print("\nLista de Compras Finalizada:")
    for item, quantidade in lista_compras:
        print("-", quantidade, item)

criar_lista_compras()
