import re

fich=open("salida.txt","w")

def do_cmd(fn):
    def final(before, instr):
        after = list(before)
        after[instr[3]] = fn(before, instr[1], instr[2])
        return after
    return final

addr = do_cmd(lambda before,x,y: before[x]+before[y])
addi = do_cmd(lambda before,x,y: before[x]+y)
mulr = do_cmd(lambda before,x,y: before[x]*before[y])
muli = do_cmd(lambda before,x,y: before[x]*y)
banr = do_cmd(lambda before,x,y: before[x] & before[y])
bani = do_cmd(lambda before,x,y: before[x] & y)
borr = do_cmd(lambda before,x,y: before[x] | before[y])
bori = do_cmd(lambda before,x,y: before[x] | y)
setr = do_cmd(lambda before,x,y: before[x])
seti = do_cmd(lambda before,x,y: x)
gtir = do_cmd(lambda before,x,y: 1 if x > before[y] else 0)
gtri = do_cmd(lambda before,x,y: 1 if before[x] > y else 0)
gtrr = do_cmd(lambda before,x,y: 1 if before[x] > before[y] else 0)
eqir = do_cmd(lambda before,x,y: 1 if x == before[y] else 0)
eqri = do_cmd(lambda before,x,y: 1 if before[x] == y else 0)
eqrr = do_cmd(lambda before,x,y: 1 if before[x] == before[y] else 0)

cmds = [ addr, addi
       , mulr, muli
       , banr, bani
       , borr, bori
       , setr, seti
       , gtir, gtri, gtrr
       , eqir, eqri, eqrr
       ]

options = {}
for code in range(16):
    options[code] = list(enumerate(cmds))

lines = open('inputTest.txt').read().strip()
lines = lines.strip().split('\n')
ans = 0
for i in range(0, len(lines), 4):
    if 'Before' in lines[i]:
        assert 'After:' in lines[i+2]
        before = list(map(int, re.findall('-?\d+', lines[i])))
        instr = list(map(int, re.findall('-?\d+', lines[i+1])))
        after = list(map(int, re.findall('-?\d+', lines[i+2])))
        options[instr[0]] = [(idx,fn) for (idx,fn) in options[instr[0]] if fn(before,instr) == after]

        matches = 0
        for idx,cmd in options[instr[0]]:
            if cmd(before, instr) == after:
                matches += 1
        if matches >= 3:
            fich.write(str(instr)+"\n")
            ans += 1

print(ans)
