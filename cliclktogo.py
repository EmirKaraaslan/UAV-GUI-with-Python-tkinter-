import tkinter as tk
import tkintermapview
import dronekit
root = tk.Tk()
root.title("Drone Control")
root.geometry("500x500")






import tkinter as tk
import tkintermapview

frame = tk.Frame(root)
frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the map widget and add it to the frame
map_widget = tkintermapview.TkinterMapView(frame, width=600, height=400, corner_radius=0)
map_widget.pack(side=tk.BOTTOM)

###############################click event????##########################


def on_map_click(event):

    lat, lon = event.latitude, event.longitude
    print(f"Clicked on {lat}, {lon}")

map_widget.bind("<Button-1>", on_map_click)


################################click deneme#########################################


def add_marker_event(coords):
    print("Target Location:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="Target Location")
    print("MISSON BEGIN!!!")


map_widget.add_right_click_menu_command(label="SET TARGET",
                                        command=add_marker_event,
                                        pass_coords=True)
######################################################################################
# Default Location
map_widget.set_address("Bahçeşehir Üniversitesi , İstanbul")

########################################DENEMEE





#########################################################################
from dronekit import VehicleMode, LocationGlobalRelative

def fly_to_location(lat, lon):
    # create a mission to fly to the target location
    target_location = LocationGlobalRelative(lat, lon, 10)  # replace 10 with your desired altitude
    cmds = vehicle.commands
    cmds.clear()
    cmds.add(
        Command(
            0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,
            lat, lon, 10  # replace 10 with your desired altitude
        )
    )
    cmds.upload()

    # arm the drone and take off
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    vehicle.simple_takeoff(10)  # replace 10 with your desired altitude

    # wait for the drone to reach the target location
    while vehicle.mode.name == "GUIDED":
        remaining_distance = get_distance_metres(vehicle.location.global_relative_frame, target_location)
        print(f"Distance to target: {remaining_distance}m")
        if remaining_distance <= 1:
            print("Reached target location!")
            break
        time.sleep(1)

    # land the drone and disarm
    vehicle.mode = VehicleMode("LAND")
    time.sleep(5)
    vehicle.armed = False
root.mainloop()
