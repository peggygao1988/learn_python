from collections import deque


def search(lines, pattern, history=2):
    previous_lines = deque(maxlen=history)
    for line in lines:
        previous_lines.append(line)
        if pattern in line:
            yield line, previous_lines


if __name__ == '__main__':
    lines = ['hello girl morining boy',
             'world say hello, say hey',
             'i say hello, what up',
             'haha hi, new world',
             'all of me love all of your world',
             'hello new start'
             ]
    for line, prelines in search(lines, 'hello'):
        for l in prelines:
            print(l, end=';')
            print('\n')
        print(line, end='.')
        print('-'*20)
