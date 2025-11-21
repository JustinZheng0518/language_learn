from heatmap_app.heatmap_app import HeatmapApp
from heatmap_app.heatmap_generator import HeatmapGenerator
from heatmap_app.image_canvas import ImageCanvas
from heatmap_app.mouse_tracker import MouseTracker


if __name__ == "__main__":
    canvas = ImageCanvas(mode="image", path="env.jpg")
    tracker = MouseTracker()

    heatmap = HeatmapGenerator(
        height=canvas.H,
        width=canvas.W,
        sigma=80,
        decay=0.96
    )

    app = HeatmapApp(canvas, tracker, heatmap)
    app.run()
