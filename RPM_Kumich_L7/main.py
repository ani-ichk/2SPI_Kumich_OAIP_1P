from abc import ABC, abstractmethod
import csv
import json


class DataProcessor(ABC):
    @abstractmethod
    def load_data(self, source: str):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_data(self, destination: str):
        pass


class TXTProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str):
        with open(source, 'r', encoding='utf-8') as f:
            self.data = f.readlines()

    def process_data(self):
        return len(self.data) if self.data else 0

    def save_data(self, destination: str):
        with open(destination, 'w', encoding='utf-8') as f:
            f.write(f'Обработка {self.process_data()} записей завершена')


class CSVProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str):
        with open(source, 'r', newline='', encoding='utf-8') as f:
            self.data = list(csv.reader(f))

    def process_data(self):
        return len(self.data) if self.data else 0

    def save_data(self, destination: str):
        with open(destination, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([f'Обработка {self.process_data()} записей завершена'])


class JSONProcessor(DataProcessor):
    def __init__(self):
        self.data = []

    def load_data(self, source: str):
        with open(source, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def process_data(self):
        return len(self.data) if self.data else 0

    def save_data(self, destination: str):
        with open(destination, 'w', encoding='utf-8') as f:
            json.dump(f'Обработка {self.process_data()} записей завершена', f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    txt_processor = TXTProcessor()
    csv_processor = CSVProcessor()
    json_processor = JSONProcessor()

    txt_processor.load_data('text1.txt')
    csv_processor.load_data('text2.csv')
    json_processor.load_data('text3.json')

    print(txt_processor.process_data())
    print(csv_processor.process_data())
    print(json_processor.process_data())

    txt_processor.save_data('res_text1.txt')
    csv_processor.save_data('res_text2.csv')
    json_processor.save_data('res_text3.json')