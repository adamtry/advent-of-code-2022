from PIL import Image
import numpy as np
from nodes import Node, NodePath
import colorsys
import glob


class ImageGenerator:
    def __init__(self, start_node, end_node, nodes, paths):
        self.start_node: Node = start_node
        self.end_node: Node = end_node
        self.nodes: list[Node] = nodes
        self.paths: list[NodePath] = paths
        self.rows = max([node.row for node in self.nodes])
        self._max_value = max([node.value for node in self.nodes])  # 26 for a-z
        self._base_pixel_array = np.array([])
        self.generate_base_image()

    def generate_base_image(self):
        pixels = []
        for _ in range(0, self.rows+1):
            pixels.append([])
        for node in self.nodes:
            value = round(node.value * (100 / self._max_value) + 1, 1)  # range (0-100)
            pixel = colorsys.hls_to_rgb(0.7, value, 1)
            pixels[node.row].append(pixel)
        pixels[self.start_node.row][self.start_node.col] = (0, 150, 50)
        pixels[self.end_node.row][self.end_node.col] = (255, 0, 0)
        self._base_pixel_array = np.array(pixels, dtype=np.uint8)
        image = Image.fromarray(self._base_pixel_array)
        image.save("maps/map0.png")

    def draw_paths(self, paths: list[NodePath]):
        new_pixels = self._base_pixel_array.copy()
        path = None
        for path in paths:
            new_pixels[path.last_node().row][path.last_node().col] = (255, 150, 0)
            self._base_pixel_array[path.nodes[-2].row][path.nodes[-2].col] = (200, 200, 200)
        image = Image.fromarray(new_pixels)
        image.save(f"maps/map{path.length()}.png")

    @staticmethod
    def make_gif(file_name, folder_path: str):
        # Create the frames
        frames = []
        images = sorted(glob.glob(f"{folder_path}/*.png"))
        for image in images:
            new_frame = Image.open(image)
            frames.append(new_frame)

        # Save into a GIF file that loops forever
        frames[0].save(f"{file_name}.gif", format='GIF',
                       duration=100,
                       append_images=frames[1:],
                       save_all=True,
                       loop=0)


