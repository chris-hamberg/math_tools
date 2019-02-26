'''
Generate Polynomial Equations
'''
import random
import os, sys

template_string = '{0}x{1}' # coefficent variable exponent
exponents = {2: '\u00b2', 3: '\u00b3'}

def generate_terms():
    terms = []
    for power in range(2, random.randint(3,4)):
        terms.append(template_string.format(random.randint(1,9), exponents[power]))
    terms.reverse()
    terms.append('{0}x'.format(random.randint(1,9))) # 1x**1
    terms.append(str(random.randint(1,9))) # generate a constant
    return terms

def generate_operators(terms):
    polynomial = ''
    indicies = set()
    for i in range(0, len(terms)):
        indicies.add(random.randint(i, len(terms)-1))
    indicies = list(indicies)
    indicies.sort()
    for i in indicies:
        polynomial += terms[i] + ' ' + random.choice(['+', '-']) + ' '
    polynomial = ' '.join(polynomial.split()[:-1])
    if len(polynomial) < 4:
        return generate_operators(terms)
    return polynomial

def operation(poly1, poly2):
    if len(poly1) < len(poly2):
        poly1, poly2 = poly2, poly1
    operand = random.choice(['+', '-', 'x', '\u00f7'])
    if operand == '\u00f7':
        values = poly2.split()
        poly2 = ' '.join(values[:3])
    return '({0}) {1} ({2})'.format(poly1, operand, poly2), operand

def display(polynomial, operand):
    while True:
        os.system('clear')
        print('\n' + polynomial)
        print('\n[ENTER] to generate another polynomial.')
        print('"H" for help.')
        print('"Q" to quit.')
        val = input('\n>>> ')
        if val.lower() == 'h':
            display_rules(operand)
        else:
            return val or 'a'


def display_rules(sign):
    os.system('clear')
    polynomials = {
            'poly1': 'ax\u00b2 + c',
            'poly2': 'bx + d'
            }
    if sign == 'x':
        terms = {
                'x**2': 'x\u00b2',
                'x**3': 'x\u00b3',
                }
        polynomials.update(terms)
        print('''
 Multiplying Polynomials:

    1. Use the distributive property to distribute each term from the first
       polynomial, across the second polynomial.
    2. Add all of the terms together.
    3. Combine like terms if there are any.

    - ex.
            ({poly1}) * ({poly2})

            1. a{x**2}({poly2}) = ab{x**3} + a{x**2}d
               c({poly2})   = bxc + dc

            2. ab{x**3} + a{x**2}d + cbx + cd

            3. There are no like terms in the example.

'''.format(**polynomials))          
    elif sign == '+':
        print('''
 Adding Polynomials:

    1. Since addition is associative we can simply remove the parens.

    2. Perform the subsequent additions.
''')
    elif sign == '-':
        print('''
 Subtracting Polynomials:

    1. Given an expression such as: ({poly1}) - ({poly2})
       there is a negative 1 understood before the second set of parens. 
       Such that:
        
        ({poly1}) - ({poly2}) = ({poly1}) - 1({poly2})

    2. Distribute the negative one across the second set of parenthesized 
       values.
       
    3. Add each polynomial together.
'''.format(**polynomials))
    
    else:
        print('''
 Dividing Polynomials.

    1. Use Long Division

    2. Reference https://www.youtube.com/watch?v=vRxa2sSN0C0
''')
    input('Press Enter to Continue\n>>> ')

def main():
    while True:
        poly1 = generate_operators(generate_terms())
        poly2 = generate_operators(generate_terms())
        problem, operand = operation(poly1, poly2)
        if display(problem, operand).lower() == 'q':
            sys.exit(0)

if __name__ == '__main__':
    main()
