from omni.isaac.examples.base_sample import BaseSample



class KMRROS2(BaseSample):
    def __init__(self) -> None:
        super().__init__()
        return

    def setup_scene(self):
        """ used to setup anything in the world, adding tasks happen here for instance.
        """
        world = self.get_world()
        world.scene.add_default_ground_plane()

        return

    async def setup_post_load(self):
        """ called after first reset of the world when pressing load, 
            intializing provate variables happen here.
        """
        return

    async def setup_pre_reset(self):
        """ called in reset button before resetting the world
            to remove a physics callback for instance or a controller reset
        """
        return

    async def setup_post_reset(self):
        """ called in reset button after resetting the world which includes one step with rendering
        """
        return

    def world_cleanup(self):
        """Function called when extension shutdowns and starts again, (hot reloading feature)
        """
        return

