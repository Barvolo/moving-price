from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests

image = Image.open("/Users/barvolovski/Downloads/351509975_1191197961564448_182628024836522163_n.jpg")

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

# Process the image and get outputs
inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# Post-process the detections
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.65)[0]

# Assume a known reference object size (e.g., door is 203.2 cm tall)
reference_obj_height_in_pixels = 1000  # hypothetical pixel height of the door
real_world_height_of_reference = 203.2  # real world height in cm
scale_factor = real_world_height_of_reference / reference_obj_height_in_pixels  # cm per pixel

# Calculate and print sizes of detected objects in cm
for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    width_px = box[2] - box[0]  # Calculate pixel width of the box
    height_px = box[3] - box[1]  # Calculate pixel height of the box
    width_cm = width_px * scale_factor  # Convert to cm
    height_cm = height_px * scale_factor  # Convert to cm
    
    print(
        f"Detected {model.config.id2label[label.item()]} with confidence {round(score.item(), 3)} "
        f"at location {box}. Estimated size: {round(width_cm, 2)} cm wide x {round(height_cm, 2)} cm high."
    )


    