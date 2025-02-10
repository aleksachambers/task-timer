"""
Program: run_task
Aleksa Chambers
2/8/2025

The Task object is used in the main file to run the timer. 
There are three methods for this object: Start, Current_Time, and End.
"""
import time 
import csv

class Task:
    def __init__(self):
        self.tasks = {}
        self.n = 1

    def start(self):
        """This grabs the starting time."""
        start_time = time.time()
        start_time_display = time.strftime("%H:%M:%S")
        self.tasks[self.n] = {'start_time':start_time,
                                'start_time_display':start_time_display,
                                'end_time_display':None,
                                'end_time':None,
                                'is_running':True}
        print(f"Task {self.n} started at {start_time_display}.")
        #self.running = True
        self.current_task()

    
    def current_task(self):
        """This runs the timer, and gives the option to see the current time, start a new task, or stop the timer."""
        while True:  # This runs until the task is stopped or a new task is started
            for task_number in self.tasks:
                if self.tasks[task_number]['is_running']:
                    # Get the current time elapsed for each running task
                    current_time = time.time() - self.tasks[task_number]['start_time']
                    minutes = int(current_time // 60)
                    seconds = int(current_time % 60)
                    print(f"**Task {task_number} running for {minutes} minutes and {seconds} seconds.**")
            time.sleep(1)

            # Give user options
            choice = input(f"To stop type 'stop'.\n To start timing a new task, type 'new'.\n Otherwise to see current time, hit 'ENTER'. ")
            if choice == 'stop':
                stop_number = int(input("Type the number of the task you would like to stop. "))
                if stop_number in self.tasks and self.tasks[stop_number]['is_running']:
                    self.end(stop_number)
                else:
                    pass
            elif choice == 'new':
                self.new_task()
                break
            else:
                pass
            
            # Check if all tasks have been stopped
            if all(task['is_running'] == False for task in self.tasks.values()):
                break



    def end(self, stop_number):
        """This grabs the ending time and calculates the total time."""
        if stop_number in self.tasks and self.tasks[stop_number]['is_running']:
            # Only stop the selected task
            self.tasks[stop_number]['is_running'] = False
            end_time = time.time()
            end_time_display = time.strftime("%H:%M:%S")
            final_time = end_time - self.tasks[stop_number]['start_time']
            minutes = int(final_time // 60)
            seconds = int(final_time % 60)
            self.tasks[stop_number]['end_time'] = end_time
            self.tasks[stop_number]['end_time_display']=end_time_display
            print(f"Task {stop_number} ended at {end_time_display}.\n Task took {minutes} minutes, and {seconds} seconds to complete.")
            self.timesheet()

    def new_task(self):
        """Starts timing a new task for the user."""
        self.n += 1
        self.start()

    def timesheet(self):
        print(self.tasks)
        with open('timesheet.csv', 'w', newline='') as csvfile:
            timewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            timewriter.writerow(['Task', ' Start Time', ' End Time'])
            for task_number, task_info in self.tasks.items():
                if task_info['end_time']:
                    timewriter.writerow([task_number, task_info['start_time_display'], task_info['end_time_display']])