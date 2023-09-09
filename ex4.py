import sys

"""
Ao iniciar, o programa deve solicitar ao usuário os nomes dos campos que serão obrigatórios para os cadastros.
Na sequência, deve mostrar o menu e iniciar o fluxo normal de execução.

Opção 1. Crie uma função cadastrar_usuario para cadastrar um usuário de maneira flexível.
A função deve receber uma tupla com os campos obrigatórios para cadastro.
Estes campos devem ser definidos globalmente em tempo de execução pelo usuário.
(opção anterior) O usuário pode cadastrar quantos campos quiser além dos obrigatórios até digitar "sair".Deve então retornar ao menu.
A função deve retornar o dicionário gerado e armazenar no dicionário global chamado banco_usuarios

Opção 2. Criar uma outra função imprimir_usuarios com 4 possibilidades de invocação:- Caso a função não receba argumentos, deve imprimir todos os usuários 
com todas suasinfos.- Caso receba vários nomes, deve imprimir todos dados de todos os usuários com os 
nomesespecificados.exemplo: imprimir_usuarios("alberto", "joaquina", "enzo", "valentina")- Caso receba uma série de 
elementos campo e valor deve imprimir apenas os dadoscompletosde todos os usuários que satisfazem as condições:
- Receber nomes e campos, valor: apenas nos usuários listados, imprimir os dados dosusuários quesatisfazem às condições dadas. 
(usar *args e **kwargs facilita a definção da fun=ção)exemplo de execução da opção 

2:1 - impirmir todos2 - filtrar por nomes3 - filtrar por campos4 - filtrar por nomes e campos2alberto, maria, enzo>> 
deve imprimir os dados de alberto, maria e enzooutro exemplo3digite o campo de busca:endereçodigite o endereçoxv de 
novembromais algum campo:idadedigite a idade20mais algum campo?sair

>> Deve imprimir os dados dos usuários que possuem o endereço xv de novembro a e idade20. Retorna ao menu inicial outro exemplo
:4digite os nomesalberto, maria, josedigite os camposidadedigte a idade10outro camposair>> 
deve imprimir os dados dos usuários, entre alberto, maria e josé, que possuem 10 anos.Retorna ao menu inicial.
"""

class Fake_database():
    """_summary_

    """
    def __init__(self):

        self.user_bank = ()
        self.obligatory_fields_tuple = ()

    def _validate_values_for_tuple(user_entry) -> tuple:
        """_summary_
            Limpa input removendo espaços em branco e adquirindo chaves separadas por vírgula.
        Args:
            user_entry (str): Input com valores do usuário separados por vírgula.

        Returns:
            tuple: tupla das chaves informadas pelo usuário.
        """
        return [field.strip() for field in user_entry.split(',')]
    
    def _get_user_obligatory_fields_tuple(self) -> tuple:
        """_summary_
            Adquire os campos obrigatórios por input. e usuário digitar nenhum retorna tupla vazia.
        Returns:
            obligatory_tuple: tupla com campos obrigatórios inseridos pelo usuário (validados) ou tupla vazia.
        """
        obligatory_tuple = ()
        while True:
            user_entry = input('Digite os nomes dos campos separados por vírgula (sem espaços em branco) ou "nenhum" para finalizar sem adicionar campos: ')
            # Limpa input removendo espaços em branco e adquirindo chaves separadas por vírgula.
            field_names = self._validate_values_for_tuple(user_entry)
            # Se usuário escreveu nenhum não cria chaves e retorna tupla vazia.
            if ('nenhum' in field_names):
                break
            # Quebra loop se não houverem chaves vazias, retornando a tupla validada.
            elif all(field_names): 
                obligatory_tuple = tuple(field_names) 
                break
            else: 
                print("Por favor, insira nomes válidos para todos os campos.")
        return obligatory_tuple

    def _register_user(self, obligatory_fields_tuple) -> None:
        non_obligatory_tuple = ()
        if (input('Deseja inserir campos não obrigatórios para usuário? (s/n): ').upper == 'S'):
            while True:
                user_entry = input('Digite os nomes dos campos separados por vírgula (sem espaços em branco) ou "nenhum" não adicionar campos: ')
                # Se usuário escreveu nenhum não cria chaves e retorna tupla vazia.
                if ('nenhum' in field_names):
                    break
        return 

    def _print_main_menu(self) -> None:
        print('Fake DB:')
        print('-- Opção 1 -- Regitrar novo usuário')
        print('-- Opção 2 -- Imprimir usuários.')
        print('-- Opção 0 -- Sair')
    
    def _print_search_user_menu(self):
        print('pEsquisa de usuários cadastrados. Escolha:')
        print('-- Opção 1 imprimir todos usuários -- ')
        print('-- Opção 2  -- ')
        print('-- Opção 3 -- ')
        print('-- Opção 4 -- ')
        print('-- Opção 5 -- Voltar para tela inicial')
        print('-- Opção 6 -- Encerrar programa')

    def _select_user_search(self):
        """_summary_
            Método de controle do menu de busca.
        """
        option  = ''
        while True:
            self._print_search_user_menu()
            if(option == '1'):
                
            elif(option == '2'):

            elif(option == '3'):

            elif(option == '4'):

            elif(option == '5'):
                # Volta para menu principal.
                break
            elif(option == '6'):
                # Encerra o programa
                sys.exit()


    def start(self) -> None:
        """_summary_
            Método de controle do menu inicial.
        """
        # Adquire nomes de campos obrigatórios do usuário.
        self._get_user_obligatory_fields_tuple()
        option = ''
        while True:
            # Faz print do menu inicial.
            self._print_main_menu()
            # 
            option = ''
            if(option == '1'):
                self._register_user()
            elif(option == '2'):
                self._select_user_search()
            elif(option == '0'):
                # termina programa.
                break
            else:
                print('Escolha não reconhecida.')

fake_db = Fake_database()
fake_db.start()