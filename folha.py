# Informação das tabelas de INSS e IRRF

tabela_inss_2023 = {
    'inss1': 7.5,
    'inss2': 9,
    'inss3': 12,
    'inss4': 14
}

base = {
    '1903.98': 'irrf1',
    '> 1903.98 <= 2826.65': 'irrf2',
    '> 2826.65 <= 3751.06': 'irrf3',
    '> 3751.06 <= 4664.68': 'irrf4',
    '> 4664.68': 'irrf5'
}

tabela_irrf_2023 = {
    'irrf1': "Isento",
    'irrf2': [7.5, 142.80],
    'irrf3': [15, 354.80],
    'irrf4': [22.50, 636,13],
    'irrf5': [27.5, 869.36],
    'dependente': 189.59,
    'qtde_dependente': 3
}

# Calcula INSS
def desconto_inss(salario):
    faixa_salarial = {}
    if salario <= 1302:
        faixa1 = {'base': salario, 'inss': salario * 0.075}
        faixa_salarial['faixa1'] = faixa1
        desconto_inss = faixa1['inss']
    elif salario > 1302 and salario <= 2571.29:
        faixa1 = {'base': 1302, 'inss': 1302 * 0.075}
        faixa2 = {'base': (salario - 1302), 'inss': (salario - 1302) * 0.09}
        faixa_salarial['faixa1'] = faixa1
        faixa_salarial['faixa2'] = faixa2
        desconto_inss = faixa1['inss'] + faixa2['inss']
    elif salario > 2571.29 and salario <= 3856.94:
        faixa1 = {'base': 1302, 'inss': 1302 * 0.075}
        faixa2 = {'base': (2571.29 - 1302), 'inss': (2571.29 - 1302) * 0.09}
        faixa3 = {'base': (salario - 2571.29), 'inss': (salario - 2571.29) * 0.12}
        faixa_salarial['faixa1'] = faixa1
        faixa_salarial['faixa2'] = faixa2
        faixa_salarial['faixa3'] = faixa3
        desconto_inss = faixa1['inss'] + faixa2['inss'] + faixa3['inss']
    elif salario > 3856.94 and salario <= 7507.49:
        faixa1 = {'base': 1302, 'inss': 1302 * 0.075}
        faixa2 = {'base': (2571.29 - 1302), 'inss': (2571.29 - 1302) * 0.09}
        faixa3 = {'base': (3856.94 - 2571.29), 'inss': (3856.94 - 2571.29) * 0.12}
        faixa4 = {'base': (salario - 3856.94), 'inss': (salario - 3856.94) * 0.14}
        faixa_salarial['faixa1'] = faixa1
        faixa_salarial['faixa2'] = faixa2
        faixa_salarial['faixa3'] = faixa3
        faixa_salarial['faixa4'] = faixa4
        desconto_inss = faixa1['inss'] + faixa2['inss'] + faixa3['inss'] + faixa4['inss']
    else:
        faixa1 = {'base': 1302, 'inss': 1302 * 0.075}
        faixa2 = {'base': (2571.29 - 1302), 'inss': (2571.29 - 1302) * 0.09}
        faixa3 = {'base': (3856.94 - 2571.29), 'inss': (3856.94 - 2571.29) * 0.12}
        faixa4 = {'base': (7507.49 - 3856.94), 'inss': (7507.49 - 3856.94) * 0.14}
        faixa_salarial['faixa1'] = faixa1
        faixa_salarial['faixa2'] = faixa2
        faixa_salarial['faixa3'] = faixa3
        faixa_salarial['faixa4'] = faixa4
        desconto_inss = faixa1['inss'] + faixa2['inss'] + faixa3['inss'] + faixa4['inss']
    return desconto_inss, faixa_salarial

# Calculando IRRF

# base_irrf = salario - desconto_inss

# total_dependente = dependente - qtde_dependente

#desconto_ir = ((base_irrf * aliquota_ir) - decucao) - total_dependente

