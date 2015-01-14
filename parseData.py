# We want to implement a function parse(line) => [strings]
def parse(line):
    p = []
    quote = 0
    value = ""
    for c in range(len(line)):
        if line[c] == '"':
            quote += 1
            if not (c < len(line)-1):
                if not (value == ""):
                    #if (line[c+1] != ","):
                    #if not (line[c+1] == '"'):
                    value += line[c]
        elif line[c] == ",":
            if quote%2 == 0:
                p.append(value)
                value = ""
            else:
                value += line[c]
        else:
            value += line[c]
    if value[-1] == '"':
        value = value[:-1]
    p.append(value)
    return p

def p(parsed):
    print '|',
    for p in parsed:
        print p, '|',
    print

p(parse("John,Smith,john.smith@gmail.com,Los Angeles,1"))          # John|Smith|john.smith@gmail.com|Los Angeles|1	   
p(parse('Jane,Robin,jane@msn.com,"San Francisco, CA",0'))	   # Jane|Roberts|janer@msn.com|San Francisco, CA|0
p(parse('"Alexandra""Alex""",Mando,alex.mando@gmail.com,Miami,1')) # Alexandra "Alex"|Menendez|alex.menendez@gmail.com|Miami|1
p(parse('one,two,,four,"five"'))				   # one|two||four|five
