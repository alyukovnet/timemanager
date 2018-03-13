from .neural import NeuralNetwork
from .data import neural_types
from datetime import date
import numpy as np
import pickle

phys_net = NeuralNetwork()
chem_net = NeuralNetwork()
gum_net = NeuralNetwork()


def load():
    global phys_lessons, chem_lessons, gum_lessons, work_queue
    with open('lessons', 'rb') as f:
        phys_lessons, chem_lessons, gum_lessons = pickle.load(f)
    with open('queue', 'rb') as f:
        work_queue = pickle.load(f)


def what_network(x):
    nets = (phys_net, chem_net, gum_net)
    for borders, net in neural_types.items():
        if borders[0] <= x <= borders[1]:
            return nets[net]


def clear_queue():
    global work_queue
    work_queue = []
    with open('queue', 'wb') as f:
        pickle.dump(work_queue, f)


def clear_nn():
    global phys_lessons, chem_lessons, gum_lessons
    phys_lessons = []
    chem_lessons = []
    gum_lessons = []
    with open('queue', 'wb') as f:
        pickle.dump(work_queue, f)


def train():
    for _ in range(5000):
        for input_stat, correct_predict in phys_lessons:
            phys_net.train(np.array(input_stat), correct_predict)
    for _ in range(5000):
        for input_stat, correct_predict in chem_lessons:
            chem_net.train(np.array(input_stat), correct_predict)
    for _ in range(5000):
        for input_stat, correct_predict in gum_lessons:
            gum_net.train(np.array(input_stat), correct_predict)


def actual(date_start):
    return (date.today() - date_start).days


def deadline(date_deadline):
    return (date_deadline - date.today()).days


def to_queue(lesson, work_type, date_start, date_end, time_m, pri):
    inputs = [actual(date_start), deadline(date_end), time_m, pri]
    predict = what_network(lesson).predict(np.array(inputs))[0]
    line = [lesson, work_type, date_start, date_end, time_m, pri, predict]  # Memory line
    work_queue.append(line)
    with open('queue', 'wb') as f:
        pickle.dump(work_queue, f)


def refresh_queue():
    train()
    for line in work_queue:
        inputs = [actual(line[2]), deadline(line[3]), line[4], line[5]]
        line[-1] = what_network(line[0]).predict(np.array(inputs))[0]
    with open('queue', 'wb') as f:
        pickle.dump(work_queue, f)


def new_train(queue_id):
    line = work_queue[queue_id]
    what_network(line[0]).append([[actual(line[2]), deadline(line[3]), line[4], line[5]], line[6]])
    with open('data.pickle', 'wb') as f:
        pickle.dump([phys_lessons, chem_lessons, gum_lessons], f)


def queue_del(queue_id):
    work_queue.pop(queue_id)


def main():
    load()
    train()


if __name__ == '__main__':
    main()
