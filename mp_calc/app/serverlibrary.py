

def merge(array, p, q, byfunc):
    
    len_p = len(p)
    len_q = len(q)

    i=j=k=0
    
    while i < len_p and j<len_q:
        if byfunc(p[i]) <= byfunc(q[j]):
            array[k] = p[i]
            i += 1
            k += 1

        else:
            byfunc(p[i]) > byfunc(q[j])
            array[k] = q[j]
            j += 1
            k += 1
        
    while i < len_p:
        array[k] = p[i]
        i += 1
        k += 1
    while j < len_q:
        array[k] = q[j]
        j += 1
        k += 1

def mergesort(array, byfunc=None):
    if len(array) > 1:
        mid = len(array) // 2
        lft = array[:mid]
        rgt = array[mid:]

        mergesort(lft, byfunc)
        mergesort(rgt, byfunc)

        merge(array, lft, rgt, byfunc)
    return array

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        pass

    def pop(self):
        if len(self.__items)!=0:
            a = self.__items[-1]
            self.__items.pop(-1)
            return a
        else:
            return None
        pass

    def peek(self):
        if len(self.__items)!=0:
          return self.__items[-1]
        else: 
          return None 
        pass

    @property
    def is_empty(self):
        return len(self.__items)==0
        pass

    @property
    def size(self):
        return len(self.__items)
        pass

class EvaluateExpression:
    def __init__(self, string=""):
        self._expr = string
        self.valid_char = '0123456789+-*/() '
        self.operators = '+-*/()'
        
    @property
    def expression(self):
        return self._expr

    @expression.setter
    def expression(self, new_expr):
        valid_char = '0123456789+-*/() '
        tf = True
        for i in new_expr:
            if i not in valid_char:
                tf = False
                break
        if tf == True:
            self._expr = new_expr
        else:
            self._expr = ""

    def insert_space(self):
        i = 0
        while i < len(self._expr):
            if self._expr[i] in '+-*/()':
                self._expr = self._expr[:i] + ' ' + self._expr[i] + ' ' + self._expr[i+1:]
                i += 3
            else:
                i += 1
        return self._expr


    def process_operator(self, operand_stack, operator_stack):
        op = operator_stack.peek()
        op1 = operand_stack.pop()
        op2 = operand_stack.pop()

        if op == "+":
            result = op2 + op1
        elif op == "-":
            result = op2 - op1
        elif op == "*":
            result = op2 * op1
        elif op == "/":
            result = op2 // op1
                        
        operator_stack.pop()
        operand_stack.push(result)
        
    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        for char in tokens:

            if char in '0123456789':
                operand_stack.push(int(char))
            elif char in '+-':
                if not operator_stack.peek() == '(' and not operator_stack.peek() == ')' and operator_stack.peek() != None:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(char)
            
            elif char in '*/':
                if operator_stack.peek() == '*' or operator_stack.peek() == '/':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(char)
                        
            elif char == '(':
                operator_stack.push(char)

            elif char == ')':
                while operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
                
        while operator_stack.peek() != None:
            self.process_operator(operand_stack, operator_stack)
                
        return operand_stack.pop()

def get_smallest_three(challenge):
    records = challenge.records
    times = [r for r in records]
    mergesort(times, lambda x: x.elapsed_time)
    return times[:3]
