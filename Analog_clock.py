import tkinter as tk
import math
import time

class AnalogClock(tk.Canvas):
    def __init__(self, master=None, size=400):
        super().__init__(master, width=size, height=size, bg='white')
        self.size = size
        self.center = size // 2
        self.radius = size // 2 - 20
        self.create_clock_face()
        self.update_clock()

    def create_clock_face(self):
        # Draw the clock face
        self.create_oval(20, 20, self.size - 20, self.size - 20, fill='lightblue')

        # Draw the hour markers
        for hour in range(12):
            angle = math.radians(hour * 30)  # 30 degrees for each hour
            x = self.center + (self.radius - 10) * math.cos(angle - math.pi / 2)
            y = self.center + (self.radius - 10) * math.sin(angle - math.pi / 2)
            self.create_text(x, y, text=str(hour if hour != 0 else 12), font=('Arial', 14))

    def update_clock(self):
        self.delete('hands')
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate angles for hands
        hour_angle = math.radians(hours * 30 + minutes * 0.5)  # 30 degrees per hour + 0.5 degrees per minute
        minute_angle = math.radians(minutes * 6)  # 6 degrees per minute
        second_angle = math.radians(seconds * 6)  # 6 degrees per second

        # Draw hour hand
        self.create_line(self.center, self.center,
                         self.center + (self.radius * 0.5) * math.cos(hour_angle - math.pi / 2),
                         self.center + (self.radius * 0.5) * math.sin(hour_angle - math.pi / 2),
                         width=6, fill='black', tags='hands')

        # Draw minute hand
        self.create_line(self.center, self.center,
                         self.center + (self.radius * 0.75) * math.cos(minute_angle - math.pi / 2),
                         self.center + (self.radius * 0.75) * math.sin(minute_angle - math.pi / 2),
                         width=4, fill='blue', tags='hands')

        # Draw second hand
        self.create_line(self.center, self.center,
                         self.center + (self.radius * 0.9) * math.cos(second_angle - math.pi / 2),
                         self.center + (self.radius * 0.9) * math.sin(second_angle - math.pi / 2),
                         width=2, fill='red', tags='hands')

        # Update the clock every second
        self.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Analog Clock")
    clock = AnalogClock(master=root)
    clock.pack()
    root.mainloop()