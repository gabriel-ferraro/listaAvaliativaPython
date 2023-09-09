import sys

class Fake_database():
    """_summary_
        Simula um banco de dados salvando usuários em memória. Ao iniciar o programa o usuário deve inserir valores que servirão como chaves obrigatórias,
        que devem ser sempre preenchidas ao registrar um novo usuário. Após a primeira etapa o programa mostra um menu de escolhas onde o usuário pode registrar novos usuários,
        inserir campos opcionais e 'salvar' o usuário; A outra opção permite pesquisar por todos usuários salvos na lista de tuplas.
    """
    def __init__(self):
        """_summary_
            Inicialzia uma lista vazia para representar o 'banco' de usuários em memória, mantém as chaves obrigatórias inseridas no início do programa.
        """
        self.user_bank = [] # Armazena em memória os usuários criados.
        self.obligatory_fields_tuple = () # Tupla de campos obrigatórios requisitdados no início do programa.
    
    def _get_user_obligatory_fields_tuple(self) -> None:
        """_summary_
            Adquire os campos obrigatórios por input. e usuário digitar nenhum retorna tupla vazia.
        Returns:
            obligatory_tuple: tupla com campos obrigatórios inseridos pelo usuário (validados) ou tupla vazia.
        """
        tuple_for_keys = tuple()
        while True:
            user_entry = input('Digite os nomes dos campos separados por vírgula (sem espaços em branco) ou "nenhum" para finalizar sem adicionar campos: ').lower()
            # Limpa input removendo espaços em branco e adquirindo chaves separadas por vírgula.
            field_names = [field.strip() for field in user_entry.split(',')]
            # Se usuário escreveu nenhum não cria chaves e retorna tupla vazia.
            if ('nenhum' in field_names):
                break
            # Quebra loop se não houverem chaves vazias, retornando a tupla validada.
            elif(all(field_names)): 
                tuple_for_keys = tuple(field_names) 
                break
            else: 
                print("Por favor, insira nomes válidos para todos os campos.")
        print(f'Tupla de campos obrigatórios: {tuple_for_keys}')
        self.obligatory_fields_tuple = tuple_for_keys

    def _register_user(self) -> None:
        """_summary_
        """
        user = {}
        # Checa se tupla de itens obrigatórios tem itens.
        if (self.obligatory_fields_tuple):
            # Pede para preencher os campos obrigatórios.
            for field in self.obligatory_fields_tuple:
                user[field] = input(f"Digite o valor para o campo '{field}': ")
        
        # Pede para preencher os campos opcionais.
        while True:
            optional_field = input("Digite o nome de um campo opcional (ou 'sair' para encerrar): ")
            # Quebra loop.
            if optional_field.upper() == 'SAIR':
                break
            user[optional_field] = input(f"Digite o valor para o campo '{optional_field}': ")
        # Adiciona o usuário ao banco de usuários.
        self.user_bank.append(user)
        print(f'Usuário cadastrado com sucesso: {user}')
    
    def _print_users(self, *args, **kwargs) -> None:
        """_summary_
            Identifica argmentos recebidos. Se não receber argumentos faz print de todos dados, se receber nomes retorna todos dados dos usuários recebidos,
            se receber argumentos de chave e valor, faz print das informações dos usuários que combinam.
        """
        # Checa condições.
        if (not args and not kwargs):
            # Caso a função não receba argumentos, imprimir todos os usuários com todas as informações
            for user in self.user_bank:
                print(user)
        else:
            # Caso receba argumentos, filtrar os usuários com base nas condições fornecidas
            filtered_users = []
            for user in self.user_bank:
                # Por default atende condições para fazer pesquisa.
                meet_conditions = True
                # Filtrar por nomes
                if (args):
                    if (user.get("nome") not in args):
                        meet_conditions = False
                # Filtrar por campos e valores
                for field, value in kwargs.items():
                    if (field not in user or user[field] != value):
                        meet_conditions = False
                if (meet_conditions):
                    filtered_users.append(user)
            # Imprimir os usuários filtrados
            print('\nDados identificados: ')
            for user in filtered_users:
                print(user)


    def _select_user_search(self) -> None:
        """_summary_
            Método de controle do menu de busca.
        """
        option  = ''
        while True:
            # Print do menu de pesquisa.
            print('Menu de pesquisa de usuários cadastrados:')
            print('-- Opção 1 -- Pesquisar todos usuários')
            print('-- Opção 2 -- Insira os nomes de usuários para ver seus dados')
            print('-- Opção 3 -- Insira chaves-valores para adquirir os dados dos usuários semelhantes')
            print('-- Opção 4 -- Voltar para o menu principal.')
            print('-- Opção 0 -- Encerrar programa')
            option = input("Escolha uma opção: ")
            if(option == '1'):
                self._print_users()
            elif(option == '2'):
                names = input('Insira o nome dos usuários, separado por vírgula: ')
                names = [name.strip() for name in names.split(',') if name.strip()]
                # Verifica se a lista de nomes não está vazia após a validação.
                if (names):
                    self._print_users(*names)
                else:
                    print("Nenhum nome válido inserido.")
            elif(option == '3'):
                fields = input('Insira os campos de busca, separado por vírgula: ')
                fields = [field.strip() for field in fields.split(',') if field.strip()]
                kwargs = {}
                # Verifica se a lista de campos não está vazia após a validação.
                if (fields):
                    for field in fields:
                        value = input(f'Digite o valor para o campo "{field}": ')
                        kwargs[field] = value
                    self._print_users(**kwargs)
            elif(option == '4'):
                # Volta para menu principal.
                print('Voltando para o menu principal.')
                break
            elif(option == '0'):
                # Encerra o programa
                print("Finalizando.")
                sys.exit()
            else:
                print('Escolha não reconhecida.')

    def start(self) -> None:
        """_summary_
            Método de controle do menu inicial.
        """
        # Adquire nomes de campos obrigatórios do usuário.
        self._get_user_obligatory_fields_tuple()
        option = ''
        while True:
            # Faz print do menu principal.
            print('Fake DB:')
            print('-- Opção 1 -- Registrar novo usuário')
            print('-- Opção 2 -- Pesquisar por usuários cadastrados.')
            print('-- Opção 0 -- Sair')
            option = input("Escolha uma opção: ")
            if(option == '1'):
                self._register_user()
            elif(option == '2'):
                self._select_user_search()
            elif(option == '0'):
                # termina programa.
                print("Finalizando.")
                break
            else:
                print('Escolha não reconhecida.')

fake_db = Fake_database()
fake_db.start()