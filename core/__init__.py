from .neural import NeuralNetwork
from .data import neural_types
from datetime import date
import numpy as np
import pickle


def sort_by_result(lesson):
    return lesson[-1]


class LessonQueue:
    def __init__(self):
        try:
            with open('data/queue', 'rb') as f:
                self._data = pickle.load(f)
        except FileNotFoundError:
            self._data = []
        self.neural = NNStorage()

    def __delitem__(self, key):
        self._data.pop(key)
        self.save_data()

    def save_data(self):
        with open('data/queue', 'wb') as file:
            pickle.dump(self._data, file)

    @property
    def data(self):
        return self._data

    def add(self, lesson, work_type, start, end, time, priority):
        inputs = [actual(start), deadline(end), time, priority]
        predict = self.neural.choose_type(lesson).predict(np.array(inputs))[0]
        line = [lesson, work_type, start, end, time, priority, False, predict]
        self._data.append(line)
        self._data.sort(key=sort_by_result, reverse=True)
        self.save_data()
        return line

    def clear(self):
        self._data.clear()
        self.save_data()

    def refresh(self):
        self.neural.train()
        for line in self._data:
            inputs = [actual(line[2]), deadline(line[3]), line[4], line[5]]
            line[-1] = self.neural.choose_type(line[0]).predict(np.array(inputs))[0]
        self.save_data()


class NNStorage:
    def __init__(self):
        # lessons, networks: phys, chem, gum
        try:
            with open('data/lessons', 'rb') as f:
                self._lessons = pickle.load(f)
        except FileNotFoundError:
            self._lessons = [[], [], []]
        self._networks = NeuralNetwork(), NeuralNetwork(), NeuralNetwork()

    def choose_type(self, x):
        for borders, net in neural_types.items():
            if borders[0] <= x <= borders[1]:
                return self._networks[net]

    def clear(self):
        for i in range(len(self._lessons)):
            self._lessons[i].clear()
        self.train()

    def train(self):
        for net, lesson in zip(self._networks, self._lessons):
            for _ in range(5000):
                for input_stat, correct_predict in lesson:
                    net.train(np.array(input_stat), correct_predict)

    def _dump(self):
        with open('data/lessons', 'wb') as file:
            pickle.dump(self._lessons, file)

    def add(self, queue_line):
        self.choose_type(queue_line[0]).append([
            [actual(queue_line[2]), deadline(queue_line[3]), queue_line[4], queue_line[5]],
            queue_line[6]
        ])
        self._dump()


def actual(date_start):
    return (date.today() - date_start).days


def deadline(date_deadline):
    return (date_deadline - date.today()).days
