class Tic_tac_toe_NxN_game:
    """_summary_
        Classe que gerencia um jogo da velha de tamanhao variável (NxN) que pode ser jogado por dois jogadores no console.
        Os jogadores devem escolher o tamanho o tabuleiro com um inteiro, símbolos para representar suas jogadas,
        como: X ou O e um símbolo para representar o tabuleiro. Os símbolos não devem repetir e devem ter o tamaho de um (1) caractere.
        Um jogador deve seleciona o índice da linha e coluna que deseja fazer sua jogada, ganha aquele que completar uma fileira
        com seu símbolo na vertical, diagonal, ou horizontal, se todos campos são preenchidos ninguém ganham (empate).

        O grid que representa o "tabuleiro" é uma matriz NxN, a cada jogada é checado o estado do jogo de acordo 
        com os símbolos na matriz. Enquanto a matriz não é completamente preenchida ou um jogador ganha, o jogo continua.
    """
    def __init__(self, player_1_symbol: str, player_2_symbol: str, board_symbol: str,
                    board_size: int) -> None:
        """_summary_
            O construtor recebe os valores para gerenciar as escolhas do jogador, é validado se símbolos repetidos foram apresentados.
            O board é inicializado como uma lista vazia e a quantidade de jogadas com 0.
        Args:
            player_1_symbol (str): Símbolo esolhido pelo player 1.
            player_2_symbol (str): Símbolo esolhido pelo player 2.
            board_symbol (str): Símbolo ecolhido para representar os grids do tabuleiro.
            board_size (int): Tamanho das linhas e colunas formando um tabuleiro quadrado.
        """
        self.player_1_symbol = player_1_symbol
        self.player_2_symbol = player_2_symbol
        self.board_symbol = board_symbol
        self.board_size = board_size
        self.board = [] # Matriz que contém o tabuleiro.
        self.amount_of_plays = 0 # Contador da quantidade de jogadas.
        # Faz validação dos símbolos e valores dos jogadores.
        self._validate_players_options()
    
    def _valid_symbols(self) -> bool:
        """_summary_
            Valida se os símbolos para os player no tabuleiro tem um caractere e se não repetem.
        Returns:
            bool: Retorna falso caso símbolos forem maiores que um caractere ou repetidos.
        """
        # Se uma das validações não passou, retorna False.
        return (
            len(self.player_1_symbol) == 1
            and len(self.player_2_symbol) == 1
            and len(self.board_symbol) == 1
            and self.player_1_symbol != self.player_2_symbol 
            and self.player_1_symbol != self.board_symbol
            and self.player_2_symbol != self.board_symbol
        )
    
    def _recieve_int_board_size(self):
        """_summary_
            Cria loop que ocorre até receber valor para o tamano do board válido.
        """
        while True:
            try:
                self.board_size = int(input('Insira um int para o tamanho do quadrado do tabuleiro: '))
            except ValueError:
                print('É necessário inserir um número int!')
                continue
            # Sem exceção - quebra loop.
            break

    def _generate_board(self) -> None:
        """_summary_
            Faz o set do board NxN preenchendo os campos da matriz com o símbolo escolhido pelos jogadores.
        """
        self.board = [[self.board_symbol for i in range(self.board_size)] for j in range(self.board_size)]
    
    def _validate_players_options(self) -> None:
        """_summary_
            Valida se os jogadores inseriram símbolos repetidos ou maiores que 1 (uma string ao invés de somente um caractere)
            e lança mensagem até que valores diferentes sejam fornecidos. Após validação inicializa o board.
        """
        # Enquanto não recebe símbolos válidos, pede por novos inputs.
        while (not self._valid_symbols()):
            print('Símbolos identificadores devem ser diferentes para os players e o board e devem ter um (1) caractere de tamanho! Insira outros valores.')
            self.player_1_symbol = input("Símbolo do player 1: ")
            self.player_2_symbol = input("Símbolo do player 2: ")
            self.board_symbol = input("Símbolo para o tabuleiro: ")
        # Enquanto não recebe o valor para tamanho válido, pede por novo input.
        while (self.board_size <= 1):
            print('Valor informado para tamanho do tabuleiro deve ser maior que 1.')
            self._recieve_int_board_size()
               
        # Com os valores válidos, inicializa o board.
        self._generate_board()

    def _is_left_diag_complete(self, player_symbol: str) -> bool:
        """_summary_
            Retorna se diagonal esquerda foi completada com símbolo do jogador e finalizou o jogo.
        Args:
            player_symbol (str): Símbolo do jogador atual.

        Returns:
            bool: bool para identificar se player completou diagonal e ganhou.
        """
        return all(self.board[i][i] == player_symbol for i in range(self.board_size))
    
    def _is_right_diag_complete(self, player_symbol: str) -> bool:
        """_summary_
            Retorna se diagonal direita foi completada com símbolo do jogador e finalizou o jogo.
        Args:
            player_symbol (str): Símbolo do jogador atual.

        Returns:
            bool: bool para identificar se player completou diagonal e ganhou.
        """
        return all(self.board[i][self.board_size - 1 - i] == player_symbol for i in range(self.board_size))
    
    def _is_game_playing(self, player_symbol: str) -> bool:
        """_summary_
            Determina se o jogo deve continuar retornando um booleano (False é fim do jogo),
            checa condições para mandar mensagem de vitória ou empate (todos campos marcados).
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
        for column in range(self.board_size):
            # O for percorre todos os itens da matriz, 
            if all(self.board[row][column] == player_symbol for row in range(self.board_size)):
                self._victory_message(player_symbol)
                game_continue = False

        # Verificar vitória nas diagonais.
        if (self._is_left_diag_complete(player_symbol) or self._is_right_diag_complete(player_symbol)):
            self._victory_message(player_symbol)
            game_continue = False

        # Verifica se todos os campos foram preenchidos e não houve vitória de nenhum jogador.
        if (all(all(field != self.board_symbol for field in row) for row in self.board)):
            print(f"Empate! Ninguém ganhou.\nFim do jogo da velha {self.board_size}x{self.board_size}.")
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
            bool: falso se valores inseridos estão fora do intervalo da matriz.
        """
        # Retorno default é True.
        result = True
        if ((row < 0 or row > self.board_size) or (column < 0 or column > self.board_size)):
            print(f"É necessário inserir um número maior ou igual a 0 e menor ou igual a {self.board_size} para fazer a jogada.")
            result = False
        elif self.board[row][column] != self.board_symbol:
            print("Esse campo já foi preenchido. Escolha outro.")
            result = False
        # Faz retorno
        return result
    
    def _make_play(self, current_player_symbol: str) -> None:
        """_summary_
            Identifica o símbolo do jogador atual e o grid onde o jogador deseja jogar.
            Faz a jogada se os símbolos são váidos e o campo escolhido ainda não foi preenchido.
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
                print(f"É necessário inserir um int válido maior ou igual a 0 e menor ou igual a {self.board_size} para fazer a jogada.")
                continue
            if (self._validate_play(row, column)):
                # Se jogador tenta fazer jogada em campo válido, quebra loop.
                break
            # Faz print do board novamente para que os players possam visualizar onde fazer a jogada.
            self._print_current_board()
            
        # Coloca o símbolo do jogador no campo (faz a jogada).
        self.board[row][column] = current_player_symbol
        # Aumenta a quantidadede jogadas.
        self.amount_of_plays += 1

    def _print_current_board(self):
        """_summary_
            Faz o set do board preenchendo os campos da matriz com o símbolo escolhido pelos jogadores.
            Faz print com os índices das respectivas linhas e colunas para facilitar a identificação no grid.
        """
        # Imprimir os índices das colunas
        col_indexes = ' '.join([str(i) for i in range(self.board_size)])
        print('  ' + col_indexes)
        for i in range(self.board_size):
            # Imprimir os índices das linhas
            print(i, end=' ')
            # Faz print dos símbolos dos grids da matriz.
            for j in range(self.board_size):
                print(self.board[i][j], end=' ')
            # Print para fazer quebra no final de cada 'row'.
            print()

    def _victory_message(self, player_symbol: str) -> None:
        """_summary_
            Faz o print de uma mensagem de vitória com o símbolo do jogador vencedor.
        Args:
            player_symbol (str): Símbolo do jogador vencedor.
        """
        print(f"O jogador com símbolo -> {player_symbol} ganhou !!!\nFim do joga da velha {self.board_size}x{self.board_size}.")

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
game = Tic_tac_toe_NxN_game('X', 'O', '-', 1)
game.run_game()