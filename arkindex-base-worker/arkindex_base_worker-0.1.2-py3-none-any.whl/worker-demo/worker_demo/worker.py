# -*- coding: utf-8 -*-
from arkindex_worker.worker import ElementsWorker


class Demo(ElementsWorker):
    def process_element(self, element):
        print("Demo processing element", element)


def main():
    Demo(description="Demo ML worker for Arkindex").run()


if __name__ == "__main__":
    main()
