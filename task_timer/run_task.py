"""
Program: run_task
Aleksa Chambers
2/8/2025

The Task object is used in the main file to run the timer. 
There are three methods for this object: Start, Current_Time, and End.
"""
import time

class Task:
    def __init__(self):
        self.start_time = None
        self.end_time = None 
        self.is_running = False

    def start(self):
        """This grabs the starting time."""
        self.start_time = time.time()
        start_time_display = time.strftime("%H:%M:%S")
        print(f"Task started at {start_time_display}.")
        self.running = True
        self.current_task()
    
    def current_task(self):
        """This runs the timer, and gives the option to either see the current time, or stop the timer."""
        while self.running:
            current_time = time.time() - self.start_time
            minutes = int(current_time // 60)
            seconds = int(current_time % 60)
            print(f"Task running for {minutes} minutes and {seconds} seconds.")
            time.sleep(1)
            stop = input("To stop type 'stop'. Otherwise to see current time, hit 'ENTER'. ")
            if stop == 'stop':
                self.end()
                break


    def end(self):
        """This grabs the ending time and calculates the total time."""
        self.is_running = False
        self.end_time = time.time()
        end_time_display = time.strftime("%H:%M:%S")
        final_time = self.end_time - self.start_time
        minutes = int(final_time // 60)
        seconds = int(final_time % 60)
        print(f"Task ended at {end_time_display}.\n Task took {minutes} minutes, and {seconds} seconds to complete.")