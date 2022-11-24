import os
import omni.ui as ui
from omni.isaac.examples.base_sample import BaseSampleExtension
from omni.isaac.kmr.kmr_ros2 import KMRROS2
from omni.isaac.ui.ui_utils import get_style, dropdown_builder, btn_builder


class KMRROS2Extension(BaseSampleExtension):
    def on_startup(self, ext_id: str):
        super().on_startup(ext_id)
        super().start_extension(
            menu_name="",
            submenu_name="",
            name="KMR ROS2",
            title="KMR ROS2 example standalone",
            doc_link="",
            overview="KMR ROS2 extension",
            file_path=os.path.abspath(__file__),
            sample=KMRROS2(),
        )
        self.environment = "Grid"
        self.robot = "KMR"
        
        self.config_ui_elements = {}
        frame = self.get_frame(index=0)
        self._build_config_ui(frame)

        return


    def set_environment(self, env):
        self.environment=env
    
    def set_robot(self, robot):
        self.robot = robot
   

    def _build_config_ui(self, frame):
        with frame:
            with ui.VStack(style=get_style(), spacing=5, height=0):
                frame.title = "Configuration"
                frame.visible = True

                dropdown_builder(
                    "Environment",
                    items=["Grid", "Simple warehouse", "Warehouse"],
                    default_val=0,
                    on_clicked_fn=lambda env: self.set_environment(env),
                    tooltip="Select environment",
                )

                dropdown_builder(
                    "Robot",
                    items=["KMR", "O3dyn", "Honomic Dummy"],
                    default_val=0,
                    on_clicked_fn=lambda robot: self.set_robot(robot),
                    tooltip="Select environment",
                )

                dict = {
                    "label": "Print env+robot",
                    "type": "button",
                    "text": "Print",
                    "tooltip": "Print",
                    "on_clicked_fn": lambda: print(self.environment, self.robot),
                }
                self.config_ui_elements["Print env+robot"] = btn_builder(**dict)
                self.config_ui_elements["Print env+robot"].enabled = True
