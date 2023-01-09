import unittest
from index import get_data, Node, NodePath
from image_generator import ImageGenerator


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        node_list = get_data("test_input.txt")
        self.assertEqual(
            Node(0, 1, 1),
            node_list[0]
        )
        self.assertEqual(
            Node(0, 0, 0).adjacent_nodes,
            []
        )


class TestGenerateImage(unittest.TestCase):
    def test_generate_image(self):
        start_node, end_node, node_list = get_data("test_input.txt")
        image_generator = ImageGenerator(start_node, end_node, node_list, None)

    def test_overlay_paths(self):
        path = NodePath(Node(2, 0, 1))
        start_node, end_node, node_list = get_data("test_input.txt")
        image_generator = ImageGenerator(start_node, end_node, node_list, None)
