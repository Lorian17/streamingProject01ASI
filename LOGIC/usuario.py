usuarios = []

def adicionar_usuario(cpf, nome, email, senha):    
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            return u
    return None

def remover_usuario(cpf):
    for u in usuarios:
        if (u[0] == cpf):
            usuarios.remove(u)
            return True
    return False
	
def iniciar_usuarios():
    adicionar_usuario(22222,"joao", "joao@gmail.com", 313517357)
    adicionar_usuario(33333,"maria", "maria@gmail.com",741481485)
