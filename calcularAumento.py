def calcular_aumento(funcionario):
    if funcionario['Cargo'] == 'Tecnico':
        if funcionario['Anos de Serviço'] > 2:
            return funcionario['Salario'] * 1.12
        else:
            return funcionario['Salario'] * 1.10
        
    elif funcionario['Cargo'] == 'Especialista':
        if  funcionario['Anos de Serviço'] > 3:
            return funcionario['Salario'] * 1.15
        else:
            return funcionario['Salario'] * 1.12
    
    elif funcionario['Cargo'] == 'Operador':
        if funcionario['Anos de Serviço'] > 5:
            return funcionario['Salario'] * 1.11
        else:
            return funcionario['Salario'] * 1.09
        
    elif funcionario['Cargo'] == 'Assistente':
        if funcionario['Anos de Serviço'] >= 2:
            return funcionario['Salario'] * 1.07
        else:
            return funcionario['Salario'] * 1.05