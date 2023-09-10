class Tic_tac_toe_4x4_game:
    """_summary_
        Classe que gerencia um jogo da velha 4x4 que pode ser jogado por dois jogadores no console.
        Os jogadores devem escolher símbolos para representar suas jogadas, como: X ou O e um símbolo para representar o tabuleiro. Os símbolos não devem repetir
        e devem ter o tamaho de um caractere. Um jogador deve selecionar o índice da linha e coluna que deseja fazer a jogada,
        ganha aquele que completar uma fileira com seu símbolo na vertical, diagonal, ou horizontal, se todos campos são preenchidos ninguém ganham (empate).

        O grid que representa o "tabuleiro" é uma matriz 4x4, a cada jogada é checado o estado do jogo de acordo 
        com os símbolos na matriz. Enquanto a matriz não é completamente preenchida ou um jogador ganha, o jogo continua.
    """
    def __init__(self, player_1_symbol: str, player_2_symbol: str, board_symbol: str) -> None:
        """_summary_
            O construtor recebe os valores para gerenciar as escolhas do jogador, é validado se símbolos repetidos foram apresentados.
            O board é inicializado como uma lista vazia e a quantidade de jogadas com 0.
        Args:
            player_1_symbol (str): Símbolo esolhido pelo player 1.
            player_2_symbol (str): Símbolo esolhido pelo player 2.
            board_symbol (str): Símbolo ecolhido para representar os grids do tabuleiro.
        """
        self.player_1_symbol = player_1_symbol
        self.player_2_symbol = player_2_symbol
        self.board_symbol = board_symbol
        self.amount_of_plays = 0 # Contador da quantidade de jogadas.
        self.board = [] # Será a matriz que contém o tabuleiro.
        # Faz validação dos símbolos dos jogadores.
        self._validate_players_symbols()

    def _validate_players_symbols(self):
        """_summary_
            Valida se os jogadores inseriram símbolos repetidos ou maiores que 1 (uma string ao invés de somente um caractere)
            e lança mensagem até que valores diferentes sejam fornecidos. Após validação inicializa o board.
        """
        while (
                len(self.player_1_symbol) != 1
                or len(self.player_2_symbol) != 1
                or len(self.board_symbol) != 1
                or self.player_1_symbol == self.player_2_symbol 
                or self.player_1_symbol == self.board_symbol 
                or self.player_2_symbol == self.board_symbol):
            print('Símbolos identificadores devem ser diferentes para os players e o board e devem ter um (1) caractere de tamanho! Insira outros valores.')
            self.player_1_symbol = input("Símbolo do player 1: ")
            self.player_2_symbol = input("Símbolo do player 2: ")
            self.board_symbol = input("Símbolo para o tabuleiro: ")
    
        # Com os valores válidos, inicializa o board.
        self._generate_board()
    
    def _generate_board(self) -> None:
        """_summary_
            Faz o set do board 4x4 preenchendo os campos da matriz com o símbolo escolhido pelos jogadores.
        """
        self.board = [[self.board_symbol for i in range(4)] for i in range(4)]
    
    def _is_game_playing(self, player_symbol: str) -> bool:
        """_summary_
            Determina se o jogo deve continuar retornando um booleano (False é fim do jogo),
            checa condições para mandar mensagem de vitória ou empate (todos campos marcados sem formar sequência em reta ou diagonal).
        Args:
            player_symbol (str): símbolo escolhido para representar o jogador.

        Returns:
            bool: Booleano para representar se o jogo continua (true) ou acabou (false).
        """
        # Por padrão o jogo continua.
        game_continue = True
        # Verifica se um jogador ganhou em uma linha.
        for rows in self.board:
            # O for percorre todos as linhas do tabuleiro, se uma tem todos campos com mesmo símbolo que do jogador atual, vitória do jogador.
            if (all(symbol == player_symbol for symbol in rows)):
                self._victory_message(player_symbol)
                game_continue = False
            
        # Verifica se um jogador ganhou na coluna.
        for column in range(4):
            # O for percorre todos os itens da matriz, 
            if all(self.board[row][column] == player_symbol for row in range(4)):
                self._victory_message(player_symbol)
                game_continue = False

        # Verificar vitória nas diagonais. For da esquerda checa se diagonal esquerda (valores de i crescente): 0,0 - 1,1 - 2,2 - 3,3 tem o símbolo do jogador.
        # For da direita compara valores da diagonal direita (linha -> i e coluna -> 4-1-i): 0,3 - 1,2 - 2,1 - 3,0.
        if all(self.board[i][i] == player_symbol for i in range(4)) or all(self.board[i][4 - 1 - i] == player_symbol for i in range(4)):
            self._victory_message(player_symbol)
            game_continue = False

        # Verifica se todos os campos foram preenchidos e não houve vitória de nenhum jogador.
        if (all(all(field != self.board_symbol for field in row) for row in self.board)):
            print("Empate! Ninguém ganhou.\nFim do joga da velha 4x4.")
            game_continue = False

        # Retorna controle de estado do jogo.
        return game_continue

    def _validate_play(self, row: int, column: int) -> bool:
        """_summary_
            Valida a entrada do jogador para índice da linha e coluna.
        Args:
            row (int): inteiro que identifica a linha escolhida pelo jogador no tabuleiro.
            column (int): inteiro que identifica a coluna escolhida pelo jogador no tabuleiro.

        Returns:
            bool: falso se valores inseridos estão fora do intervalo da matriz ou se não são int.
        """
        # Retorno default é True.
        result = True
        if ((row < 0 or row > 3) or (column < 0 or column > 3)):
            print("É necessário inserir um número inteiro válido maior ou igual a 0 e menor ou igual a 3 para fazer a jogada.")
            result = False
        elif (self.board[row][column] != self.board_symbol):
            print("Esse campo já foi preenchido. Escolha outro.")
            result = False
        # Realiza retorno.
        return result
    
    def _make_play(self, current_player_symbol: str) -> None:
        """_summary_
            Identifica o símbolo do jogador atual e o grid onde o jogador deseja jogar.
            Faz a jogada se os símbolos são váidos e o campo escolhido ainda não foi preenchido, aumenta qtde de jogadas.
        Args:
            player_symbol (str): símbolo do jogador atual.
        """
        # Checa a linha e coluna que o player atual quer jogar.
        # Enquanto valores inválidos (diferentes de inteiros ou fora dos limites da matriz) forem inseridos, manda mensagem para validação.
        while True:
            try:
                row = int(input(f"Jogador {current_player_symbol}: escolha a linha: "))
                column = int(input(f"Jogador {current_player_symbol}: escolha a coluna: "))
            except ValueError:
                print("É necessário inserir um número inteiro válido maior ou igual a 0 e menor ou menor ou igual a 3 para fazer a jogada.")
                continue
            if(self._validate_play(row, column)):
                # Se jogador tenta fazer joagada em campo válido, quebra loop.
                break
            # Faz print do board novamente para que os players possam visualizar onde fazer a jogada.
            self._print_current_board()
            
        # Coloca o símbolo do jogador no campo (faz a jogada).
        self.board[row][column] = current_player_symbol
        # Aumenta a quantidadede jogadas.
        self.amount_of_plays += 1

    def _print_current_board(self):
        """_summary_
            Faz o set do board 4x4 preenchendo os campos da matriz com o símbolo escolhido pelos jogadores.
            Faz print com os índices das respectivas linhas e colunas para facilitar a identificação no grid.
        """
        # Imprimir os índices das colunas
        col_indexes = ' '.join([str(i) for i in range(4)])
        print('  ' + col_indexes)
        for i in range(4):
            # Imprimir os índices das linhas
            print(i, end=' ')
            # Faz print dos símbolos dos grids da matriz.
            for j in range(4):
                print(self.board[i][j], end=' ')
            # Print para fazer quebra no final de cada 'row'.
            print()

    def _victory_message(self, player_symbol: str) -> None:
        """_summary_
            Faz o print de uma mensagem de vitória com o símbolo do jogador vencedor.
        Args:
            player_symbol (str): Símbolo do jogador vencedor.
        """
        print(f"O jogador com símbolo -> {player_symbol} ganhou !!!\nFim do joga da velha 4x4.")

    def run_game(self) -> None:
        """_summary_
            Roda o jogo da velha.
        """
        print('--- início do jogo da velha! ---\n')
        # Faz set do primeiro jogador.
        current_player_symbol = self.player_1_symbol
        while True:
            # Faz print do tabuleiro no momento atual.
            self._print_current_board()
            # Jogador atual faz jogada
            self._make_play(current_player_symbol)
            # Checa se jogo continua ou acabou (termina loop do jogo).
            if (not self._is_game_playing(current_player_symbol)):
                break
            # Muda a vez da jogada para o outro jogador.
            current_player_symbol = self.player_2_symbol if current_player_symbol == self.player_1_symbol else self.player_1_symbol

        print(f"Quantidade de jogadas realizadas: {self.amount_of_plays}")
        # Faz print do board após última jogada.
        self._print_current_board()

# inicializando e rodando objeto do jogo.
game = Tic_tac_toe_4x4_game('X', 'O', '-')
game.run_game()