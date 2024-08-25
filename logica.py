import logicaFunciones 

# prod evaluarFormula(formula_con_variables: list[str]) -> None {
#   requiere: {formula_con_variables debe tener al menos una variable y no debe estar vacia}
#   requiere: {Las operaciones son: -, OR, AND y parentesis (, )}
#   requiere: {Una variable no peude estar al lado de otra variables}
#   requiere: {Los negadores deben o estar adelante de una variable o de un parentesis}
#   requiere: {todos los parentesis deben estar correctos}
#   requiere: {Las variables no se pueden llamar como las operaciones}
#   requiere: {Una operaciones AND / OR, no puede estar al lado de otra AND/OR}
#   asegura: {muestra todas las posibles combinaciones de las variables}
#   asegura: {muestra la tabla de verdad tras evaluar la formula}
# }
def evaluarFormula(formula_con_variables: list[str]):
    logicaFunciones.evaluarConTodasLasPosibilidades(formula_con_variables)

formulaVariables: list[str] = ["-", "(", "P", "OR", "Q", ")"]    
formula: list[str] = ["-", "True", "OR", "-", "(", "False", "AND", "-", "TRUE", ")"]

def esMasFuerteQue(formula_a_ver_si_es_mas_fuerte: list[str], formula_para_comparar):
    formula_de_fuerza: list[str] = ["-", "("]
    for i in formula_a_ver_si_es_mas_fuerte:
        formula_de_fuerza.append(i)
    formula_de_fuerza.append(")")
    formula_de_fuerza.append("OR")
    formula_de_fuerza.append("(")
    for i in formula_para_comparar:
        formula_de_fuerza.append(i)
    formula_de_fuerza.append(")")
    return logicaFunciones.esTautologia(formula_de_fuerza, True)
    

#logicaFunciones.evaluarConTodasLasPosibilidades(formulaVariables)
#print(convertirNumeroDecimalEnBinario(16, 5))

print(esMasFuerteQue(["P", "AND", "Q"], ["P", "OR", "Q"]))