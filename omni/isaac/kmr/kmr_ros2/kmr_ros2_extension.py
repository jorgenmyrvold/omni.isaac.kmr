import os
import omni.ui as ui
from omni.isaac.examples.base_sample import BaseSampleExtension
from omni.isaac.kmr.kmr_ros2 import KMRROS2
from omni.isaac.ui.ui_utils import get_style, dropdown_builder


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
        return

    def _build_config_ui(self):
        frame = ui.CollapsableFrame(
            title="Import Options",
            height=0,
            collapsed=False,
            style=get_style(),
            style_type_name_override="CollapsableFrame",
            horizontal_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_AS_NEEDED,
            vertical_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_ON,
        )
        with frame:
            with ui.VStack(style=get_style(), spacing=5, height=0):
                dropdown_builder(
                    "Environment",
                    items=["Grid", "Simple warehouse", "Warehouse"],
                    default_val=1,
                )