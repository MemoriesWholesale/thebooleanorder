#challenge description link: https://www.codewars.com/kata/59eb1e4a0863c7ff7e000008

def solve(s,ops):
    base_string = ''
    for i in range(len(s)):
        base_string += s[i]
        if i + 1 == len(s):
            break
        base_string += ops[i]
        
    def catalanize(string):
        
        if len(string) == 1:
            return string
        if len(string) == 3:
            return ['('+ string +')']
        
        result = []
        
        for i in range(len(string)):
            
            if string[i] in {'&','|','^'}:
                head = catalanize(string[:i])
                tail = catalanize(string[i+1:])
                for j in head:
                    for k in tail:
                        result.append('('+ j + ')' + string[i] + '(' + k + ')')
        
        return result
    
    def primitive(string):
        if string in {'(t)', 't&t', 't|t', 't|f', 'f|t', 't^f', 'f^t'}:
            return 't'
        if string in {'(f)', 'f&f', 'f&t', 't&f', 'f|f', 'f^f', 't^t'}:
            return 'f'
    
    def booleanize(string):
        if primitive(string) in {'t','f'}:
            return primitive(string)
        result = ''
        for i in range(len(string)):
            if primitive(string[i:i+3]) in {'t','f'}:
                result = string[:i] + primitive(string[i:i+3]) + string[i+3:]
        return booleanize(result)
                
    count = 0
    for i in catalanize(base_string):
        if booleanize(i) == 't':
            count += 1
    
    return count