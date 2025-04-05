def porcentagem_de_aumento(funcionario):
    if funcionario['Cargo'] == 'Tecnico':
        if funcionario['Anos de Serviço'] > 2:
            return '12%'
        else:
            return '10%'
        
    elif funcionario['Cargo'] == 'Especialista':
        if  funcionario['Anos de Serviço'] > 3:
            return '15%'
        else:
            return '12%'
    
    elif funcionario['Cargo'] == 'Operador':
        if funcionario['Anos de Serviço'] > 5:
            return '11%'
        else:
            return '9%'
        
    elif funcionario['Cargo'] == 'Assistente':
        if funcionario['Anos de Serviço'] >= 2:
            return '7%'
        else:
            return '5%'