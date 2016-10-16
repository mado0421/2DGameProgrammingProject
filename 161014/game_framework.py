class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


class TestGameState:

    def __init__(self, name):
        self.name = name

    def enter(self):
        print("State [%s] Entered" % self.name)

    def exit(self):
        print("State [%s] Exited" % self.name)

    def pause(self):
        print("State [%s] Paused" % self.name)

    def resume(self):
        print("State [%s] Resumed" % self.name)

    def handle_events(self):
        print("State [%s] handle_events" % self.name)

    def update(self):
        print("State [%s] update" % self.name)

    def draw(self):
        print("State [%s] draw" % self.name)


running = None
stack = None


def change_state(state):
    global stack
    pop_state()         # 이전 상태를 날려버림
    stack.append(state) # 스택에 state를 넣고
    state.enter()       # 그 상태를 시작


def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()


def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()    # 마지막 상태의 exit()를 호출
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]   # 스택을 리스트로 구현함
    start_state.enter()     # 현재 상태의 enter()를 호출함
    while (running):
        stack[-1].handle_events()   # 스택의 마지막 상태의 ~()를 호출함
        stack[-1].update()          # update()에서 상태를 바꿔주는걸 넣어놓기 때문에 이 때 바뀜
        stack[-1].draw()
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()


def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)


if __name__ == '__main__':
    test_game_framework()
