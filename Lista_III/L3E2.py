usuario = input ('Nome de usuário: ')
senha = input ('Senha: ')
while senha == usuario :
    print ('Senha inválida! A senha não deve ser igual ao nome de usuário.')
    usuario = input ('Nome de usuário: ')
    senha = input ('Senha: ')
print ('Cadastro realizado com sucesso!')
