def find_min_in_rotated_array(nums):
    if len(nums) == 1: # array com um elemento
        return nums[0]
    while True:
        if nums[0] < nums[-1]: # array ordenado
            return nums[0]
        if len(nums) == 3: # array com 3 elementos não ordenados
            nums = nums[1:]
        if len(nums) == 2:  # array com 2 elementos
            return nums[0] if nums[0] < nums[1] else nums[1]  # min(nums)? O(2)

        # Fatia a lista
        meio = len(nums) // 2
        if nums[0] < nums[meio-1]:  # esquerda está ordenada
            nums = nums[meio:]  # pego a direita
        else:
            nums = nums[:meio]  # pego a esquerda

'''
Explicação
1. O processo se baseia no fatiamento da lista, em esquerda e direita.
2. Se a da esquerda está ordenada, jogo a esquerda fora e fico com a direita
3. Caso contrário, fico com a esquerda

Observação: olho primeiro a da esquerda, pois lemos da esquerda para a direita
e o ordenamento que nos importa está neste slice (esquerda). Não existe a 
possibilidade de ambas estarem desordenadas, apenas de ambas estarem ordenadas.
Neste caso, sei que o mínimo está na direita, então a pego e ela passará no 
primeiro teste.

4. É essa lista escolhida que eu testo se está ordenada e, em caso positivo,
retorno o primeiro valor da lista. Isso é o que sai do loop infinito.

Casos de borda:
1. A princípio, se a matriz só tem um elemento, que deveria ser o mínimo (depende
da forma do fatiamento). Mas seguimos, isso ficará mais claro.
2. Com o fatiamento teremos, inevitavelmente alguns casos de borda (após cada 
iteração em que a lista é fatiada, sempre teremos uma lista com um elemento e uma
com dois ou duas listas com 2 elementos) - aqui tratamos as situações de saída:
    2.1 Se a lista tiver 4 elementos, ela ainda entrará na divisão em duas listas 
        retornando duas listas de dois elementos. A comparação da lista da esquerda
        ainda retornará a lista correta (esquerda ou direita), mesmo no caso 
        [3, 4] e [1,2]. Como ele vai ver primeiro a esquerda (ordenada), vai me 
        retornar a lista certa (direita), com 2 elementos ordenados [1,2]
    2.2 lista com com 3 elementos  só tem uma opção de estar ordenada [1, 2, 3].
        Este é o caso em que teremos o problema, pois, se fatiadas, retornariam 
        listas [1] e [2,3], que eliminaria a lista [1] e retornaria o valor errado 
        (2). Por isso não fatiaríamos, caindo no caso do teste ordenado. Mas, se 
        não passar nesse teste ([3,1,2] ou [2.3.1]) basta eliminar o primeiro 
        elemento e teremos uma lista de dois elementos ([1,2] ou [3,1])
    2.3 Uma lista com 2 elementos, então, pode apenas retornar o primeiro (se ele
        for menor) ou o segundo, em caso contrário. 
    2.3 Se a lista diver 5 elementos, ela será quebrada em uma de 2 e uma de três
        elementos. Daí precisarmos das exceções com 2 e 3 elementos. Mas há um 
        porém: podemos ter as listas [4,5] e [1,2,3]. Por conta disso, precisarmos 
        olhar sempre primeiro para a esquerda para tomar a decisão do lado que 
        seguirá (olhando primeiro para a esquerda, retornará, ainda que ordenada, 
        a da direita)
3. E por que testar duas vezes se a lista está ordenada (uma antes e outra depois
de entrar no while True? Só porque testei e isso reduziu em quase 50% o tempo
total de execução, jogando o meu tempo inferior a 83% dos demais. Me parece, então,
que evitar ao máximo a entrada no loop é bem eficiente. 
'''