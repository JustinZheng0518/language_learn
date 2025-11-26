from heatmap_app import HeatmapApp
from heatmap_generator import HeatmapGenerator
from image_canvas import ImageCanvas
from mouse_tracker import MouseTracker
from vision_models.object_detector import OmDetObjectDetector
from vision_models.box_visualizer import BoxVisualizer
if __name__ == "__main__":
    canvas = ImageCanvas(mode="blue_background", path="../env.jpg")
    tracker = MouseTracker()
    heatmap = HeatmapGenerator(height=canvas.H, width=canvas.W, sigma=80, decay=0.96)
    object_detector = OmDetObjectDetector()
    box_visualizer = BoxVisualizer()
    app = HeatmapApp(canvas, tracker, heatmap, object_detector, box_visualizer)
    app.run()
