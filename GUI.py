from dronekit import connect, VehicleMode
import time
import tkinter as tk
import dronekit
import folium
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO


def get_vehicle_info(vehicle):
    while True:
        print("Longitude: %s" % vehicle.location.global_relative_frame.lon)
        print("Altitude: %s" % vehicle.location.global_relative_frame.alt)
        print("Latitude: %s" % vehicle.location.global_relative_frame.lat)
        print("Yaw: %s" % vehicle.attitude.yaw)
        print("Pitch: %s" % vehicle.attitude.pitch)
        print("Roll: %s" % vehicle.attitude.roll)
        print("Heading: %s" % vehicle.heading)
        print("Satellites Visible: %d" % satellites_visible)
        print("Battery > Level: %f" % vehicle.battery.level)
        print("Battery > Voltage: %f" % vehicle.battery.voltage)
        print("Battery > Current: %f" % vehicle.battery.current)
        print("EKF is Healthy: %s" % vehicle.ekf_ok)
        print("Last Heartbeat: %s" % vehicle.last_heartbeat)
        print("Speed > Ground Speed: %s" % vehicle.groundspeed)
        print("Speed > Air Speed: %s" % vehicle.airspeed)

        print("\n")
        time.sleep(1)


def print_to_gui(vehicle, root, lon_label, alt_label, lat_label, yaw_label, pitch_label, roll_label, heading_label,
                 satellites_label, batterylevel_label, batteryvoltage_label,
                 batterycurrent_label, ekf_label, lastheartbeat_label, groundspeed_label, airspeed_label):
    while True:
        lon = vehicle.location.global_relative_frame.lon
        alt = vehicle.location.global_relative_frame.alt
        lat = vehicle.location.global_frame.lat
        yaw = vehicle.attitude.yaw
        pitch = vehicle.attitude.pitch
        roll = vehicle.attitude.roll
        heading = vehicle.heading
        satellites = vehicle.gps_0.satellites_visible
        batterylevel = vehicle.battery.level
        batteryvoltage = vehicle.battery.voltage
        batterycurrent = vehicle.battery.current
        lastheartbeat = vehicle.last_heartbeat
        groundspeed = vehicle.groundspeed
        airspeed = vehicle.airspeed
        ekf = vehicle.ekf_ok

        lon_label.config(text="Longitude: %s" % lon)
        alt_label.config(text="Altitude: %s" % alt)
        lat_label.config(text="Latitude: %s" % lat)
        yaw_label.config(text="Yaw: %s" % yaw)
        pitch_label.config(text="Pitch: %s" % pitch)
        roll_label.config(text="Roll: %s" % roll)
        heading_label.config(text="Heading: %s" % heading)
        satellites_label(text="Satellites Visible: %d" % satellites)
        batterylevel_label(text="Battery > Level: %f" % batterylevel)
        batteryvoltage_label(text="Battery > Voltage: %f" % batteryvoltage)
        batterycurrent_label(text="Battery > Current: %f" % batterycurrent)
        ekf_label(text="EKF is Healthy: %s" % ekf)
        lastheartbeat_label(text="Last Heartbeat: %s" % lastheartbeat)
        groundspeed_label(text="Speed > Ground Speed: %s" % groundspeed)
        airspeed_label(text="Speed > Air Speed: %s" % airspeed)
        root.update()
        time.sleep(1)


# Connect to the Pixhawk
vehicle = connect("COM3", wait_ready=True, baud=57600)

# Create the GUI ##########################################

root = tk.Tk()

#Arka Plan Renginin ayarlanması
root.configure(bg='#2a283b')

#uygulama başlatıldığında windows çubuğunda açılan ikonun oluşturulması
root.iconbitmap("C:\\Users\\LENOVO\\Desktop\\dd\\goknil.ico")

#Uygulama çerceve ismi ve pencere boyutarının belirlenmesi
root.title("GÖKNİL Quadcopter GCS Panel")
root.geometry("1800x900")


#Label'da yazılacak text ismi boyutu ve lokasyonunun belirlenmesi
label = tk.Label(root, text=" Quadcopter Flight Informations", font=('Courier New Baltic', 30), bg="#2a283b", fg='white')
label.pack(padx=20,  pady=20)



# Create a PhotoImage object
img = Image.open("C:\\Users\\LENOVO\\Desktop\\dd\\goknil.jpg")
img = ImageTk.PhotoImage(img)

# create a label to display the image
original_image = Image.open("C:\\Users\\LENOVO\\Desktop\\dd\\goknil.jpg")

# Resize the image
resized_image = original_image.resize((200, 200), Image.ANTIALIAS)

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(resized_image)
label = tk.Label(root, image=photo,bd=0)
label.place(x=0, y=0)

satellites_label = tk.Label(root, text="Satellites Visible:", font=('Arial', 16), bg="#2a283b", fg='white')
satellites_label.place(x=70, y=700)


lon_label = tk.Label(root, text="Longitude :", font=('Arial', 16), bg="#2a283b", fg='white')
lon_label.place(x=70, y=750)

alt_label = tk.Label(root, text="Altitude:", font=('Arial', 16), bg="#2a283b", fg='white')
alt_label.place(x=70, y=800)

lat_label = tk.Label(root, text="Latitude:", font=('Arial', 16), bg="#2a283b", fg='white')
lat_label.place(x=70, y=850)

yaw_label = tk.Label(root, text="Yaw:", font=('Arial', 16), bg="#2a283b", fg='white')
yaw_label.place(x=460, y=750)

pitch_label = tk.Label(root, text="Pitch:", font=('Arial', 16), bg="#2a283b", fg='white')
pitch_label.place(x=460, y=800)

roll_label = tk.Label(root, text="Roll:", font=('Arial', 16), bg="#2a283b", fg='white')
roll_label.place(x=460, y=850)

heading_label = tk.Label(root, text="Heading:", font=('Arial', 16), bg="#2a283b", fg='white')
heading_label.place(x=460, y=700)

batterylevel_label = tk.Label(root, text="Battery > Level:", font=('Arial', 16), bg="#2a283b", fg='sky blue')
batterylevel_label.place(x=1400, y=100)

batteryvoltage_label = tk.Label(root, text="Battery > Voltage:", font=('Arial', 16), bg="#2a283b", fg='sky blue')
batteryvoltage_label.place(x=1400, y=150)

batterycurrent_label = tk.Label(root, text="Battery > Current:", font=('Arial', 16), bg="#2a283b", fg='sky blue')
batterycurrent_label.place(x=1400, y=200)

ekf_label = tk.Label(root, text="EKF is Healthy:", font=('Arial', 16), bg="#2a283b", fg='green')
ekf_label.place(x=70, y=300)

lastheartbeat_label = tk.Label(root, text="Last Heartbeat:", font=('Arial', 16), bg="#2a283b", fg='green')
lastheartbeat_label.place(x=70, y=350)


groundspeed_label = tk.Label(root, text="Speed > Ground Speed:", font=('Arial', 16), bg="#2a283b", fg='red')
groundspeed_label.place(x=70, y=500)

airspeed_label = tk.Label(root, text="Speed > Air Speed:", font=('Arial', 16), bg="#2a283b", fg='red')
airspeed_label.place(x=70, y=550)


# Start the GUI and vehicle information update
root.after(0, print_to_gui, vehicle, root, satellites_label, lon_label, alt_label, lat_label, yaw_label, pitch_label,
           roll_label, heading_label, batterylevel_label, batteryvoltage_label,
           batterycurrent_label, ekf_label, lastheartbeat_label, groundspeed_label, airspeed_label)
root.mainloop()
