from heatmap_app.heatmap_app import HeatmapApp
from heatmap_app.heatmap_generator import HeatmapGenerator
from heatmap_app.image_canvas import ImageCanvas
from heatmap_app.mouse_tracker import MouseTracker

from vision_models.object_detector import OmDetObjectDetector
from vision_models.box_visualizer import BoxVisualizer

from translator.translator import Translator
from speech.speaker import GTTSSpeaker
from event.event_bus import EventBus
from event.event_type import EventType


# ============================================================
# Event handlers (callbacks)
# ============================================================

def on_image_loaded(img):
    print("[EVENT] Image loaded:", img.shape)

def on_objects_detected(dets):
    print(f"[EVENT] {len(dets)} objects detected")

def on_heat_enter(box):
    print("[EVENT] Heat entered box:", box)

def on_heat_leave(box):
    print("[EVENT] Heat left box:", box)


# ============================================================
# Main
# ============================================================
DEFUALT_GAUSSIAN_SIGMA = 120
DEFUALT_HEAT_DECAY_RATE = 0.9

if __name__ == "__main__":
    # Register event listeners
    bus = EventBus()
    bus.subscribe(EventType.IMAGE_LOADED, on_image_loaded)
    bus.subscribe(EventType.OBJECTS_DETECTED, on_objects_detected)
    bus.subscribe(EventType.HEATMAP_ENTER_THRESHOLD, on_heat_enter)
    bus.subscribe(EventType.HEATMAP_LEAVE_THRESHOLD, on_heat_leave)

    # Construct all components
    canvas = ImageCanvas(mode="image", path="animal.jpg")
    tracker = MouseTracker()
    object_detector = OmDetObjectDetector()
    box_visualizer = BoxVisualizer()
    speaker = GTTSSpeaker(lang="de")
    translator = Translator(source_lang="en", target_lang="de")
    heatmap = HeatmapGenerator(
        height=canvas.H,
        width=canvas.W,
        sigma=DEFUALT_GAUSSIAN_SIGMA,
        decay=DEFUALT_HEAT_DECAY_RATE
    )

    # Launch app
    app = HeatmapApp(canvas, tracker, heatmap, object_detector, box_visualizer, translator, speaker, bus)
    app.run()
