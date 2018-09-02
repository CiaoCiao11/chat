def read_file(filename):
    lines=[]
    with open(filename,'r',encoding='utf-8-sig') as f:
      for  line in f:
          lines.append(line.strip())
    
    return lines
def convert(lines):
    A_word=0
    A_stick=0
    A_photo=0
    V_word=0
    V_stick=0
    V_photo=0
    for line in lines:
        s=line.split(' ')
        name=s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
              A_stick+=1
            elif s[2] == '圖片':
              A_photo+=1
            else:
              for m in s[2:]:
                A_word+=len(m)
        if name == 'Viki':
            if s[2] == '貼圖':
              V_stick+=1
            elif s[2] == '圖片':
              V_photo+=1
            else:
              for m in s[2:]:
                V_word+=len(m)
    print('Allen:',A_word,'個字')
    print('Allen:',A_stick,'個貼圖')
    print('Allen:',A_photo,'個圖片')
    print('Viki:',V_word,'個字')
    print('Viki:',V_stick,'個貼圖')
    print('Viki:',V_photo,'個圖片')


    


def main():
    lines=read_file('-LINE-Viki.txt')
    convert(lines)
   
main()