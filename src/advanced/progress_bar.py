import time


# class display a simple text progress bar
class ProgressBar:

    def __init__(self, total: int, prefix='Progress: ',
                 suffix='Complete', decimals=1, length=50, fill='█', print_end="\r"):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.print_progress_bar(0)

        """
        Initialize progress bar
        @params:            
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """

    def __print_progress_bar(self, iteration: int):
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (iteration / float(self.total)))
        filled_length = int(self.length * iteration // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end=self.print_end)

    # Print iterations progress
    def print_progress_bar(self, iteration: int):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
        """
        self.__print_progress_bar(iteration=iteration)
        # Print New Line on Complete
        if iteration == self.total:
            print()

    def print_progress_bar_iter(self, iterable):
        self.total = len(iterable)
        self.__print_progress_bar(0)
        for i, item in enumerate(iterable):
            yield item
            self.__print_progress_bar(i+1)
        print()


# usage
def _main():
    # A List of Items
    items = list(range(0, 57))
    length = len(items)

    # Initial call to print 0% progress
    progress = ProgressBar(total=length, fill='#')
    for i, item in enumerate(items):
        time.sleep(0.1)
        # Update Progress Bar
        progress.print_progress_bar(i+1)

    for item in progress.print_progress_bar_iter(items):
        time.sleep(0.1)


if __name__ == '__main__':
    _main()
