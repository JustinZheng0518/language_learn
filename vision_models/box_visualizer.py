import numpy as np
import cv2


class BoxVisualizer:
    """
    Draws ONLY rectangle edges (no fill) for multiple bounding boxes.
    Supports:
        • multiple boxes
        • clean outline edges only
        • optional highlight of one specific box
    """

    def __init__(self, default_color=(0, 255, 0), thickness=2, font_scale=1.0):
        self.default_color = default_color
        self.thickness = thickness
        self.font_scale = font_scale
        self.label_colors = {}  # optional

    def set_label_color(self, label, color):
        """Optionally set unique color for a label string."""
        self.label_colors[label] = color

    def draw(self, image_rgb, detections, highlight_index=None):
        """
        Draw multiple bounding box edges.

        detections: [
            { "label": str, "score": float, "box": [x1,y1,x2,y2] },
            ...
        ]
        highlight_index: index to draw in red
        """

        img = image_rgb.copy()

        for i, det in enumerate(detections):
            x1, y1, x2, y2 = map(int, det["box"])
            label = det["label"]
            score = det["score"]

            # Determine color and thickness
            if i == highlight_index:
                color = (0, 0, 255)  # highlight = red
                thickness = self.thickness + 1
            elif label in self.label_colors:
                color = self.label_colors[label]
                thickness = self.thickness
            else:
                color = self.default_color
                thickness = self.thickness

            # -----------------------------
            # Draw *only rectangle edges*
            # -----------------------------
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

            # -----------------------------
            # Minimal text (very small bg)
            # -----------------------------
            text = f"{label} {score:.2f}"
            (tw, th), _ = cv2.getTextSize(
                text, cv2.FONT_HERSHEY_SIMPLEX, self.font_scale, 1
            )

            # Tiny text background rectangle (optional)
            cv2.rectangle(img, (x1, y1 - th - 3), (x1 + tw + 2, y1), color, -1)

            # Draw text itself
            cv2.putText(
                img,
                text,
                (x1 + 1, y1 - 3),
                cv2.FONT_HERSHEY_SIMPLEX,
                self.font_scale,
                (0, 0, 0),  # black text
                1,
                cv2.LINE_AA
            )

        return img
