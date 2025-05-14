from libqtile import widget
from libqtile.widget import Battery,base
from libqtile.lazy import lazy
from customScripts import colors
import psutil

theme = colors.colors

shutdown_widget = widget.TextBox(
    text=" ⏻ ",  # The power icon (can be replaced with any text or icon)
    fontsize=24,
    foreground=theme["red"],  # Red color for visibility
    mouse_callbacks={
        "Button1": lazy.spawn("shutdown now"),  # Left-click to shutdown
        "Button3": lazy.spawn("reboot"),  # Right-click to reboot
    },
)
class BatteryWidget(base.ThreadPoolText):
    def __init__(self, **config):
        # Set the default update interval (e.g., 10 seconds)
        self.update_interval = 10
        super().__init__("", **config)
        self.add_defaults({})
    def poll(self):
        # Get battery information
        battery = psutil.sensors_battery()
        if battery:
            percent = int(battery.percent)
            if not battery.power_plugged:
                if percent >= 95:
                    return f" {percent}%"
                elif percent >= 90:
                    return f" {percent}%"
                elif percent >= 80:
                    return f"󰂁 {percent}%"
                elif percent >= 70:
                    return f"󰂀 {percent}%"
                elif percent >= 60:
                    return f"󰁿 {percent}%"
                elif percent>= 50:
                    return f"󰁾 {percent}%"
                elif percent >= 40:
                    return f"󰁽 {percent}%"
                elif percent >= 30:
                    return f"󰁼 {percent}%"
                else:
                    return f"󰂃 {percent}%"
            else:
                if percent >= 95:
                    return f"󰂅 {percent}%"
                elif percent >= 90:
                    return f"󰂋 {percent}%"
                elif percent >= 80:
                    return f"󰂊 {percent}%"
                elif percent >= 70:
                    return f"󰢞 {percent}%"
                elif percent >= 60:
                    return f"󰂉 {percent}%"
                elif percent>= 50:
                    return f"󰢝 {percent}%"
                elif percent >= 40:
                    return f"󰂈 {percent}%"
                elif percent >= 30:
                    return f"󰂇 {percent}%"
                else:
                    return f"󰢜 {percent}%"

        else:
            return "No Battery"

