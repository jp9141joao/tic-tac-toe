# **Jogo da Velha (Tic Tac Toe)**

Este é um projeto em Python que implementa o clássico jogo da velha no terminal. O jogo oferece dois modos: **Jogar sozinho** (contra o computador com diferentes níveis de dificuldade) e **Jogar com um amigo** (modo multiplayer). 

---

## **Funcionalidades**

### **Modos de Jogo**
1. **Jogar sozinho:** 
   - Enfrente o computador com dificuldades ajustáveis:
     - **Fácil:** Movimentos básicos.
     - **Médio:** Estratégia intermediária.
     - **Difícil:** Desafie sua habilidade!
2. **Jogar com um amigo:** 
   - Participe de uma partida no modo multiplayer, jogando no mesmo computador.

### **Regras do Jogo**
- O tabuleiro é composto por 9 posições numeradas de 1 a 9.
- Cada jogador alterna entre as marcas `X` e `O`.
- O vencedor é aquele que alinha três de suas marcas horizontalmente, verticalmente ou diagonalmente.
- Caso todas as posições sejam preenchidas sem um vencedor, o jogo termina em empate.

---

## **Como Jogar**

1. Execute o programa no terminal.
2. Escolha um modo no menu inicial:
   - **1** para jogar contra o computador.
   - **2** para jogar com um amigo.
   - **3** para sair do jogo.
3. No modo **Jogar sozinho**, selecione o nível de dificuldade.
4. Digite o número correspondente à posição desejada para fazer sua jogada.
5. O placar é atualizado automaticamente após cada rodada.

---

## **Exemplo de Layout do Tabuleiro**
Antes de cada jogada, o tabuleiro é exibido assim:

```
 1  |  2  |  3  
----------------
 4  |  5  |  6  
----------------
 7  |  8  |  9  
```

Após as jogadas, as posições selecionadas são substituídas por `X` ou `O`. 

---

## **Dependências**
- **Python 3.6+**
- Biblioteca `os` (já incluída nas distribuições padrão do Python).

---

## **Como Executar**

1. Certifique-se de ter o Python 3 instalado no seu sistema.
2. Baixe o código-fonte e salve-o em um arquivo chamado `jogo_da_velha.py`.
3. Abra o terminal e navegue até o diretório onde o arquivo está salvo.
4. Execute o comando:
   ```bash
   python jogo_da_velha.py
   ```

Divirta-se e bons jogos! 😊
