import random

class Termo_game:
    """_summary_
        Jogo Termo: joga-se como um jogo da forca. Após cada tentativa do jogador, é checado se houve uma letra marcada
        no mesmo índice que da palavra a ser adivinhada, se isso ocorrer a letra deve ser "pintada" de azul, se o jogador
        seleciona uma letra existente em uma posição errada, a letra se torna amarela. o case da letra é irrelevante,
        pois em todas comparações tanto a palavra sorteada quanto a tentativa são tranformados em upper case.

        O construtor recebe a quantidade de tentativas que o jogador tem para adivinhar a palavra e o path para um arquivo txt que contém as palavras.
        A palavra que o jogador deve adivinhar é selecionada aleatóriamente, se o jogador não inserir a quantidade necessária de letras
        para adivinhara palavra, é requisitado que insira até que ele o faça. As palavras do txt são carregadas em uma lista durante a execução do jogo.
    """
    def __init__(self, amount_of_tries: int, archive_path: str) -> None:
        """_summary_
            O construtor recebe a quantidade de tentativas que o jogador terá para adivinhar a palavra e o caminho para o arquivo txt com a lista de palavras.
            São recebidos como args: amount_of_tries para indicar as tentativas que o jogador terá para vencer o jogo e archive_path para receber o local da lista de arquivos.
        Args:
            amount_of_tries (int): Quantidade de tentativas que o jogador terá até acertar palavra.
            archive_path (str): caminho até arquivo lista_palavras.txt.
        """
        self.archive_path = archive_path
        self.amount_of_tries = amount_of_tries
        self.current_word = '' # Armazena a palavra escolhida aleatóriamente do arquivo lista_palavras.txt.
        self.player_guess = '' # Armazena a palavra inserida na tentativa "atual" do jogador.
        self.words_list = [] # Lista para carregar palavras do arquivo em memória.
        self.guess_history = [] # Lista com histórico de tentativas do  jogador.

    def _load_words_from_file(self) -> None:
        """_summary_
            Percorre arquivo com as palavras do jogo, remove espaços em brancos e carrega palavras em memória na lista.
            É necessário que cada palavra esteja em uma linha no txt.
        """
        with open(self.archive_path, 'r') as archive:
            # Lê as linhas do arquivo e remove espaços em branco, insere na lista.
            self.words_list = [line.strip() for line in archive]

    def _make_letter_blue(self, letter: str) -> str:
        """_summary_
            Recebe uma letra e a deixa azul (indica que letra adivinhada esta no local correto).
        Args:
            letter (str): letra escolhida pelo player no local correto.
        """
        return "\033[34m" + letter + "\033[0m"

    def _make_letter_yellow(self, letter: str) -> str:
        """_summary_
            Recebe uma letra e a deixa amarela (indica que a letra adivinhada existe na palavra, mas está no local errado).
        Args:
            letter (str): letra escolhida pelo player que existe na palavra mas está no local errado.
        """
        return "\033[33m" + letter + "\033[0m"

    def _check_matching_letters(self, attempt_number):
        """_summary_
            Identifica letras enviadas pelo player e aplica coloração azul ou amarela se estiverem presentes na palavra a ser adivinhada.
        """
        # Transforma string (imutável) em lista (mutável).
        current_word_list = list(self.player_guess)
        # Percorre palavra.
        for i in range(len(self.current_word)):
            # Se letras da palavra de tentativa está no mesmo índice da palavra, aplica azul na letra.
            if (self.player_guess[i].upper() == self.current_word[i].upper()):
                current_word_list[i] = self._make_letter_blue(self.player_guess[i])
            # Se letra presente na tentativa está contida na palavra, aplica cor amarela na letra.
            elif (self.player_guess[i].upper() in self.current_word.upper()):
                current_word_list[i] = self._make_letter_yellow(self.player_guess[i])
        # Converte a lista de letras de volta para uma string.
        checked_player_guess = ''.join(current_word_list)
        # Adiciona tentativa no histórico de tentativas.
        self.guess_history.append(f'{attempt_number} - {checked_player_guess}')

    def _get_player_input(self):
        """_summary_
            Valida se tentativa do jogador é menor que a quantidade de caracteres necessários para adivinhar a palavra.
        Args:
            player_input (str): input referente à tetativa de adivinhar a palavra.
        """
        self.player_guess = input(f'Adivinhe a palavra: ')
        while(len(self.player_guess) != 5):
            self.player_guess = input(f'Você deve inserir {len(self.current_word)} letras para adivinhar a palavra. insira novamente: ')

    def run_game(self) -> None:
        # Carrega palavras do txt em memória.
        self._load_words_from_file()
        # Adquire um palavra aleatória vinda do arquivo txt na variável self.current_word.
        self.current_word = random.choice(self.words_list)
        print('--- Iniciado o jogo Termo! ---\n')
        print(f'Você tem {self.amount_of_tries} tentativas para adivinhar a palavra misteriosa que possui {len(self.current_word)} caracteres!')
        print(f'Letras adivinhadas nos locais corretos ficam na cor azul, letras nos locais incorretos mas presentes na palavra ficam amarelas.')
        print(f'Suas tentativas devem ter {len(self.current_word)} letras.')
        print('Vamos começar!!!\n')
        # variável de controle para tentativas do jogo.
        attempt = 1
        # loop principal.
        while True:
            print(f'Tentativa {attempt}:')
            self._get_player_input()
            # Check play.
            self._check_matching_letters(attempt)
            # Faz print de todas tentativas até o momento.
            for word in self.guess_history: print(word)
            # Condições para fim do jogo: se jogador acertar todas posições antes de esgotar tentativas.
            if (self.current_word.upper() == self.player_guess.upper()):
                print('A palavra foi adivinhada! :)\n')
                break
            # Jogo acaba com tentativas esgotadas.
            elif(self.amount_of_tries == attempt):
                print('A quantidade de tentativas acabou, você perdeu :(\n')
                break
            # Aumenta quantidade de tentativas.
            attempt += 1
        # Fim do jogo
        print(f'A palavra era -> {self.current_word} \nFim de jogo!')

game = Termo_game(6, './lista_palavras.txt')
game.run_game()
