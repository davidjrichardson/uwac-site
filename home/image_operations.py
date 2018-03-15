from wagtail.images.image_operations import Operation
from willow.plugins.pillow import PillowImage


class DesaturationOperation(Operation):
    def construct(self, saturation):
        self.saturation = int(saturation)

        if self.saturation > 100:
            raise ValueError("Desaturation value must be no more than 100%")

    def run(self, willow, image, env):
        return PillowImage(willow.get_pillow_image().convert('L'))
