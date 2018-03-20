from .neural import NeuralNetwork
from .data import neural_types
from datetime import date
import numpy as np
import pickle


def sort_by_result(task):
    return task[-1]


class TasksQueue:
    def __init__(self):
        try:
            with open('data/queue', 'rb') as file:
                self._data = pickle.load(file)
        except FileNotFoundError:
            self._data = []
            self.dump()
        self.neural = NetworkTrain()

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, key):
        self._data.pop(key)
        self.dump()

    def dump(self):
        with open('data/queue', 'wb') as file:
            pickle.dump(self._data, file)

    @property
    def data(self):
        return self._data

    def add(self, lesson, work_type, start, end, time, priority):
        inputs = [actual(start), deadline(end), time, priority]
        predict = self.neural.predict(np.array(inputs))[0]
        task = [lesson, work_type, start, end, time, priority, False, predict]
        self._data.append(task)
        self._data.sort(key=sort_by_result, reverse=True)
        self.dump()

    def clear(self):
        self._data.clear()
        self.dump()

    def refresh(self):
        self.neural.train()
        for task in self._data:
            inputs = [actual(task[2]), deadline(task[3]), task[4], task[5]]
            task[-1] = self.neural.predict(np.array(inputs))[0]
        self.dump()


class NetworkTrain:
    def __init__(self):
        try:
            with open('data/trains', 'rb') as file:
                self._trains = pickle.load(file)
        except FileNotFoundError:
            self._trains = []
            self._dump()
        self._net = NeuralNetwork()

    def clear(self):
        self._trains.clear()
        self._dump()
        self.train()

    def train(self, epochs=5000):
        for _ in range(epochs):
            for inputs, correct_predict in self._trains:
                self._net.train(np.array(inputs), correct_predict)

    def _dump(self):
        with open('data/trains', 'wb') as file:
            pickle.dump(self._trains, file)

    def add(self, task):
        self._trains.append([[actual(task[2]), deadline(task[3]), task[4], task[5]], task[-1]])
        self._dump()


def actual(date_start):
    return (date.today() - date_start).days


def deadline(date_end):
    return (date_end - date.today()).days
