import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# Set background color
Window.clearcolor = (1, 1, 1, 1)

# --- Step Tracking Variables ---
steps_count = 0
distance_walked_km = 0.0
calories_burned = 0.0
trees_donated = 0
step_goal = 10000
android_mode = False

try:
    from jnius import autoclass, cast
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.ACTIVITY_RECOGNITION])
    android_mode = True
except:
    print("[INFO] Running in PC Test Mode.")


class StepCounter(BoxLayout):
    steps = NumericProperty(0)
    distance = NumericProperty(0.0)
    calories = NumericProperty(0.0)
    trees = NumericProperty(0)
    status = StringProperty("Welcome to PlanetFit!")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Logo
        self.logo = Image(source="logo.png", size_hint=(1, 0.3), allow_stretch=True)
        self.add_widget(self.logo)

        # Card-like layout
        self.info_box = GridLayout(cols=1, spacing=10, size_hint=(1, 0.4))

        self.steps_label = Label(text="👣 Steps: 0", font_size=28, color=[0, 0, 0, 1])
        self.distance_label = Label(text="📏 Distance: 0.00 km", font_size=20, color=[0, 0, 0, 1])
        self.calories_label = Label(text="🔥 Calories: 0.00 kcal", font_size=20, color=[0, 0, 0, 1])
        self.tree_label = Label(text="🌳 Trees Donated: 0", font_size=22, color=[0, 0.5, 0, 1])
        self.status_label = Label(text=self.status, font_size=16, color=[0.2, 0.2, 0.2, 1])

        self.info_box.add_widget(self.steps_label)
        self.info_box.add_widget(self.distance_label)
        self.info_box.add_widget(self.calories_label)
        self.info_box.add_widget(self.tree_label)
        self.info_box.add_widget(self.status_label)

        self.add_widget(self.info_box)

        # Progress bar for tree donation
        self.progress_bar = ProgressBar(max=step_goal, value=0, size_hint=(1, 0.05))
        self.add_widget(self.progress_bar)

        if not android_mode:
            self.simulate_button = Button(text="Simulate Step 👟", size_hint=(1, 0.15), background_color=(0.1, 0.6, 0.1, 1), font_size=20)
            self.simulate_button.bind(on_press=self.simulate_step)
            self.add_widget(self.simulate_button)

        if android_mode:
            self.setup_android_sensor()

    def simulate_step(self, instance):
        self.update_steps(self.steps + 1)

    def update_steps(self, steps):
        self.steps = steps
        self.distance = round(self.steps * 0.0008, 3)
        self.calories = round(self.steps * 0.04, 2)

        # Tree donation logic
        if self.steps < 10000:
            self.trees = 0
            remaining = 10000 - self.steps
        else:
            self.trees = 1 + (self.steps - 10000) // 50000
            remaining = 50000 - ((self.steps - 10000) % 50000)

        # Update UI
        self.steps_label.text = f"👣 Steps: {self.steps}"
        self.distance_label.text = f"📏 Distance: {self.distance:.2f} km"
        self.calories_label.text = f"🔥 Calories: {self.calories:.2f} kcal"
        self.tree_label.text = f"🌳 Trees Donated: {self.trees}"
        self.status_label.text = f"Donate next tree in {remaining} steps"

        # Progress bar logic
        if self.steps < 10000:
            self.progress_bar.max = 10000
            self.progress_bar.value = self.steps
        else:
            self.progress_bar.max = 50000
            self.progress_bar.value = (self.steps - 10000) % 50000

    def setup_android_sensor(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Context = autoclass('android.content.Context')
        Sensor = autoclass('android.hardware.Sensor')
        SensorManager = autoclass('android.hardware.SensorManager')
        SensorEventListener = autoclass('android.hardware.SensorEventListener')

        activity = PythonActivity.mActivity
        sensor_service = activity.getSystemService(Context.SENSOR_SERVICE)
        self.sensorManager = cast('android.hardware.SensorManager', sensor_service)
        self.step_sensor = self.sensorManager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER)

        if self.step_sensor is None:
            self.status_label.text = "Step sensor not available"
            return

        self.listener = SensorEventListener()

        def onSensorChanged(event):
            steps = int(event.values[0])
            self.update_steps(steps)

        def onAccuracyChanged(sensor, accuracy):
            pass

        self.listener.onSensorChanged = onSensorChanged
        self.listener.onAccuracyChanged = onAccuracyChanged

        self.sensorManager.registerListener(
            self.listener, self.step_sensor, SensorManager.SENSOR_DELAY_NORMAL
        )


class PlanetFitApp(App):
    def build(self):
        self.icon = 'logo.png'
        return StepCounter()


if __name__ == '__main__':
    PlanetFitApp().run()


