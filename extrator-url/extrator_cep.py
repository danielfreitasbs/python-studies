endereco = "Rua das Flores 78, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re  # Regular Expression -- RegEx -- faz parte da lib padrao

# 5 digitos + hifen(opcional) + 3 digitos

padrao = re.compile(
    "[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match

if busca:
    cep = busca.group();
    print(cep)
